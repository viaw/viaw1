from setuptools import setup, find_packages

setup(
    name='pack',
    version='0.0.1',
    author='Vince Knight',
    author_email=('knightva@cardiff.ac.uk'),
    packages=find_packages('src'),
    package_dir={"": "src"},
    description='A library to make research using cards easier',
)