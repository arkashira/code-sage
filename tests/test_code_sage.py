import json
from code_sage import CodeSage, CodeSageConfig

def test_code_sage_config():
    config = CodeSageConfig(theme='dark', font_size=14)
    assert config.theme == 'dark'
    assert config.font_size == 14

def test_code_sage_get_config():
    config = CodeSageConfig(theme='light', font_size=12)
    code_sage = CodeSage(config)
    assert code_sage.get_config().theme == 'light'
    assert code_sage.get_config().font_size == 12

def test_code_sage_set_config():
    config = CodeSageConfig(theme='dark', font_size=14)
    code_sage = CodeSage(config)
    new_config = CodeSageConfig(theme='light', font_size=12)
    code_sage.set_config(new_config)
    assert code_sage.get_config().theme == 'light'
    assert code_sage.get_config().font_size == 12

def test_code_sage_save_config():
    config = CodeSageConfig(theme='dark', font_size=14)
    code_sage = CodeSage(config)
    code_sage.save_config('config.json')
    with open('config.json', 'r') as f:
        config_data = json.load(f)
    assert config_data['theme'] == 'dark'
    assert config_data['font_size'] == 14

def test_code_sage_load_config():
    config = CodeSageConfig(theme='light', font_size=12)
    code_sage = CodeSage(config)
    code_sage.save_config('config.json')
    code_sage.load_config('config.json')
    assert code_sage.get_config().theme == 'light'
    assert code_sage.get_config().font_size == 12

def test_code_sage_load_config_not_found():
    config = CodeSageConfig(theme='dark', font_size=14)
    code_sage = CodeSage(config)
    try:
        code_sage.load_config('non_existent_config.json')
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Config file not found"
