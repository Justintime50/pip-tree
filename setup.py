import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'coveralls == 3.*',
    'flake8',
    'pytest == 6.*',
    'pytest-cov == 2.*',
]

setuptools.setup(
    name='pip-tree',
    version='1.1.0',
    description='Get the dependency tree of your Python virtual environment via Pip.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/pip-tree',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
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
            'pip-tree=pip_tree.tree:main',
        ],
    },
    python_requires='>=3.7',
)
