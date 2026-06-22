import os
import time
import pytest
from engine import CodeSageEngine

def create_synthetic_repo(tmp_path, num_files: int, lines_per_file: int) -> str:
    """ Create a synthetic Go repository with the specified number of files and lines.
    Each file contains `lines_per_file` lines of dummy Go code.
    """
    for i in range(num_files):
        file_path = tmp_path / f"file_{i}.go"
        with open(file_path, "w", encoding="utf-8") as f:
            for _ in range(lines_per_file):
                f.write("package main\nfunc main() {}\n")
    return str(tmp_path)

def test_ingest_happy_path(tmp_path, caplog):
    """ Test that the engine ingests a synthetic 1M LOC repo within 30 seconds, indexes all files, and logs no fatal errors.
    """
    repo_path = create_synthetic_repo(tmp_path, num_files=1000, lines_per_file=1000)
    engine = CodeSageEngine()
    start = time.perf_counter()
    index = engine.ingest(repo_path)
    elapsed = time.perf_counter() - start
    # Assert ingestion time <= 30 seconds
    assert elapsed <= 30.0, f"Ingestion took {elapsed:.2f}s, exceeding 30s"
    # Assert all files indexed
    assert len(index) == 1000, f"Expected 1000 files, got {len(index)}"
    # Assert total lines counted
    total_lines = sum(index.values())
    assert total_lines == 1000 * 1000 * 2, f"Expected 2,000,000 lines, got {total_lines}"
    # Assert no fatal errors were logged
    error_logs = [rec for rec in caplog.records if rec.levelno >= logging.ERROR]
    assert not error_logs, f"Fatal errors logged: {[rec.message for rec in error_logs]}"

def test_ingest_empty_repo(tmp_path):
    """ Test ingestion of an empty repository returns an empty index.
    """
    engine = CodeSageEngine()
    index = engine.ingest(str(tmp_path))
    assert index == {}, "Expected empty index for empty repo"

def test_ingest_no_go_files(tmp_path):
    """ Test ingestion of a repo with no .go files returns an empty index.
    """
    # Create a non-Go file
    (tmp_path / "README.md").write_text("# README", encoding="utf-8")
    engine = CodeSageEngine()
    index = engine.ingest(str(tmp_path))
    assert index == {}, "Expected empty index when no .go files are present"

def test_ingest_retrigger(tmp_path):
    """ Test that ingestion can be re-triggered and the index updates accordingly.
    """
    engine = CodeSageEngine()
    # First ingestion: one file
    file1 = tmp_path / "a.go"
    file1.write_text("package main\nfunc main() {}\n", encoding="utf-8")
    index1 = engine.ingest(str(tmp_path))
    assert len(index1) == 1, "First ingestion should index one file"
    # Add another file and re-ingest
    file2 = tmp_path / "b.go"
    file2.write_text("package main\nfunc main() {}\n", encoding="utf-8")
    index2 = engine.ingest(str(tmp_path))
    assert len(index2) == 2, "Second ingestion should index two files"
    # Ensure the index reflects the new file
