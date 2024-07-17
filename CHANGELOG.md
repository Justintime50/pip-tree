# CHANGELOG

## v4.0.0 (2024-07-17)

- Remove reliance on `pkg_resources` from `setuptools` and instead uses the `importlib.metadata` module which is builtin
  - Corrects potential issues on Python 3.12+ if `setuptools` wasn't already in the environment
- Sorts `requires` and `required_by` in output

## v3.2.0 (2023-10-25)

- Adds support for Python 3.12

## v3.1.1 (2023-08-27)

- Expand paths for user-supplied strings. This now allows for spaces in paths and proper expansion of home directories (eg: `~`)

## v3.1.0 (2023-08-24)

- Adds `--version` flag

## v3.0.0 (2023-07-01)

- Drop support for Python 3.7

## v2.1.0 (2023-03-25)

- Makes the `path` CLI arg optional, the default value is now the virtual environment that Pip Tree is running from meaning that you can install Pip Tree to a project and run it without needing to specify the `site-packages` directory explicitly

## 2.0.2 (2021-12-02)

- Adds `mypy` type checking and fixes types
- Fixes a potential bug when regex pattern matching on package names would result in `None`

## v2.0.1 (2021-11-25)

- Small bug fix to change the types of functions available in the `__all__` variable to strings

## v2.0.0 (2021-11-25)

- Refactored code
  - Unwrapped functions from `PipTree` class, exposed them outside the package
  - Removed an entire loop and function, now Pip Tree will run even faster
  - Broke out `cli` logic to a separate module
  - Use smarter enumeration for package count
- Added type hinting
- Updated documentation

## v1.1.0 (2021-09-20)

- Drops support for Python 3.6
- Removes unused `mock` library

## v1.0.0 (2021-05-13)

- Switched from shelling out to Pip to using the internal Pip API natively via Python (closes #4 and closes #2), this change makes the previous ~1 minute operation now take ~1 second!
- Adds `updated` field indicating when the package was installed or updated (closes #5)
- The `requires` and `required-by` keys are now lists instead of comma separated strings, they also include the version the requirements are pinned to
- Using `argparse` instead of environment variable to specify path to site-packages
- Separated out code better into classes and additional functions
- 100% code coverage
- Converted classmethods to staticmethods

## v0.5.0 (2020-11-24)

- Removes pip version warnings from output
- Fixes `local variable 'i' referenced before assignment` error
- Matching pip command timeout by setting the subprocess timeout to 15 from 10 seconds
- Running pip commands in isolated mode which ignores custom configuration
- Running pip commands while skipping user input (if ever applicable)
- Small speed improvements were made by shifting logic around

## v0.4.0 (2020-11-24)

- Fixed reference of `PIPPIN_PIP` to `PIP_PATH` now that the package has been renamed
- Removed unused pip variables in favor of the constant `PIP_PATH`
- Updated documentation

## v0.3.0 (2020-11-16)

- Refactored Pippin from a shell script to a Python script
- Now retrieve the pip list as JSON
- Now retrieve the pip package details as RFC-compliant mail header format
- Now with Python, we shell out to pip and run the commands but retrieve the data as machine parseable instead of human readable and chopping it up after the fact
- Added unit tests, updated docs, added Makefile
- Changed name from `Pippin` to `Pip Tree`... stupid PyPi naming rules

## v0.2.0 (2020-11-12)

- Added the version number of the packages to the output
- Removed redundant file deletion to boost performance and decrease file manipulation calls
- Added documentation to better explain what each function does
- Small tweaks throughout

## v0.1.0 (2020-11-10)

- Initial release
- Pippin will generate a report of the dependency breakdown of your Python virtual environment
- Pippin will say the number of dependencies in an environment
- Pippin will take an optional argument allowing you to specify which virtual environment (path to pip) to use
