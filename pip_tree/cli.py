import argparse
import json
import os

import pip_tree
from pip_tree._version import __version__


class PipTreeCli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Get the dependency tree of your Python virtual environment via Pip."
        )
        parser.add_argument(
            "-p",
            "--path",
            required=False,
            default=pip_tree.SITE_PACKAGES_PATH,
            type=str,
            help=(
                "The path to the site-packages directory of a Python virtual environment. If a path is not provided,"
                " the virtual environment Pip Tree is run from will be used."
            ),
        )
        parser.add_argument(
            "--version",
            action="version",
            version=f"%(prog)s {__version__}",
        )
        parser.parse_args(namespace=self)

    def generate_console_output(self):
        """Take the output of the dependency tree and print to console."""
        print("Generating Pip Tree report...")

        final_output, package_count = pip_tree.generate_pip_tree(os.path.expanduser(self.path))
        console_output = json.dumps(final_output, indent=4)

        print(console_output)
        print(f'Pip Tree report complete! {package_count} dependencies found for "{self.path}".')


def main():
    PipTreeCli().generate_console_output()


if __name__ == "__main__":
    main()
