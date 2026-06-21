import re
from dataclasses import dataclass, field
from typing import List, Callable, Dict, Any

@dataclass
class Suggestion:
    """Represents a single code review suggestion."""
    message: str
    line: int = None
    severity: str = "suggestion"  # could be "warning" or "error"

@dataclass
class Reviewer:
    """Personalized code reviewer."""
    style_profile: Dict[str, Any] = field(default_factory=dict)
    context: Dict[str, Any] = field(default_factory=dict)
    custom_rules: List[Callable[[str, int, Dict[str, Any]], List[Suggestion]]] = field(default_factory=list)

    def analyze(self, code: str) -> List[Suggestion]:
        """Return a list of suggestions based on style, context, and custom rules."""
        suggestions: List[Suggestion] = []
        # Default rule: line length
        max_len = self.style_profile.get("max_line_length", 80)
        for idx, line in enumerate(code.splitlines(), start=1):
            if len(line) > max_len:
                suggestions.append(
                    Suggestion(
                        message=f"Line {idx} exceeds maximum length of {max_len} characters.",
                        line=idx,
                        severity="warning",
                    )
                )
        # Default rule: trailing whitespace
        for idx, line in enumerate(code.splitlines(), start=1):
            if line.rstrip() != line:
                suggestions.append(
                    Suggestion(
                        message=f"Line {idx} has trailing whitespace.",
                        line=idx,
                        severity="warning",
                    )
                )
        # Context-based suggestion: project name
        project_name = self.context.get("project_name")
        if project_name:
            suggestions.append(
                Suggestion(
                    message=f"Consider adding a module docstring mentioning the project '{project_name}'.",
                    severity="suggestion",
                )
            )
        # Apply custom rules
        for rule in self.custom_rules:
            suggestions.extend(rule(code, len(code.splitlines()), self.context))
        return suggestions

def no_empty_functions_rule(code: str, line_count: int, context: Dict[str, Any]) -> List[Suggestion]:
    """Custom rule: detect empty function definitions."""
    suggestions: List[Suggestion] = []
    pattern = re.compile(r"def\s+\w+\s*\(.*\):\s*(?:pass|#.*)?$")
    for idx, line in enumerate(code.splitlines(), start=1):
        if pattern.match(line.strip()):
            suggestions.append(
                Suggestion(
                    message=f"Function on line {idx} is empty.",
                    line=idx,
                    severity="error",
                )
            )
    return suggestions
