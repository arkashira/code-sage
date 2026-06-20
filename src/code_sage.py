import argparse
import json
from dataclasses import dataclass
from typing import List

@dataclass
class AnalysisResult:
    file_path: str
    issues: List[str]

def analyze_code(file_path: str) -> AnalysisResult:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            issues = []
            if 'TODO' in content:
                issues.append('TODO comment found')
            if 'FIXME' in content:
                issues.append('FIXME comment found')
            return AnalysisResult(file_path, issues)
    except FileNotFoundError:
        return AnalysisResult(file_path, ['File not found'])

def main() -> None:
    parser = argparse.ArgumentParser(description='Code Sage CLI')
    parser.add_argument('file_path', help='Path to the source file')
    args = parser.parse_args()
    result = analyze_code(args.file_path)
    print(json.dumps(result.__dict__, indent=4))

if __name__ == '__main__':
    main()
