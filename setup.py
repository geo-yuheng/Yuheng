import setuptools

from kqs.global_const import KQS_CORE_NAME, KQS_VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
