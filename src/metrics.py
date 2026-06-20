import json
from dataclasses import dataclass
from typing import Optional
from src.config import load_config

@dataclass
class Metrics:
    client_id: str
    analyses_run: int
    average_latency: float
    os_version: str

def collect_metrics() -> Optional[Metrics]:
    config = load_config()
    if not config.telemetry:
        return None
    # Simulate collecting metrics
    return Metrics(
        client_id=config.client_id,
        analyses_run=10,
        average_latency=0.5,
        os_version='Linux'
    )

def send_metrics(metrics: Metrics) -> None:
    # Simulate sending metrics
    print(f'Sending metrics: {metrics}')
