import pytest
from code_sage import analyze_code, AnalysisResult

def test_analyze_code_found_issues(tmp_path):
    file_path = tmp_path / 'test.py'
    file_path.write_text('TODO: fix this\nFIXME: fix that')
    result = analyze_code(str(file_path))
    assert result.file_path == str(file_path)
    assert result.issues == ['TODO comment found', 'FIXME comment found']

def test_analyze_code_no_issues(tmp_path):
    file_path = tmp_path / 'test.py'
    file_path.write_text('print("Hello World")')
    result = analyze_code(str(file_path))
    assert result.file_path == str(file_path)
    assert result.issues == []

def test_analyze_code_file_not_found():
    result = analyze_code('non_existent_file.py')
    assert result.file_path == 'non_existent_file.py'
    assert result.issues == ['File not found']

def test_main(tmp_path, capsys):
    file_path = tmp_path / 'test.py'
    file_path.write_text('TODO: fix this\nFIXME: fix that')
    import sys
    sys.argv = ['code-sage', str(file_path)]
    from code_sage import main
    main()
    captured = capsys.readouterr()
    assert 'TODO comment found' in captured.out
    assert 'FIXME comment found' in captured.out
