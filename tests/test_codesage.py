import pytest
from codesage import Issue, generate_report, generate_html_report, generate_json_report
import json

def test_generate_report():
    issues = [Issue("Python", "Example issue"), Issue("Java", "Another issue")]
    project_fingerprint = "example-fingerprint"
    report = generate_report(issues, project_fingerprint)
    assert report.timestamp
    assert report.project_fingerprint == project_fingerprint
    assert len(report.issues) == 2

def test_generate_html_report():
    issues = [Issue("Python", "Example issue"), Issue("Java", "Another issue")]
    project_fingerprint = "example-fingerprint"
    report = generate_report(issues, project_fingerprint)
    html_report = generate_html_report(report)
    assert "<html>" in html_report
    assert "<h1>Code Sage Report</h1>" in html_report
    assert "Python: 1" in html_report
    assert "Java: 1" in html_report

def test_generate_json_report():
    issues = [Issue("Python", "Example issue"), Issue("Java", "Another issue")]
    project_fingerprint = "example-fingerprint"
    report = generate_report(issues, project_fingerprint)
    json_report = generate_json_report(report)
    data = json.loads(json_report)
    assert data["timestamp"]
    assert data["project_fingerprint"] == project_fingerprint
    assert len(data["issues"]) == 2

def test_main_html():
    import sys
    import io
    sys.argv = ["codesage", "--format", "html"]
    import codesage
    codesage.main()
    with open("report.html", "r") as f:
        html_report = f.read()
    assert "<html>" in html_report

def test_main_json():
    import sys
    import io
    sys.argv = ["codesage", "--format", "json"]
    import codesage
    codesage.main()
    with open("report.json", "r") as f:
        json_report = f.read()
    data = json.loads(json_report)
    assert data["timestamp"]
    assert data["project_fingerprint"]
    assert len(data["issues"]) == 2
