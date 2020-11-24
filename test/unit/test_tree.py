import mock
import pytest
import subprocess
import json
from pip_tree import PipTree


MOCK_PACKAGE_LIST = [
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
    }
]


@mock.patch('pip_tree.tree.PipTree.generate_dependency_tree', return_value=['mock-output', 40])
def test__generate_console_output(mock_dependency_tree):
    PipTree._generate_console_output()
    mock_dependency_tree.assert_called_once()


@mock.patch('pip_tree.tree.PipTree.get_pip_package_list', return_value=[{'name': 'mock-package'}])
@mock.patch('pip_tree.tree.PipTree.get_package_dependencies', return_value=[{'Name': 'mock-package'}, 40])  # noqa
def test_generate_dependency_tree(mock_get_package_dependencies, mock_get_pip_package_list):
    PipTree.generate_dependency_tree()
    mock_get_pip_package_list.assert_called_once()
    mock_get_package_dependencies.assert_called_once_with([{'name': 'mock-package'}])


@mock.patch('subprocess.check_output', return_value=json.dumps([{'Name': 'mock-package'}]))
def test_get_pip_package_list_works(mock_subprocess):
    output = PipTree.get_pip_package_list()
    assert isinstance(output, list)


@mock.patch('subprocess.check_output', side_effect=subprocess.TimeoutExpired(cmd=subprocess.check_output, timeout=0.1))  # noqa
def test_get_pip_package_list_timeout(mock_timeout):
    with pytest.raises(subprocess.TimeoutExpired):
        PipTree.get_pip_package_list()


@mock.patch('subprocess.check_output', side_effect=subprocess.CalledProcessError(returncode=127, cmd=subprocess.check_output))  # noqa
def test_get_pip_package_list_error(mock_error):
    with pytest.raises(subprocess.CalledProcessError):
        PipTree.get_pip_package_list()


@pytest.mark.skip('Need to mock stdout before this will work')
@mock.patch('subprocess.check_output', return_value='TODO')
def test_get_package_dependencies_works(mock_subprocess):
    final_list, package_count = PipTree.get_package_dependencies(MOCK_PACKAGE_LIST)
    assert isinstance(final_list, dict)


@mock.patch('subprocess.check_output', side_effect=subprocess.TimeoutExpired(cmd=subprocess.check_output, timeout=0.1))  # noqa
def test_get_package_dependencies_timeout(mock_timeout):
    package_list = [{'name': 'mock-package'}]
    with pytest.raises(subprocess.TimeoutExpired):
        PipTree.get_package_dependencies(package_list)


@mock.patch('subprocess.check_output', side_effect=subprocess.CalledProcessError(returncode=127, cmd=subprocess.check_output))  # noqa
def test_get_package_dependencies_error(mock_error):
    package_list = [{'name': 'mock-package'}]
    with pytest.raises(subprocess.CalledProcessError):
        PipTree.get_package_dependencies(package_list)
