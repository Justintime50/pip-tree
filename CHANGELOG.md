# CHANGELOG

## v0.4.0 (2020-11-24)

* Fixed reference of `PIPPIN_PIP` to `PIP_PATH` now that the package has been renamed
* Removed unused pip variables in favor of the constant `PIP_PATH`
* Updated documentation

## v0.3.0 (2020-11-16)

* Refactored Pippin from a shell script to a Python script
* Now retrieve the pip list as JSON
* Now retrieve the pip package details as RFC-compliant mail header format
* Now with Python, we shell out to pip and run the commands but retrieve the data as machine parseable instead of human readable and chopping it up after the fact
* Added unit tests, updated docs, added Makefile
* Changed name from `Pippin` to `Pip Tree`... stupid PyPi naming rules

## v0.2.0 (2020-11-12)

* Added the version number of the packages to the output
* Removed redundant file deletion to boost performance and decrease file manipulation calls
* Added documentation to better explain what each function does
* Small tweaks throughout

## v0.1.0 (2020-11-10)

* Initial release
* Pippin will generate a report of the dependency breakdown of your Python virtual environment
* Pippin will say the number of dependencies in an environment
* Pippin will take an optional argument allowing you to specify which virtual environment (path to pip) to use
