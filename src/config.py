import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    telemetry: bool
    client_id: str
    public_key: str

def load_config() -> Config:
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
            return Config(
                telemetry=data.get('telemetry', False),
                client_id=data.get('client_id', ''),
                public_key=data.get('public_key', '')
            )
    except FileNotFoundError:
        return Config(telemetry=False, client_id='', public_key='')

def save_config(config: Config) -> None:
    with open('config.json', 'w') as f:
        json.dump({
            'telemetry': config.telemetry,
            'client_id': config.client_id,
            'public_key': config.public_key
        }, f)
