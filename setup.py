# coding=utf-8
# !/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='amber-python-clients',
    packages=['amber', 'amber.common', 'amber.hokuyo', 'amber.ninedof', 'amber.roboclaw', 'amber.tests'],
    package_dir={'amber': 'src/amber',
                 'amber.common': 'src/amber/common',
                 'amber.hokuyo': 'src/amber/hokuyo',
                 'amber.ninedof': 'src/amber/ninedof',
                 'amber.roboclaw': 'src/amber/roboclaw',
                 'amber.tests': 'src/amber/tests'},
    install_requires=required,
    version='0.2',
    description='Amber clients in python',
    author=u'Paweł Suder',
    author_email='pawel@suder.info',
    url='http://dev.suder.info/',
    download_url='http://github.com/dev-amber/amber-python-clients/',
    keywords=['amber', 'hokuyo', 'roboclaw', 'ninedof', 'panda'],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    long_description='''\
'''
)
