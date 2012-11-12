"""
py2app build script for iTunesU credential generator app.

see README.md

"""

from setuptools import setup
setup(
    app=["launch-itu.py"],
    setup_requires=["py2app"],
)
