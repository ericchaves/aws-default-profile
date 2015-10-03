from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='aws-change-profile',
    version='1.0.0',
    description='Change default AWS profile within profiles defined in credentials file.',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*','config','misc']),
    install_requires=[
        'configparser>=3.3.0'
    ],
    dependency_links = [
    ],
    entry_points={
        'console_scripts': [
            'aws-change-profile=aws_change_profile:main'
        ],
    },
)