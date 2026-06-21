import argparse
import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    offline_mode: bool

def load_config() -> Config:
    try:
        with open('config.json', 'r') as f:
            config_data = json.load(f)
            return Config(offline_mode=config_data['offline_mode'])
    except FileNotFoundError:
        return Config(offline_mode=True)

def save_config(config: Config) -> None:
    with open('config.json', 'w') as f:
        json.dump({'offline_mode': config.offline_mode}, f)

def setup() -> None:
    config = Config(offline_mode=True)
    save_config(config)

def status() -> Dict[str, str]:
    config = load_config()
    return {'offline_mode': 'enabled' if config.offline_mode else 'disabled'}

def main() -> None:
    parser = argparse.ArgumentParser(description='Code Sage CLI')
    subparsers = parser.add_subparsers(dest='command')

    setup_parser = subparsers.add_parser('setup')
    setup_parser.set_defaults(func=setup)

    status_parser = subparsers.add_parser('status')
    status_parser.set_defaults(func=status)

    args = parser.parse_args()
    if args.command:
        args.func()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
