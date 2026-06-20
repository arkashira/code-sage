import pytest
from src.analysis_engine import AnalysisEngine
from src.config import Config

def test_analysis_engine_timeout():
    config = Config(max_analysis_ms=500)
    engine = AnalysisEngine(config)
    with pytest.raises(TimeoutError):
        engine.analyze("test_repository")

def test_analysis_engine_success():
    config = Config(max_analysis_ms=2000)
    engine = AnalysisEngine(config)
    result = engine.analyze("test_repository")
    assert result == "Analysis completed for test_repository"

def test_load_config():
    config = Config(max_analysis_ms=1000)
    assert config.max_analysis_ms == 1000
