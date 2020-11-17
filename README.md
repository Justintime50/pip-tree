<div align="center">

# Pip Tree

Get the dependency tree of your Python virtual environment via Pip.

[![Build Status](https://travis-ci.com/Justintime50/pip-tree.svg?branch=main)](https://travis-ci.com/Justintime50/pip-tree)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/pip-tree/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/pip-tree?branch=main)
[![PyPi](https://img.shields.io/pypi/v/pip-tree)](https://pypi.org/project/pip-tree/)
[![Licence](https://img.shields.io/github/license/justintime50/pip-tree)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

There is no simple, native way to get the dependency tree of a Python virtual environment using Pip as the package manager. Pip Tree fixes this problem by retrieving every package from your virtual environment and returning the packages it depends on as well as what depends on that package. These results will print to console.

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

Invoke Pip Tree as a script and pass an optional pip path as an environment variable (great for per-project virtual environments). If no optional pip path is passed, then Pip Tree will attempt to use the system `pip3` installation.

```bash
PIPPIN_PIP="~/my_project/venv/bin/pip" pip-tree
```

You can also import Pip Tree as a package and build custom logic for your needs. Pip Tree will return an array of json objects, each containing the name, version, packages required by the package, and what packages requires that package.

```python
from pip_tree import PipTree

dependency_tree = PipTree.generate_dependency_tree(
    pip='~/my_project/venv/bin/pip'
)

print(dependency_tree)
```

**Sample Output**

```
Generating Pip Tree Report for "~/my_project/venv/bin/pip"...

[
    {
        "name": "aiohttp",
        "version": "3.6.2",
        "requires": "async-timeout, multidict, attrs, yarl, chardet",
        "required-by": "slackclient"
    },
    {
        "name": "astroid",
        "version": "2.4.2",
        "requires": "six, wrapt, lazy-object-proxy",
        "required-by": ""
    },
    {
        "name": "async-timeout",
        "version": "3.0.1",
        "requires": "",
        "required-by": "aiohttp"
    },
    {
        "name": "attrs",
        "version": "19.3.0",
        "requires": "",
        "required-by": "aiohttp"
    },
    ...
]

Pip Tree report complete! 40 dependencies found for "~/my_project/venv/bin/pip".
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

## Attribution

- [GitHub Issue](https://github.com/pypa/pip/issues/5261#issuecomment-388173430) that helped with the refactor to Python
- Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
