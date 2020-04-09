from setuptools import setup, find_packages
from os import path
from io import open


NAME = "compile-minifier"
VERSION = "0.1.0"

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open("requirements/base.txt") as f:
    REQUIRES = f.read().strip().split("\n")

with open("requirements/ci.txt") as f:
    CI_REQUIRES = f.read().strip().split("\n")


setup(
    name=NAME,
    version=VERSION,
    description="Python compiler and minifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="contact@bimdata.io",
    url="https://github.com/bimdata/compile-minifier",
    install_requires=REQUIRES,
    extras_require={"ci": CI_REQUIRES,},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.5, <4",
    include_package_data=True,
    entry_points={"console_scripts": ["compileminify=main:entrypoint",],},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
