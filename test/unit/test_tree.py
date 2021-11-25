import sys

import pip_tree


def test_get_package_details():
    """The poor man's approach to unit testing this library is to feed
    its own virtual environment details to itself and assert they match.

    Asserting the entire collection is difficult due to odd environment
    dependencies (such as pip itself being a different version in build systems),
    so we simply assert that certain attributes exist for a package such as `pytest`.
    """
    # Get the Python version of the invoking process of the tests
    full_python_version = sys.version.split(' ')[0]  # eg: 3.10.0
    python_version_numbers = [number for number in full_python_version.split('.')]  # eg: [3, 10, 0]
    python_version = '.'.join(python_version_numbers[:-1])  # eg: 3.10

    pip_path = f'./venv/lib/python{python_version}/site-packages'
    package_details, package_count = pip_tree.generate_pip_tree(pip_path)

    assert any(item['name'] == 'pytest-cov' for item in package_details)
    assert any('toml' in item['requires'] for item in package_details)
    assert any('pytest' in item['required_by'] for item in package_details)
    assert 20 < package_count < 40  # Assert the package count is within a reasonable number for this package, ~30
