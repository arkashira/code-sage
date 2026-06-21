import pytest
from reviewer import Reviewer, Suggestion, no_empty_functions_rule

def test_line_length_and_trailing_whitespace():
    code = "def foo():\n print('Hello world!') \n return 42\n"
    reviewer = Reviewer(style_profile={"max_line_length": 20})
    suggestions = reviewer.analyze(code)
    # Expect two suggestions: line length and trailing whitespace
    assert any(s.message == "Line 2 exceeds maximum length of 20 characters." for s in suggestions)
    assert any(s.message == "Line 2 has trailing whitespace." for s in suggestions)
    # No suggestion for line 3
    assert not any(s.message == "Line 3 exceeds maximum length of 20 characters." for s in suggestions)

def test_context_project_name():
    code = "def bar():\n pass\n"
    reviewer = Reviewer(context={"project_name": "Alpha"})
    suggestions = reviewer.analyze(code)
    assert any(s.message == "Consider adding a module docstring mentioning the project 'Alpha'." for s in suggestions)

def test_custom_rule_no_empty_functions():
    code = "def empty():\n pass\n\ndef non_empty():\n print('ok')\n"
    reviewer = Reviewer(custom_rules=[no_empty_functions_rule])
    suggestions = reviewer.analyze(code)
    assert any(s.message == "Function on line 1 is empty." for s in suggestions)
    # Ensure non-empty function is not flagged
    assert not any(s.message == "Function on line 3 is empty." for s in suggestions)

def test_edge_case_empty_code():
    code = ""
    reviewer = Reviewer()
    suggestions = reviewer.analyze(code)
    # No suggestions for empty code
    assert suggestions == []

def test_edge_case_long_line_no_profile():
    code = "a" * 1000
    reviewer = Reviewer()
    suggestions = reviewer.analyze(code)
    # Default max_line_length is 80, so should flag
    assert any(s.message == "Line 1 exceeds maximum length of 80 characters." for s in suggestions)
