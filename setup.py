from setuptools import setup

setup(
    name = 'teleg-api-bot',
    packages = ['telegapi'],
    data_files = [('telegapi',['telegapi/config.yml'])],
    version = '0.0.11',
    description = 'Wrapper to Telegram bots API',
    author = 'LibreLabUCM',
    author_email = 'librelabucm@googlegroups.com',
    url = 'https://github.com/LibreLabUCM/teleg-api-bot',
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
