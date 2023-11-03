## CODE_OF_CONDUCT

### Technical limitation

1. Yuheng project follow the semantic version principal, you can see full text in [SemVer](https://semver.org/).
2. Our commit message follow the conventional commits standard, you can see it at [ConventionalCommits](https://www.conventionalcommits.org/).

### Package release checklist

1. Update version in `/src/yuheng/basic/global_const.py`
2. Run `pre_build_process.py` in root dictionary
3. Now we changed to poetry package management system totally, you just run `poetry build` then `poetry publish` and everything will be done, and don't need to follow [pypa official guidebook](hhttps://packaging.python.org/tutorials/packaging-projects/).
4. If you are living in Mainland of China or other countries/regions that can't access to GitHub and Pypi freely, we suggest you finish above process in a VPS, that don't cost you much time. (In fact, you can consider the VPS as a pure clean virtual environment). We suggest you use GitHub Codespace for open source purpose release. You need to run `pip install poetry` to init package manager environment, and use `poetry config http-basic.pypi <username> <password>` or `poetry config pypi-token.pypi <my-token>` configure your access. You can get more help in [poetry documents](https://python-poetry.org/docs/master/repositories/#configuring-credentials).