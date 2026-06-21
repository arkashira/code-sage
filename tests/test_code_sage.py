from code_sage import CodeSage, Error, ErrorType, RefactoringSuggestion

def test_detect_errors():
    code = "print("
    language = "python"
    code_sage = CodeSage(code, language)
    errors = code_sage.detect_errors()
    assert len(errors) == 1
    assert errors[0].type == ErrorType.SYNTAX_ERROR
    assert errors[0].message == "Missing closing parenthesis"
    assert errors[0].line == 1
    assert errors[0].column == 1

def test_provide_refactoring_suggestions():
    code = "x = 5"
    language = "python"
    code_sage = CodeSage(code, language)
    suggestions = code_sage.provide_refactoring_suggestions()
    assert len(suggestions) == 1
    assert suggestions[0].message == "Consider using a constant for the value 5"
    assert suggestions[0].line == 1
    assert suggestions[0].column == 1

def test_highlight_errors_and_suggestions():
    code = "print(x = 5"
    language = "python"
    code_sage = CodeSage(code, language)
    errors = code_sage.detect_errors()
    suggestions = code_sage.provide_refactoring_suggestions()
    highlighted_code = code_sage.highlight_errors_and_suggestions(errors, suggestions)
    assert highlighted_code == "print(x = 5 # Missing closing parenthesis # Consider using a constant for the value 5"

def test_no_errors_or_suggestions():
    code = "print('Hello World')"
    language = "python"
    code_sage = CodeSage(code, language)
    errors = code_sage.detect_errors()
    suggestions = code_sage.provide_refactoring_suggestions()
    assert len(errors) == 0
    assert len(suggestions) == 0
    highlighted_code = code_sage.highlight_errors_and_suggestions(errors, suggestions)
    assert highlighted_code == code
