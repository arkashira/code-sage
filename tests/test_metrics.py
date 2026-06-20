from src.metrics import collect_metrics, send_metrics
import pytest
import json

def test_collect_metrics():
    # Create a config.json file to enable telemetry
    with open('config.json', 'w') as f:
        json.dump({
            'telemetry': True,
            'client_id': 'client-id',
            'public_key': 'public-key'
        }, f)
    metrics = collect_metrics()
    assert metrics
    assert metrics.client_id
    assert metrics.analyses_run > 0
    assert metrics.average_latency > 0
    assert metrics.os_version

def test_send_metrics():
    # Create a config.json file to enable telemetry
    with open('config.json', 'w') as f:
        json.dump({
            'telemetry': True,
            'client_id': 'client-id',
            'public_key': 'public-key'
        }, f)
    metrics = collect_metrics()
    send_metrics(metrics)
    # Simulate sending metrics
    assert True

def test_collect_metrics_disabled():
    # Simulate disabled telemetry
    with open('config.json', 'w') as f:
        json.dump({
            'telemetry': False,
            'client_id': 'client-id',
            'public_key': 'public-key'
        }, f)
    metrics = collect_metrics()
    assert metrics is None
