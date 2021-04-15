
from setuptools import setup, find_packages


def main():
    setup(
        name='exampleparser',
        version='1.0',
        description='NOMAD parser implementation for Example.',
        author='The NOMAD Authors',
        license='APACHE 2.0',
        packages=find_packages(exclude=['tests']),
        install_requires=['nomad-lab'])


if __name__ == '__main__':
    main()