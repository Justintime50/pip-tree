<div align="center">

# Pip Tree

Get the dependency tree of your Python virtual environment via Pip.

[![Build Status](https://github.com/Justintime50/pip-tree/workflows/build/badge.svg)](https://github.com/Justintime50/pip-tree/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/pip-tree/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/pip-tree?branch=main)
[![PyPi](https://img.shields.io/pypi/v/pip-tree)](https://pypi.org/project/pip-tree/)
[![Licence](https://img.shields.io/github/license/justintime50/pip-tree)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/pip-tree/showcase.png" alt="Showcase">

</div>

There is no simple, native way to get the dependency tree of a Python virtual environment using the Pip package manager for Python. Pip Tree fixes this problem by retrieving every package from your virtual environment and returning a list of JSON objects that include the package name, version installed, date updated, and which packages are required by each package (the tree).

## Install

```bash
# Install Pip Tree
pip3 install pip-tree

# Install locally
make install

# Get Makefile help
make help
```

## Usage

```
Usage:
    pip-tree --path "path/to/my_project/venv/lib/python3.9/site-packages"

Options:
    -h, --help            show this help message and exit
    -p PATH, --path PATH  The path to the site-packages directory of a Python virtual environment.
```

**Package**

```python
from pip_tree import PipTree

path = 'path/to/my_project/venv/lib/python3.9/site-packages'

package_list = PipTree.get_pip_package_list(path)
for package in package_list:
    package_object = PipTree.get_package_object(package)
    package_details = PipTree.get_package_details(package_object)
    print(package_details.project_name)
```

**Sample Output**

```json
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
            "itsdangerous>=2.0",
            "click>=7.1.2",
            "Werkzeug>=2.0",
            "Jinja2>=3.0"
        ],
        "required_by": []
    }
]

Pip Tree report complete! 40 dependencies found for "path/to/my_project/venv/lib/python3.9/site-packages".
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run test coverage
make coverage
```
