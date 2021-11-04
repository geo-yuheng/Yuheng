import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keqing_sword-LaoshuBaby",
    version="0.1.0",
    author="LaoshuBaby",
    author_email="keaitianxinmail@qq.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/osmchina/osmchina-keqing_sword",
    project_urls={
        "Bug Tracker": "https://github.com/osmchina/osmchina-keqing_sword/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)