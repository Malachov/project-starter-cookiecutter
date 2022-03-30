# project-starter-cookiecutter

Project scaffolding fast and easy. Python package or Py / vue / eel desktop application

Install [cookiecutter](https://github.com/cookiecutter/cookiecutter) and run

    cookiecutter https://github.com/Malachov/project-starter-cookiecutter

Answer some questions and you're ready to go.

Empty application contain simple example to be overwritten and look like this

<div align="center"><img src="docs/source/_static/project-starter-gui.png" width="620" alt="project-starter-gui"/></div>

## Further steps

As python package, it's usually used with [readthedocs](https://readthedocs.org/) free hosting that trigger deploys automatically after pushing to master. You need to activate it on readthedocs.

**CI/CD**
Project include `.travis.yml` for Travis CI, but it's not recommended using it. There is file `push_script.py` in folder `utils` which for my use case is better (faster) than travis and can do most of what you want from CI like run pipeline - running tests / generate docs / increment version / push to GitHub / push to PyPi.

You can delete `.travis.yml`. If you want to generate test coverage badge (usually from travis), you can use GitHub actions yml file for pushing codecov coverage file (without token).

Check utils module for more information.

**IDE files**
It also includes some default project specific settings for VS Code. You can also delete it.
