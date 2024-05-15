from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "transistorfm",
    version = "0.1.0",
    author = "Josh Griffiths",
    author_email = "josh@hakuna.co.uk",
    description = "A Python client for the Transistor.fm API",
    license = "MIT",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['an_example_pypi_project', 'tests'],
    long_description=long_description
)