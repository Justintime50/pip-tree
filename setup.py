import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'black',
    'coveralls == 3.*',
    'flake8',
    'isort',
    'mypy',
    'pytest == 6.*',
    'pytest-cov == 2.*',
    'types-setuptools',
]

setuptools.setup(
    name='pip-tree',
    version='2.0.2',
    description='Get the dependency tree of your Python virtual environment via Pip.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/pip-tree',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    package_data={'pip_tree': ['py.typed']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'pip-tree=pip_tree.cli:main',
        ],
    },
    python_requires='>=3.7, <4',
)
