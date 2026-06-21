import argparse
import json
import dataclasses
from datetime import datetime
import os

@dataclasses.dataclass
class Issue:
    language: str
    description: str

@dataclasses.dataclass
class Report:
    timestamp: str
    project_fingerprint: str
    issues: list[Issue]

def generate_report(issues, project_fingerprint):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = Report(timestamp, project_fingerprint, issues)
    return report

def generate_html_report(report):
    html = f"""
    <html>
    <body>
    <h1>Code Sage Report</h1>
    <p>Timestamp: {report.timestamp}</p>
    <p>Project Fingerprint: {report.project_fingerprint}</p>
    <h2>Issues by Language</h2>
    <ul>
    """
    language_counts = {}
    for issue in report.issues:
        if issue.language not in language_counts:
            language_counts[issue.language] = 0
        language_counts[issue.language] += 1
    for language, count in language_counts.items():
        html += f"<li>{language}: {count}</li>"
    html += """
    </ul>
    <p><a href="issues.json">Full Issue Dump</a></p>
    </body>
    </html>
    """
    return html

def generate_json_report(report):
    data = {
        "timestamp": report.timestamp,
        "project_fingerprint": report.project_fingerprint,
        "issues": [{"language": issue.language, "description": issue.description} for issue in report.issues]
    }
    return json.dumps(data, indent=4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["html", "json"])
    args = parser.parse_args()
    issues = [Issue("Python", "Example issue"), Issue("Java", "Another issue")]
    project_fingerprint = "example-fingerprint"
    report = generate_report(issues, project_fingerprint)
    if args.format == "html":
        html_report = generate_html_report(report)
        with open("report.html", "w") as f:
            f.write(html_report)
    elif args.format == "json":
        json_report = generate_json_report(report)
        with open("report.json", "w") as f:
            f.write(json_report)

if __name__ == "__main__":
    main()
