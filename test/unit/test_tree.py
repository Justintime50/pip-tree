import sys

import mock
import pytest
from pip_tree import PipTree


def get_python_version():
    return sys.version.split(' ')[0][:3]


@mock.patch('pip_tree.tree.PIP_PATH', f'./venv/lib/python{get_python_version()}/site-packages')
def test_get_package_details(expected_tree_output, expected_package_count):
    package_details, package_count = PipTree.generate_pip_tree()
    assert package_details == expected_tree_output
    assert package_count == expected_package_count


@mock.patch('pip_tree.tree.PIP_PATH', None)
def test_no_pip_path():
    message = 'PIP_PATH environment variable is required to run Pip Tree.'
    with pytest.raises(ValueError) as error:
        _ = PipTree.generate_pip_tree()
    assert message == str(error.value)
