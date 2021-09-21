import sys

from pip_tree import PipTree


def test_get_package_details():
    """The poor man's approach to unit testing this library is to feed
    its own virtual environment details to itself and assert they match.

    Asserting the entire collection is difficult due to odd environment
    dependencies (such as pip itself being a different version in build systems),
    so we simply assert that certain attributes exist for a package such as `pytest`.
    """
    python_version = sys.version.split(' ')[0][:3]
    pip_path = f'./venv/lib/python{python_version}/site-packages'
    package_details, package_count = PipTree.generate_pip_tree(pip_path)

    assert any(item['name'] == 'pytest-cov' for item in package_details)
    assert any('toml' in item['requires'] for item in package_details)
    assert any('pytest' in item['required_by'] for item in package_details)
    assert package_count > 0
