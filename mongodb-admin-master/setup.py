#!/usr/bin/env python

# ...
import os
from setuptools import setup, find_packages

setup(
    name = "mongo-admin",
    version = "0.1",
    url='http://wiki.secondlife.com/wiki/Eventlet',
    packages=['mongo','mongo.admin','mongo.utils'],
    install_requires=['setuptools','pymongo','psutil'],
    author="Adrian Costia",
    author_email="sysadm.mongodb@gmail.com",
    description="MongoDB-Admin",
	long_description="An easy way to create a cluster",
    keywords = "mongodb shard cluster replicaset replication router ",
    classifiers=[
          "License :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: Beta",
          "Intended Audience :: Developers",
          "Topic :: MongoDB",
    ],
    platforms = ["any"],
    license = "GPL"
)