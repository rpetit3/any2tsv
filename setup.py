#!/usr/bin/env python

from setuptools import setup, find_packages

version = "0.0.1"

with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="any2tsv",
    version=version,
    description="Convert various bioinformatic outputs to TSV",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=[
        "parser",
        "bioinformatics",
        "tools",
        "biology",
        "sequencing",
        "parsers",
        "bactopia"
    ],
    author="Robert A. Petit III",
    author_email="robbie.petit@gmail.com",
    url="https://github.com/rpetit3/any2tsv",
    license="MIT",
    entry_points={"console_scripts": ["any2tsv=any2tsv.__main__:run_any2tsv"]},
    install_requires=required,
    packages=find_packages(exclude=("docs")),
    include_package_data=True,
    zip_safe=False,
)
