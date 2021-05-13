import sys

import mock
import pytest
from pip_tree import PipTree


def get_python_version():
    return sys.version.split(' ')[0][:3]


@mock.patch('pip_tree.tree.PIP_PATH', f'./venv/lib/python{get_python_version()}/site-packages')
def test_get_package_details():
    """The poor man's approach to unit testing this library is to feed
    its own virtual environment details to itself and assert they match.

    Asserting the entire collection is difficult due to odd environment
    dependencies (such as pip itself being a different version in build systems),
    simply assert that certain attributes exist for a package such as `pytest`.
    """
    package_details, package_count = PipTree.generate_pip_tree()
    assert any(item['name'] == 'pytest-cov' for item in package_details)
    assert any('toml' in item['requires'] for item in package_details)
    assert any('pytest' in item['required_by'] for item in package_details)
    assert package_count > 1
    assert type(package_count) == int


@mock.patch('pip_tree.tree.PIP_PATH', None)
def test_no_pip_path():
    message = 'PIP_PATH environment variable is required to run Pip Tree.'
    with pytest.raises(ValueError) as error:
        _ = PipTree.generate_pip_tree()
    assert message == str(error.value)
