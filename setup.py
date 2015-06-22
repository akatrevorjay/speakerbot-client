from setuptools import setup, find_packages

__pkg_name__ = 'speakerbotclient'

import os

version = '0.0.1'

base_dir = os.path.dirname(__file__)

setup(
    author='Trevor Joynson',
    author_email='github@skywww.net',
    name='speakerbotclient',
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    description='Client for Speakerbot',
    install_requires=[
        'requests',
        'click',
        'pymarkovchain',
    ],
    entry_points={
        'console_scripts': [
            'speakerbotclient = speakerbotclient.cli:speakerbot'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    tests_require=[
        'mock'
    ],
    test_suite='tests'
)
