from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'teleg-api-bot',
    packages = ['telegapi'],
    version = '0.0.111',
    description = 'Wrapper to Telegram bots API',
    author = 'LibreLabUCM',
    author_email = 'librelabucm@googlegroups.com',
    url = 'https://github.com/LibreLabUCM/teleg-api-bot',
    license = 'GNU General Public License (GPL)',

    include_package_data=True,
    package_data={
        '':['config.yaml'],

    },
    install_requires = [
        'Requests',
        'pyyaml'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)
