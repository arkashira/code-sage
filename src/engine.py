import os
import time
import logging
from typing import Dict

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class CodeSageEngine:
    """ Engine that ingests a Go repository, counts lines per file, and builds an index.
    The engine can be re-triggered without restarting; each ingestion clears the previous state.
    """

    def __init__(self) -> None:
        self._index: Dict[str, int] = {}

    def ingest(self, repo_path: str) -> Dict[str, int]:
        """ Walk the repository directory, count lines in each .go file and build an index.
        Parameters
        ----------
        repo_path : str
            Path to the root of the Go repository.
        Returns
        -------
        Dict[str, int]
            Mapping from relative file path to line count.
        """
        if not os.path.isdir(repo_path):
            raise FileNotFoundError(f"Repository path not found: {repo_path}")
        # Reset index for re-triggerable ingestion
        self._index.clear()
        start = time.perf_counter()
        for root, _, files in os.walk(repo_path):
            for filename in files:
                if not filename.endswith(".go"):
                    continue
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as fh:
                        # Count lines
                        line_count = sum(1 for _ in fh)
                        rel_path = os.path.relpath(file_path, repo_path)
                        self._index[rel_path] = line_count
                except Exception as exc:
                    logger.error(f"Failed to process {file_path}: {exc}")
        elapsed = time.perf_counter() - start
        logger.info(
            f"Ingestion completed in {elapsed:.2f}s, {len(self._index)} files indexed."
        )
        return self._index

    def get_index(self) -> Dict[str, int]:
        """ Return the current index.
        Returns
        -------
        Dict[str, int]
            Current file-to-line-count mapping.
        """
        return dict(self._index)
