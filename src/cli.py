import argparse
from src.config import load_config, save_config
from src.metrics import collect_metrics, send_metrics

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['config', 'send-metrics'])
    args = parser.parse_args()
    if args.command == 'config':
        config = load_config()
        print(f'Telemetry: {config.telemetry}')
        print(f'Client ID: {config.client_id}')
        print(f'Public Key: {config.public_key}')
    elif args.command == 'send-metrics':
        metrics = collect_metrics()
        if metrics:
            send_metrics(metrics)
        else:
            print('Telemetry is disabled')

if __name__ == '__main__':
    main()
