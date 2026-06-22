import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class CodeSageConfig:
    theme: str
    font_size: int

class CodeSage:
    def __init__(self, config: CodeSageConfig):
        self.config = config

    def get_config(self):
        return self.config

    def set_config(self, config: CodeSageConfig):
        self.config = config

    def save_config(self, filename: str):
        with open(filename, 'w') as f:
            json.dump({
                'theme': self.config.theme,
                'font_size': self.config.font_size
            }, f)

    def load_config(self, filename: str):
        try:
            with open(filename, 'r') as f:
                config_data = json.load(f)
            self.config = CodeSageConfig(
                theme=config_data['theme'],
                font_size=config_data['font_size']
            )
        except FileNotFoundError:
            raise ValueError("Config file not found")

    def main(self):
        parser = ArgumentParser(description='Code Sage')
        parser.add_argument('--theme', help='Theme to use')
        parser.add_argument('--font-size', type=int, help='Font size to use')
        parser.add_argument('--save-config', help='Save config to file')
        parser.add_argument('--load-config', help='Load config from file')
        args = parser.parse_args()
        config = CodeSageConfig(theme='default', font_size=12)
        if args.theme:
            config.theme = args.theme
        if args.font_size:
            config.font_size = args.font_size
        code_sage = CodeSage(config)
        if args.save_config:
            code_sage.save_config(args.save_config)
        elif args.load_config:
            code_sage.load_config(args.load_config)
        print(code_sage.get_config())

if __name__ == '__main__':
    code_sage = CodeSage(CodeSageConfig(theme='default', font_size=12))
    code_sage.main()
