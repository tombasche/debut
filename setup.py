from sys import version_info
from setuptools import setup, find_packages

if version_info[0] < 3:
    raise Exception("Must be using Python 3")

VERSION = "0.1"

setup(
    name="debut",
    version=VERSION,
    description="Retro powerpoints in the terminal using curses",
    author="Thomas Basche",
    author_email="tcbasche@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Environment :: Console :: Curses",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7"
    ]
)
