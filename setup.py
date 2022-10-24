#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='tap-netsuite',
    version='1.5.17',
    description='Singer.io tap for extracting data from the NetSuite SOAP',
    author='hotglue',
    url='https://hotglue.xyz/',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['tap_netsuite'],
    install_requires=[
        'netsuitesdk @ git+https://github.com/xg1990/netsuite-sdk-py.git@1fa057d12f96cf7354de7951392cf92e5549543c#egg=netsuitesdk', # USING THE fixed VERSION
        'requests==2.21.0',
        'singer-python==5.3.1',
        'xmltodict==0.11.0',
        'jsonpath-ng==1.4.3',
        'jsonschema==2.6.0',
        'pytz==2018.4'
    ],
    entry_points='''
        [console_scripts]
        tap-netsuite=tap_netsuite:main
    ''',
    packages=find_packages(exclude=['tests']),
    package_data={
        'tap_netsuite.netsuite': ['schemas/*.json']
    },
    include_package_data=True,
)
