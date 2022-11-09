import os
import json

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    print("=="*10)
    print(os.system("dir"))

with open("global_const.json","r",encoding="utf-8") as kqs_const:
    kqs_const_json=json.loads(kqs_const.read())
    KQS_CORE_NAME=kqs_const_json["KQS_CORE_NAME"]
    KQS_VERSION=kqs_const_json["KQS_VERSION"]

setuptools.setup(
    name=KQS_CORE_NAME,
    version=KQS_VERSION,
    author="OSMChina",
    author_email="keaitianxinmail@qq.com",
    description="A non-database Python base OSM data parser, with SQL operation simulated",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OSMChina/OSMChina-Keqing_Sword",
    project_urls={
        "Bug Tracker": "https://github.com/OSMChina/OSMChina-Keqing_Sword/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
