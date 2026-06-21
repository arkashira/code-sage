import pytest
import json
from code_sage import analyze_codebase, display_results, AnalysisResult

def test_analyze_codebase_happy_path() -> None:
    codebase = "example codebase"
    results = analyze_codebase(codebase)
    assert results.overhead < 0.05
    assert results.accuracy > 0.5
    assert results.relevance > 0.5

def test_analyze_codebase_edge_case_empty_codebase() -> None:
    codebase = ""
    results = analyze_codebase(codebase)
    assert results.overhead == 0
    assert results.accuracy == 0
    assert results.relevance == 0

def test_display_results_happy_path() -> None:
    results = AnalysisResult(0.01, 0.9, 0.8)
    displayed_results = display_results(results)
    assert json.loads(displayed_results) == {
        "overhead": 0.01,
        "accuracy": 0.9,
        "relevance": 0.8
    }
