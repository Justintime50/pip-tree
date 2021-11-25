import datetime
import os
import re
import time
from typing import Dict, List, Tuple

import pkg_resources


class PipTree:
    @staticmethod
    def generate_pip_tree(path: str) -> Tuple[Dict, int]:
        """Generate the Pip Tree of the virtual environment specified."""
        pip_tree_results = []
        required_by_dict = {}
        packages = PipTree.get_pip_package_list(path)

        for package_count, package in enumerate(packages):
            package_details = PipTree.get_package_details(package)
            PipTree.generate_reverse_requires_field(required_by_dict, package_details)
            pip_tree_results.append(package_details)

        # Append the `required_by` field to each record
        for item in pip_tree_results:
            item['required_by'] = sorted(required_by_dict.get(item['name'], []))

        final_output = sorted(pip_tree_results, key=lambda k: k['name'].lower())

        return final_output, package_count

    @staticmethod
    def get_pip_package_list(path: str) -> List[pkg_resources.DistInfoDistribution]:
        """Get the Pip package list of a Python virtual environment.

        Must be a path like: /project/venv/lib/python3.9/site-packages
        """
        packages = pkg_resources.find_distributions(path)

        return packages

    @staticmethod
    def get_package_details(package: pkg_resources.DistInfoDistribution) -> Dict:
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

    @staticmethod
    def generate_reverse_requires_field(required_by_data: Dict, package_details: Dict) -> Dict:
        """Generate a reversed list from the `requires` fields and create a
        collection of each `required_by` fields so each package can show what it's required by.
        """
        requires_list = [item for item in package_details['requires']]
        for required_by_package in requires_list:
            word = re.compile(r'^(\w)+')
            required_by_package_name = word.match(required_by_package).group()

            if required_by_data.get(required_by_package_name):
                required_by_data[required_by_package_name].append(package_details['name'])
            else:
                required_by_data.update({required_by_package_name: [package_details['name']]})

        return required_by_data
