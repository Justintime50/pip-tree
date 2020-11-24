import os
import subprocess
import json
from email.parser import BytesHeaderParser


PIP_PATH = os.getenv('PIP_PATH', 'pip3')
TIMEOUT = 10


class PipTree():
    @classmethod
    def _generate_console_output(cls):
        """Take the output of the dependency tree and print to console.
        """
        print(f'Generating Pip Tree report for "{PIP_PATH}"...')
        console_output, number_of_dependencies = cls.generate_dependency_tree()
        print(json.dumps(console_output, indent=4))
        print(f'Pip Tree report complete! {number_of_dependencies} dependencies found for "{PIP_PATH}".')  # noqa

    @classmethod
    def generate_dependency_tree(cls):
        """Generate the dependency tree of your pip virtual environment
        and print to console.
        """
        package_list = cls.get_pip_package_list()
        dependency_tree, number_of_dependencies = cls.get_package_dependencies(package_list)
        return dependency_tree, number_of_dependencies

    @classmethod
    def get_pip_package_list(cls):
        """Get the pip package list of the virtual environment.
        """
        try:
            command = f'{PIP_PATH} list --format=json'
            package_list_output = subprocess.check_output(
                command,
                stdin=None,
                stderr=None,
                shell=True,
                timeout=TIMEOUT
            )
        except subprocess.TimeoutExpired:
            raise subprocess.TimeoutExpired(command, TIMEOUT)
        except subprocess.CalledProcessError:
            raise subprocess.CalledProcessError(127, command)
        parsed_output = json.loads(package_list_output.decode('utf-8'))
        return parsed_output

    @classmethod
    def get_package_dependencies(cls, package_list):
        """Get a single package dependencies and return a json object
        """
        final_list = []
        for i, package in enumerate(package_list):
            try:
                command = f'{PIP_PATH} show {package["name"]}'
                package_output = subprocess.check_output(
                    command,
                    stdin=None,
                    stderr=None,
                    shell=True,
                    timeout=TIMEOUT
                )
            except subprocess.TimeoutExpired:
                raise subprocess.TimeoutExpired(command, TIMEOUT)
            except subprocess.CalledProcessError:
                raise subprocess.CalledProcessError(127, command)
            parsed_package_output = BytesHeaderParser().parsebytes(
                package_output)
            final_package_output = {
                'name': parsed_package_output['Name'],
                'version': parsed_package_output['Version'],
                'requires': parsed_package_output['Requires'],
                'required-by': parsed_package_output['Required-by'],
            }
            final_list.append(final_package_output)
        return final_list, i


def main():
    PipTree._generate_console_output()


if __name__ == '__main__':
    main()
