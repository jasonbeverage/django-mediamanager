import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mediamanager',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    description='A central repository for Django apps to register any static media that needs to be included.',
    long_description=README,
    author='Jason Beverage',
    url="https://github.com/jasonbeverage/django-mediamanager",
    install_requires=["Django>=1.9"]
)