import pytest


@pytest.fixture
def expected_tree_output():
    """The poor man's approach to unit testing this library is to feed
    its own virtual environment details to itself and assert they match.

    Asserting the entire collection is difficult due to odd environment
    dependencies (such as pip itself being a different version in build systems),
    simply assert against a single large object such as `pytest`.

    This will certainly break when dependencies get bumped. Simply run:
    `venv/bin/pytest -vv`, grab the updated output, and swap the list below.
    """
    expected_tree_output = {'name': 'pytest', 'version': '6.2.4', 'updated': '2021-05-13', 'requires': [
        'attrs>=19.2.0', 'iniconfig', 'packaging', 'pluggy<1.0.0a1,>=0.12', 'py>=1.8.2', 'toml'], 'required_by': ['pytest-cov']}  # noqa

    return expected_tree_output


@pytest.fixture
def expected_package_count():
    """The number of dependencies that are contained in this virtual env.

    See note above for more details.
    """
    expected_package_count = 25
    return expected_package_count
