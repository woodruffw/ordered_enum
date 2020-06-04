#!/usr/bin/env python3

from setuptools import setup

version = {}
with open("./src/ordered_enum/version.py") as f:
    exec(f.read(), version)

with open("./README.md") as f:
    long_description = f.read()

setup(
    name="ordered_enum",
    version=version["__version__"],
    license="MIT with restrictions",
    author="William Woodruff",
    author_email="william@yossarian.net",
    description="A small library for adding total orderings to enums",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woodruffw/ordered_enum",
    packages=["ordered_enum"],
    package_dir={"": "src"},
    platforms="any",
    python_requires=">=3.6",
    extras_require={
        "dev": [
            "flake8",
            "black",
            "isort[pyproject]",
            "pytest",
            "coverage",
            "twine",
        ]
    }
)
