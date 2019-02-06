from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.package_name}}',
    version='1.0',
    packages=find_packages(),
    url='',
    license='',
    author='slavoshevskiy-me',
    author_email='slavoshevskii.mihail@phystech.edu',
    description='',
    install_requires=[
        'click==6.7',
        'tornado==5.0.2',
    ]
)
