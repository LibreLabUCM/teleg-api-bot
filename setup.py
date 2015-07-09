from setuptools import setup

setup(
    name = 'teleg-api-bot',
    packages = ['telegapi'],
    data_files = [('telegapi',['telegapi/config.yml'])],
    version = '0.0.1',
    description = 'Wrapper to Telegram bots API',
    author = 'LibreLabUCM',
    author_email = 'librelabucm@googlegroups.com',
    url = 'https://github.com/LibreLabUCM/teleg-api-bot',
    install_requires = [
        'Requests',
        'pyyaml'
    ],
    classifiers=[
        'Programming Languaje :: Python',
        'Programming Languaje :: Python :: 3',
        'License :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: in-development',
        'Environment :: Console',
        'Intended Audience :: Bot programmers',
        'Topic :: Fun'
    ]

)