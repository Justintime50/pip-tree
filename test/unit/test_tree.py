import mock
import pytest
import subprocess
from pip_tree import PipTree


@mock.patch('pip_tree.tree.PipTree.generate_dependency_tree', return_value=['mock-output', 40])
def test__generate_console_output(mock_dependency_tree):
    PipTree._generate_console_output()
    mock_dependency_tree.assert_called_once_with('pip3')


@mock.patch('pip_tree.tree.PipTree.get_pip_package_list', return_value=[{'name': 'mock-package'}])
@mock.patch('pip_tree.tree.PipTree.get_package_dependencies', return_value=[{'Name': 'mock-package'}, 40])  # noqa
def test_generate_dependency_tree(mock_get_package_dependencies, mock_get_pip_package_list):
    PipTree.generate_dependency_tree()
    mock_get_pip_package_list.assert_called_once_with('pip3')
    mock_get_package_dependencies.assert_called_once_with([{'name': 'mock-package'}], 'pip3')


@mock.patch('subprocess.check_output', side_effect=subprocess.TimeoutExpired(cmd=subprocess.check_output, timeout=0.1))  # noqa
def test_get_pip_package_list_timeout(mock_timeout):
    with pytest.raises(subprocess.TimeoutExpired):
        PipTree.get_pip_package_list()


@mock.patch('subprocess.check_output', side_effect=subprocess.CalledProcessError(returncode=127, cmd=subprocess.check_output))  # noqa
def test_get_pip_package_list_error(mock_error):
    with pytest.raises(subprocess.CalledProcessError):
        PipTree.get_pip_package_list()


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
