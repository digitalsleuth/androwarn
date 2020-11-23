#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="androwarn",
    version="1.6.1",
    author="Thomas D.",
    author_email="tdebize@mail.com",
    license="LGPL",
    classifiers=[
        "Topic :: Security",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)"
    ],
    url="https://github.com/digitalsleuth/androwarn",
    description= ("Yet another static code analyzer for malicious Android applications"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "androguard >= 3.2.1",
        "future",
        "jinja2",
        "play_scraper",
    ],
    python_requires=">=2.7",
    entry_points={
        "console_scripts": [
            "androwarn = androwarn.androwarn:main",
        ],
    },
    package_data={'': ['*.*', 'README.md', 'COPYING', 'COPYING.LESSER']},
    include_package_data = True,
)

