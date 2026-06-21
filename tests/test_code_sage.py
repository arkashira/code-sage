import pytest
from code_sage import analyze_code, display_results, CodeAnalysisResult

def test_analyze_code_happy_path():
    code = "example_code"
    results = analyze_code(code)
    assert isinstance(results, CodeAnalysisResult)
    assert results.performance_bottlenecks

def test_analyze_code_edge_case_empty_code():
    code = ""
    results = analyze_code(code)
    assert isinstance(results, CodeAnalysisResult)
    assert results.performance_bottlenecks

def test_display_results_happy_path(capsys):
    results = CodeAnalysisResult(["bottleneck1", "bottleneck2"])
    display_results(results)
    captured = capsys.readouterr()
    assert "Performance Bottlenecks:" in captured.out
    assert "- bottleneck1" in captured.out
    assert "- bottleneck2" in captured.out

def test_display_results_edge_case_empty_results(capsys):
    results = CodeAnalysisResult([])
    display_results(results)
    captured = capsys.readouterr()
    assert "Performance Bottlenecks:" in captured.out
    assert captured.out.count("- ") == 0
