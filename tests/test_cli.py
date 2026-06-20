from src.cli import main
import pytest
import sys

def test_cli_config(capsys):
    sys.argv = ['cli.py', 'config']
    main()
    captured = capsys.readouterr()
    assert 'Telemetry:' in captured.out
    assert 'Client ID:' in captured.out
    assert 'Public Key:' in captured.out

def test_cli_send_metrics(capsys):
    sys.argv = ['cli.py', 'send-metrics']
    # Create a config.json file to enable telemetry
    with open('config.json', 'w') as f:
        import json
        json.dump({
            'telemetry': True,
            'client_id': 'client-id',
            'public_key': 'public-key'
        }, f)
    main()
    captured = capsys.readouterr()
    assert 'Sending metrics:' in captured.out
