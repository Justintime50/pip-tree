<div align="center">

# Pip Tree

Get the dependency tree of your Python virtual environment via Pip.

[![Build Status](https://github.com/Justintime50/pip-tree/workflows/build/badge.svg)](https://github.com/Justintime50/pip-tree/actions)
[![Coverage Status](https://img.shields.io/codecov/c/github/justintime50/pip-tree)](https://app.codecov.io/github/Justintime50/pip-tree)
[![PyPi](https://img.shields.io/pypi/v/pip-tree)](https://pypi.org/project/pip-tree/)
[![Licence](https://img.shields.io/github/license/justintime50/pip-tree)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/pip-tree/showcase.png" alt="Showcase">

</div>

There is no simple, native way to get the dependency tree of a Python virtual environment using the Pip package manager for Python. Pip Tree fixes this problem by retrieving every package from your virtual environment and returning a list of JSON objects that include the package name, version installed, date updated, and which packages are required by each package (the tree).

## Install

```bash
# Homebrew install
brew tap justintime50/formulas
brew install pip-tree

# Install Pip Tree globally
pip3 install pip-tree

# Install Pip Tree into the virtual environment of the project you want to run it on
venv/bin/pip install pip-tree

# Install locally
just install
```

## Usage

```text
Virtual Env Usage:
    pip-tree

Global Usage:
    pip-tree --path "path/to/my_project/venv/lib/python3.9/site-packages"

Options:
    -h, --help            show this help message and exit
    -p PATH, --path PATH  The path to the site-packages directory of a Python virtual environment. If a path is not provided, the virtual environment Pip Tree is run from will be used.
    --version             show program's version number and exit
```

### Sample Output

```text
Generating Pip Tree Report...

[
    {
        "name": "docopt",
        "version": "0.6.2",
        "updated": "2021-05-12",
        "requires": [],
        "required_by": [
            "coveralls"
        ]
    },
    {
        "name": "flake8",
        "version": "3.9.2",
        "updated": "2021-05-12",
        "requires": [
            "mccabe<0.7.0,>=0.6.0",
            "pyflakes<2.4.0,>=2.3.0",
            "pycodestyle<2.8.0,>=2.7.0"
        ],
        "required_by": []
    },
    {
        "name": "Flask",
        "version": "2.0.0",
        "updated": "2021-05-12",
        "requires": [
            "click>=7.1.2",
            "itsdangerous>=2.0",
            "Jinja2>=3.0"
            "Werkzeug>=2.0",
        ],
        "required_by": []
    }
]

Pip Tree report complete! 40 dependencies found for "path/to/my_project/venv/lib/python3.12/site-packages".
```

### Package

In addition to the CLI tool, you can use functions to retrieve the list of packages and their details from a Python virtual environment in your own code:

```python
import pip_tree

path = 'path/to/my_project/venv/lib/python3.12/site-packages'

package_list = pip_tree.get_pip_package_list(path)
for package in package_list:
    package_details = pip_tree.get_package_details(package)
    print(package_details['name'])
```

## Development

```bash
# Get a comprehensive list of development tools
just --list
```
