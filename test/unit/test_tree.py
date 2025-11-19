import pip_tree


def test_get_package_details():
    """The poor man's approach to unit testing this library is to feed
    its own virtual environment details to itself and assert they match.

    Asserting the entire collection is difficult due to odd environment
    dependencies (such as pip itself being a different version in build systems),
    so we simply assert that certain attributes exist for a package such as `pytest`.
    """
    package_details, package_count = pip_tree.generate_pip_tree()

    assert any(item["name"] == "pytest" for item in package_details)
    assert any([] == item["requires"] for item in package_details)
    assert any("pytest" in item["required_by"] for item in package_details)
    assert 25 < package_count < 50  # Assert the package count is within a reasonable number for this package
