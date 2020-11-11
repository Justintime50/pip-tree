<div align="center">

# Pippin

Get the dependency tree of your Python virtual environment.

[![Build Status](https://travis-ci.com/Justintime50/easypost-cli.svg?branch=master)](https://travis-ci.com/Justintime50/easypost-cli)
[![Licence](https://img.shields.io/github/license/justintime50/easypost-cli)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

> "It comes in Pips?"

There is no simple, native way to get the dependency tree of a Python virtual environment using Pip as the package manager. Pippin fixes this problem by retrieving every package from your virtual environment and returning the packages it depends on as well as what depends on that package. These results will print to console.

Pippin is a quick and dirty solution to getting the dependency tree of your Python projects; however, it should work just fine on most Unix systems.

## Install

```bash
# Setup the tap
brew tap justintime50/formulas

# Install Pippin
brew install pippin
```

## Usage

Invoke Pippin and pass an optional pip path (great for per-project virtual environments). If no optional pip path is passed, the pippin will attempt to use the system `pip3` installation.

```bash
pippin ~/my_project/venv/bin/pip
```

**Sample Output**

```
Generating Pippin Report for "~/my_project/venv/bin/pip"...

Name: coverage
Requires: 
Required-by: pytest-cov, coveralls

Name: coveralls
Requires: docopt, coverage, requests
Required-by: 

Name: flake8
Requires: mccabe, pyflakes, pycodestyle
Required-by: 

Name: pip
Requires: 
Required-by: 

Name: PyGithub
Requires: pyjwt, requests, deprecated
Required-by: github-archive

Name: pytest
Requires: toml, attrs, pluggy, py, iniconfig, packaging
Required-by: pytest-cov

Name: pytest-cov
Requires: coverage, pytest
Required-by: 

Name: requests
Requires: urllib3, certifi, chardet, idna
Required-by: PyGithub, coveralls

Name: setuptools
Requires: 
Required-by: 

Pippin report complete! 9 dependencies found for "~/my_project/venv/bin/pip".
```

## Development

```
shellcheck src/*.sh
```

## Attribution

- Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
