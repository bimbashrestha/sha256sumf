# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search('^__version__\s*=\s*"(.*)"',
                    open('sha256sumf/sha256sumf.py').read(), re.M).group(1)

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="sha256sumf",
    packages=["sha256sumf"],
    entry_points={"console_scripts": ['sha256sumf = sha256sumf.sha256sumf:main']},
    version=version,
    description="sha256sum for folders",
    long_description=long_descr,
    long_description_content_type="text/markdown",
    author="Bimba Shrestha",
    url="https://github.com/bimbashrestha/sha256sumf",
)
