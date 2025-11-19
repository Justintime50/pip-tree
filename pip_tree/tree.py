import datetime
import os
import re
import sysconfig
import time
from importlib.metadata import (
    Distribution,
    distributions,
)
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Set,
    Tuple,
)


SITE_PACKAGES_PATH = sysconfig.get_paths()["platlib"]


def generate_pip_tree(path: str = SITE_PACKAGES_PATH) -> Tuple[List[Dict[str, Any]], int]:
    """Generate the Pip Tree of the virtual environment specified."""
    pip_tree_results = []
    required_by_data: Dict[str, Set[str]] = {}
    package_count = 0

    packages = get_pip_package_list(path)

    for package_count, package in enumerate(packages, start=1):
        package_details = get_package_details(package)
        _generate_reverse_requires_field(required_by_data, package_details)
        pip_tree_results.append(package_details)

    # Append the `required_by` field to each record created from `_generate_reverse_requires_field()`
    for item in pip_tree_results:
        item["required_by"] = sorted(required_by_data.get(item["name"], []))

    final_output = sorted(pip_tree_results, key=lambda k: k["name"].lower())

    return final_output, package_count


def get_pip_package_list(path: str = SITE_PACKAGES_PATH) -> Iterable[Distribution]:
    """Get the Pip package list of a Python virtual environment.

    Must be a path like: /project/venv/lib/python3.12/site-packages
    """
    packages = distributions(path=[path])

    return packages


def get_package_details(package: Distribution) -> Dict[str, Any]:
    """Build a dictionary of details for a package from Pip."""
    package_location = package._path  # type:ignore
    package_updated_at = (
        time.ctime(os.path.getctime(package_location))
        if package_location and os.path.exists(package_location)
        else "unknown"
    )

    requires_list = (
        [sorted(str(requirement.replace(" ", "").split(";")[0]) for requirement in package.requires)]
        if package.requires
        else []
    )

    package_details = {
        "name": package.metadata["Name"],
        "version": package.metadata["Version"],
        "updated": (
            datetime.datetime.strptime(package_updated_at, "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d")
            if package_updated_at != "unknown"
            else "unknown"
        ),
        "requires": sorted([item for sublist in requires_list for item in set(sublist)]),
    }

    return package_details


def _generate_reverse_requires_field(required_by_data: Dict[str, Set[str]], package_details: Dict[str, Any]):
    """Generate a reversed list from the `requires` fields and create a
    collection of each `required_by` fields so each package can show what it's required by.
    """
    requires_list = [item for item in package_details["requires"]]
    for required_by_package in requires_list:
        word = re.compile(r"^(\w)+")
        name_match = word.match(required_by_package)
        required_by_package_name = name_match.group() if name_match is not None else ""

        # If a package is listed, add to its set, otherwise create a new set
        if required_by_package_name in required_by_data:
            required_by_data[required_by_package_name].add(package_details["name"])
        else:
            required_by_data[required_by_package_name] = {package_details["name"]}

    required_by_data = {key: set(value) for key, value in required_by_data.items()}
