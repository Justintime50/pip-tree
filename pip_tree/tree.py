import datetime
import json
import os
import time

import pkg_resources

PIP_PATH = os.getenv('PIP_PATH')


class PipTree():
    @staticmethod
    def generate_console_output():
        """Take the output of the dependency tree and print to console.
        """
        print('Generating Pip Tree report...')
        final_output, package_count = PipTree.generate_pip_tree()
        print(json.dumps(sorted(final_output, key=lambda k: k['name'].lower()), indent=4))
        print(f'Pip Tree report complete! {package_count} dependencies found for "{PIP_PATH}".')

    @staticmethod
    def generate_pip_tree():
        """Generate the Pip Tree of the virtual environment specified.
        """
        if not PIP_PATH:
            raise ValueError('PIP_PATH environment variable is required to run Pip Tree.')

        final_output = []
        package_count = 0
        packages = PipTree.get_pip_package_list()

        for package in packages:
            package_object = PipTree.get_package_object(package)
            package_details = PipTree.get_package_details(package_object)
            final_output.append(package_details)
            package_count += 1

        return final_output, package_count

    @staticmethod
    def get_pip_package_list():
        """Get the pip package list of the virtual environment.

        Must be a path like: /project/venv/lib/python3.9/site-packages
        """
        packages = pkg_resources.find_distributions(PIP_PATH)
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
        package_details = {
            'name': package.project_name,
            'version': package.version,
            'updated': datetime.datetime.strptime(package_update_at, "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d"),
            'requires': [sorted(str(requirement) for requirement in package.requires())],
            # TODO: Add in the ability to see requirements in revers. May need to reverse the tree
            # 'required-by': [str(requirement) for requirement in package.as_requirement()],
        }
        return package_details


def main():
    PipTree.generate_console_output()


if __name__ == '__main__':
    main()
