from setuptools import setup, find_packages

setup(
    name='pack',
    version='0.1',
    author='viaw',
    author_email=('1223614880@qq.com'),
    packages=find_packages('src'),
    package_dir={"": "src"},
    description='A library to make research using cards easier',
)