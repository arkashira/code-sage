import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class ErrorType(Enum):
    SYNTAX_ERROR = 1
    TYPE_ERROR = 2
    LOGIC_ERROR = 3

@dataclass
class Error:
    type: ErrorType
    message: str
    line: int
    column: int

@dataclass
class RefactoringSuggestion:
    message: str
    line: int
    column: int

class CodeSage:
    def __init__(self, code: str, language: str):
        self.code = code
        self.language = language

    def detect_errors(self) -> List[Error]:
        errors = []
        # Simple syntax error detection
        if self.language == "python" and "print(" in self.code and not self.code.endswith(")"):
            errors.append(Error(ErrorType.SYNTAX_ERROR, "Missing closing parenthesis", 1, 1))
        return errors

    def provide_refactoring_suggestions(self) -> List[RefactoringSuggestion]:
        suggestions = []
        # Simple refactoring suggestion
        if self.language == "python" and "x = 5" in self.code:
            suggestions.append(RefactoringSuggestion("Consider using a constant for the value 5", 1, 1))
        return suggestions

    def highlight_errors_and_suggestions(self, errors: List[Error], suggestions: List[RefactoringSuggestion]) -> str:
        highlighted_code = self.code.split("\n")
        for error in errors:
            if error.line - 1 < len(highlighted_code):
                highlighted_code[error.line - 1] = f"{highlighted_code[error.line - 1]} # {error.message}"
        for suggestion in suggestions:
            if suggestion.line - 1 < len(highlighted_code):
                highlighted_code[suggestion.line - 1] = f"{highlighted_code[suggestion.line - 1]} # {suggestion.message}"
        return "\n".join(highlighted_code)

    def main(self):
        code = "print(x = 5"
        language = "python"
        errors = self.detect_errors()
        suggestions = self.provide_refactoring_suggestions()
        highlighted_code = self.highlight_errors_and_suggestions(errors, suggestions)
        print(highlighted_code)

if __name__ == "__main__":
    code_sage = CodeSage("print('Hello World')", "python")
    code_sage.main()
