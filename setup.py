
import sys
from setuptools import setup
from codecs import open
from os import system

# For convenience.
if sys.argv[-1] == "publish":
    system("python setup.py sdist upload")
    sys.exit()

def read(filename):
    kwds = {"encoding": "utf-8"} if sys.version_info[0] >= 3 else {}
    with open(filename, **kwds) as fp:
        contents = fp.read()
    return contents

# Get the version information.
import domain

setup(
    name="domain",
    version=domain.__version__,
    author="Andrew R. Casey",
    author_email="andycasey@gmail.com",
    description="Python client for the Domain property API",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="domain property api client",
    packages=["domain"],
    install_requires=["requests"],
    extras_require={
        "test": ["coverage"]
    },
    package_data={
        "": ["LICENSE"],
    },
    include_package_data=True,
    data_files=None
)
