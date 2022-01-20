import sys
sys.path.append('./zadanie2')
from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["behave==1.2.6"]


setup(
    name="zadanie2",
    version="0.0.1",
    author="Dominika Bober",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
)
