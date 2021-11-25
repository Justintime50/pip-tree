import argparse
import json

import pip_tree


class PipTreeCli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Get the dependency tree of your Python virtual environment via Pip.'
        )
        parser.add_argument(
            '-p',
            '--path',
            required=True,
            type=str,
            help='The path to the site-packages directory of a Python virtual environment.',
        )
        parser.parse_args(namespace=self)

    def generate_console_output(self):
        """Take the output of the dependency tree and print to console."""
        print('Generating Pip Tree report...')

        final_output, package_count = pip_tree.generate_pip_tree(self.path)
        console_output = json.dumps(final_output, indent=4)

        print(console_output)
        print(f'Pip Tree report complete! {package_count} dependencies found for "{self.path}".')


def main():
    PipTreeCli().generate_console_output()


if __name__ == '__main__':
    main()
