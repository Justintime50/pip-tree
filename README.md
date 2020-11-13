<div align="center">

# Pippin

Get the dependency tree of your Python virtual environment.

[![Build Status](https://travis-ci.com/Justintime50/pippin.svg?branch=main)](https://travis-ci.com/Justintime50/pippin)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/pippin/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/pippin?branch=main)
[![PyPi](https://img.shields.io/pypi/v/pippin)](https://pypi.org/project/pippin/)
[![Licence](https://img.shields.io/github/license/justintime50/pippin)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

> "It comes in pips?"

There is no simple, native way to get the dependency tree of a Python virtual environment using Pip as the package manager. Pippin fixes this problem by retrieving every package from your virtual environment and returning the packages it depends on as well as what depends on that package. These results will print to console.

Pippin is a quick and dirty solution to getting the dependency tree of your Python projects; however, it should work just fine on most Unix systems.

## Install

```bash
# Install Pippin
pip3 install pippin

# Install locally
make install

# Get Makefile help
make help
```

## Usage

Invoke Pippin as a script and pass an optional pip path as an environment variable (great for per-project virtual environments). If no optional pip path is passed, then Pippin will attempt to use the system `pip3` installation.

```bash
PIPPIN_PIP="~/my_project/venv/bin/pip" pippin
```

You can also import Pippin as a package and build custom logic for your needs. Pippin will return an array of json objects, each containing the name, version, packages required by the package, and what packages requires that package.

```python
from pippin import Pippin

dependency_tree = Pippin.generate_dependency_tree(
    pip='~/my_project/venv/bin/pip'
)

print(dependency_tree)
```

**Sample Output**

```
Generating Pippin Report for "~/my_project/venv/bin/pip"...

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

Pippin report complete! 40 dependencies found for "~/my_project/venv/bin/pip".
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
