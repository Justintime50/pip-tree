import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pippin',
    version='0.3.0',
    description='Get the dependency tree of your Python virtual environment.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/pippin',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': [
            'pytest >= 6.0.0',
            'pytest-cov >= 2.10.0',
            'coveralls >= 2.1.2',
            'flake8 >= 3.8.0',
            'mock >= 4.0.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'pippin=pippin.pip:main'
        ]
    },
    python_requires='>=3.6',
)
