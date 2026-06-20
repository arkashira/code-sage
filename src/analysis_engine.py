import time
from src.config import Config

class AnalysisEngine:
    def __init__(self, config):
        self.config = config

    def analyze(self, repository_name):
        start_time = time.time()
        try:
            # Simulate analysis time
            time.sleep(1)
            if time.time() - start_time > self.config.max_analysis_ms / 1000:
                raise TimeoutError(f"Analysis timed out for {repository_name}")
            return f"Analysis completed for {repository_name}"
        except TimeoutError as e:
            print(f"Timeout status: {e}")
            raise
