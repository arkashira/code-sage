import json
from dataclasses import dataclass

@dataclass
class Config:
    max_analysis_ms: int

def load_config(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return Config(max_analysis_ms=data['max_analysis_ms'])
