import datetime
import os
import re
import time
from typing import Any, Dict, Generator, List, Tuple

import pkg_resources


def generate_pip_tree(path: str) -> Tuple[List[Dict[str, Any]], int]:
    """Generate the Pip Tree of the virtual environment specified."""
    pip_tree_results = []
    required_by_data: Dict[str, List[str]] = {}
    package_count = 0

    packages = get_pip_package_list(path)

    for package_count, package in enumerate(packages, start=1):
        package_details = get_package_details(package)
        _generate_reverse_requires_field(required_by_data, package_details)
        pip_tree_results.append(package_details)

    # Append the `required_by` field to each record created from `_generate_reverse_requires_field()`
    for item in pip_tree_results:
        item['required_by'] = sorted(required_by_data.get(item['name'], []))

    final_output = sorted(pip_tree_results, key=lambda k: k['name'].lower())

    return final_output, package_count


def get_pip_package_list(path: str) -> Generator[pkg_resources.Distribution, None, None]:
    """Get the Pip package list of a Python virtual environment.

    Must be a path like: /project/venv/lib/python3.9/site-packages
    """
    packages = pkg_resources.find_distributions(path)

    return packages


def get_package_details(package: pkg_resources.Distribution) -> Dict[str, Any]:
    """Build a dictionary of details for a package from Pip."""
    package_updated_at = time.ctime(os.path.getctime(package.location))
    requires_list = [sorted(str(requirement) for requirement in package.requires())]

    package_details = {
        'name': package.project_name,
        'version': package.version,
        'updated': datetime.datetime.strptime(package_updated_at, "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d"),
        'requires': [item for sublist in requires_list for item in sublist],
    }

    return package_details


def _generate_reverse_requires_field(required_by_data: Dict[str, List[str]], package_details: Dict[str, Any]):
    """Generate a reversed list from the `requires` fields and create a
    collection of each `required_by` fields so each package can show what it's required by.
    """
    requires_list = [item for item in package_details['requires']]
    for required_by_package in requires_list:
        word = re.compile(r'^(\w)+')
        name_match = word.match(required_by_package)
        if name_match is not None:
            required_by_package_name = name_match.group()
        else:
            required_by_package_name = ''

        # If a package is listed, append to it, otherwise create a new list
        if required_by_data.get(required_by_package_name):
            required_by_data[required_by_package_name].append(package_details['name'])
        else:
            required_by_data.update({required_by_package_name: [package_details['name']]})
