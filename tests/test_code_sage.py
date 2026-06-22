import pytest
import json
from code_sage import analyze_codebase, display_results, AnalysisResult

def test_analyze_codebase_happy_path() -> None:
    codebase = "example_codebase"
    results = analyze_codebase(codebase)
    assert isinstance(results, AnalysisResult)
    assert results.overhead < 5
    assert results.accuracy > 0
    assert results.relevance > 0

def test_analyze_codebase_edge_case_empty_codebase() -> None:
    codebase = ""
    results = analyze_codebase(codebase)
    assert isinstance(results, AnalysisResult)
    assert results.overhead == 0
    assert results.accuracy == 0.9
    assert results.relevance == 0.8

def test_display_results_happy_path() -> None:
    results = AnalysisResult(1.0, 0.9, 0.8)
    displayed_results = display_results(results)
    assert json.loads(displayed_results) == {
        "overhead": 1.0,
        "accuracy": 0.9,
        "relevance": 0.8
    }

def test_display_results_edge_case_zero_values() -> None:
    results = AnalysisResult(0.0, 0.0, 0.0)
    displayed_results = display_results(results)
    assert json.loads(displayed_results) == {
        "overhead": 0.0,
        "accuracy": 0.0,
        "relevance": 0.0
    }
