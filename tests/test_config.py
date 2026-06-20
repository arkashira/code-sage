import json
from src.config import load_config, save_config, Config
import pytest

def test_load_config():
    with open('config.json', 'w') as f:
        json.dump({
            'telemetry': True,
            'client_id': 'client-id',
            'public_key': 'public-key'
        }, f)
    config = load_config()
    assert config.telemetry
    assert config.client_id == 'client-id'
    assert config.public_key == 'public-key'

def test_save_config():
    config = Config(telemetry=True, client_id='client-id', public_key='public-key')
    save_config(config)
    with open('config.json', 'r') as f:
        data = json.load(f)
        assert data['telemetry']
        assert data['client_id'] == 'client-id'
        assert data['public_key'] == 'public-key'

def test_load_config_default():
    # Remove the config.json file if it exists
    import os
    if os.path.exists('config.json'):
        os.remove('config.json')
    config = load_config()
    assert not config.telemetry
    assert not config.client_id
    assert not config.public_key
