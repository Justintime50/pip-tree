import argparse
import datetime
import json
import os
import re
import time

import pkg_resources


class PipTreeCli():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description=(
                'Get the dependency tree of your Python virtual environment via Pip.'
            )
        )
        parser.add_argument(
            '-p',
            '--path',
            required=True,
            help='The path to the site-packages directory of a Python virtual environment.',
        )
        parser.parse_args(namespace=self)

    def generate_console_output(self):
        """Take the output of the dependency tree and print to console.
        """
        print('Generating Pip Tree report...')
        final_output, package_count = PipTree.generate_pip_tree(self.path)
        print(json.dumps(final_output, indent=4))
        print(f'Pip Tree report complete! {package_count} dependencies found for "{self.path}".')


class PipTree():
    @staticmethod
    def generate_pip_tree(path):
        """Generate the Pip Tree of the virtual environment specified.
        """
        pip_tree_results = []
        required_by_dict = {}
        package_count = 0
        packages = PipTree.get_pip_package_list(path)

        for package in packages:
            package_object = PipTree.get_package_object(package)
            package_details = PipTree.get_package_details(package_object)
            PipTree.generate_reverse_requires_field(required_by_dict, package_details)
            pip_tree_results.append(package_details)
            package_count += 1

        # Append the `required_by` field to each record
        for item in pip_tree_results:
            item['required_by'] = sorted(required_by_dict.get(item['name'], []))

        final_output = sorted(pip_tree_results, key=lambda k: k['name'].lower())

        return final_output, package_count

    @staticmethod
    def get_pip_package_list(path):
        """Get the pip package list of the virtual environment.

        Must be a path like: /project/venv/lib/python3.9/site-packages
        """
        packages = pkg_resources.find_distributions(path)
        return packages

    @staticmethod
    def get_package_object(package):
        """Returns a package object from Pip.
        """
        package_object = pkg_resources.get_distribution(package)
        return package_object

    @staticmethod
    def get_package_details(package):
        """Build a dictionary of details for a package from Pip.
        """
        package_update_at = time.ctime(os.path.getctime(package.location))
        requires_list = [sorted(str(requirement) for requirement in package.requires())]
        package_details = {
            'name': package.project_name,
            'version': package.version,
            'updated': datetime.datetime.strptime(package_update_at, "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d"),
            'requires': [item for sublist in requires_list for item in sublist],
        }
        return package_details

    @staticmethod
    def generate_reverse_requires_field(required_by_dict, package_details):
        """Generate a reversed list from the `requires` fields and create a collection
        of each `required_by` fields so each package can show what it's required_by
        """
        requires_list = [item for item in package_details['requires']]
        for required_by_package in requires_list:
            word = re.compile(r'^(\w)+')
            required_by_package_name = word.match(required_by_package).group()

            if required_by_dict.get(required_by_package_name):
                required_by_dict[required_by_package_name].append(package_details['name'])
            else:
                required_by_dict.update(
                    {
                        required_by_package_name: [package_details['name']]
                    }
                )
        return required_by_dict


def main():
    PipTreeCli().generate_console_output()


if __name__ == '__main__':
    main()
