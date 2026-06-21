import pytest
from codesage import setup, status, load_config, save_config

def test_setup():
    setup()
    config = load_config()
    assert config.offline_mode

def test_status():
    setup()
    result = status()
    assert result['offline_mode'] == 'enabled'

def test_status_disabled():
    config = load_config()
    config.offline_mode = False
    save_config(config)
    result = status()
    assert result['offline_mode'] == 'disabled'

def test_load_config_default():
    import os
    if os.path.exists('config.json'):
        os.remove('config.json')
    config = load_config()
    assert config.offline_mode

def test_save_config():
    config = load_config()
    config.offline_mode = False
    save_config(config)
    loaded_config = load_config()
    assert not loaded_config.offline_mode
