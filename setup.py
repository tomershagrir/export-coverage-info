#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='export-coverage-info',
    version="0.1.2",
    description='TDispatch tiny script',
    long_description='''TDispatch tiny script.''',
    keywords='python',
    author='TDispatch',
    author_email='dev@tdispatch.com',
    url='http://github.com/TDispatch/export-coverage-info/',
    license='Proprietary',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "requests",
        "coverage",
        "responses",
    ],
    scripts=['export_coverage_info.py'],
)
