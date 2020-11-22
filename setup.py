from setuptools import setup, find_packages

with open("README.md", encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="androwarn",
    version="1.6",
    author="maaaaaz",
    license="GNU GPLv3",
    url="https://github.com/digitalsleuth/androwarn",
    description= ("Yet another static code analyzer for malicious Android applications"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        "androguard >= 3.2.1",
        "future",
        "jinja2",
        "play_scraper",
    ],
    entry_points={
        "console_scripts": [
            "androwarn = androwarn:main",
        ],
    },
    package_data={'': ['*.*', 'README.md', 'COPYING', 'COPYING.LESSER']},
)

