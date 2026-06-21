import time
from dataclasses import dataclass
from typing import List

@dataclass
class CodeAnalysisResult:
    """Dataclass to hold code analysis results"""
    performance_bottlenecks: List[str]

def analyze_code(code: str) -> CodeAnalysisResult:
    """Analyze the given code and return performance bottlenecks"""
    # Simulate code analysis time
    time.sleep(0.1)
    # For demonstration purposes, assume we found some bottlenecks
    performance_bottlenecks = ["bottleneck1", "bottleneck2"]
    return CodeAnalysisResult(performance_bottlenecks)

def display_results(results: CodeAnalysisResult) -> None:
    """Display the code analysis results"""
    print("Performance Bottlenecks:")
    for bottleneck in results.performance_bottlenecks:
        print(f"- {bottleneck}")
