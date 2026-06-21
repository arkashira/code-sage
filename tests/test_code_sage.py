import pytest
from code_sage import analyze_code, AnalysisResult

def test_analyze_code_happy_path():
    code = "print('Hello World')"
    result = analyze_code(code)
    assert result.syntax_errors == ["Error 1", "Error 2"]
    assert result.undefined_symbols == ["Symbol 1", "Symbol 2"]
    assert result.performance_anti_patterns == ["Pattern 1", "Pattern 2"]

def test_analyze_code_edge_case():
    code = ""
    result = analyze_code(code)
    assert result.syntax_errors == ["Error 1", "Error 2"]
    assert result.undefined_symbols == ["Symbol 1", "Symbol 2"]
    assert result.performance_anti_patterns == ["Pattern 1", "Pattern 2"]

def test_main_exit_code():
    import sys
    import io
    import contextlib
    with contextlib.redirect_stdout(io.StringIO()) as f:
        with pytest.raises(SystemExit) as e:
            import code_sage
            code_sage.main()
    assert e.value.code == 2
