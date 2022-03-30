# {{cookiecutter.project_name}}

[![Python versions](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_name}}) [![PyPI version](https://badge.fury.io/py/{{cookiecutter.project_name}}.svg)](https://badge.fury.io/py/{{cookiecutter.project_name}}) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/context:python) [![Documentation Status](https://readthedocs.org/projects/{{cookiecutter.project_name}}/badge/?version=latest)](https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/?badge=latest) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![codecov](https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}})

{{cookiecutter.description}}

## Links

Official documentation - [readthedocs](https://{{cookiecutter.github_user}}.readthedocs.io/)

Official repo - [GitHub](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.github_user}})

{% if cookiecutter.app_type == 'python package' %}
## Installation

Python >=3.6 (Python 2 is not supported).

Install with

```console
pip install {{cookiecutter.github_user}}
```
## Modules

- module1
- module2
{% endif %}
{% if cookiecutter.app_type != 'python package' %}
## How to

To run an app in develop mode, you have to run both frontend and python. Run frontend with debugging app.py (do not run, just debug). Then run frontend with `npm run serve` in gui folder (or use Task explorer if using VS Code). Open your favourite browser and open [http://localhost:8080](http://localhost:8080).

It's recommended to use Vue.js devtools extension where you can see what component is on cursor, edit props values or see list of all used mutations.

In opened app, there is a little help button where there is a simple overview about how to develop with these tools.

Delete is faster than write, so there are many working examples like for example plot, various formatting (flex row, flex column), settings panel, function call from python to JS and vice versa or automatic alerting from python. If you want to see how some example is working, just use **ctrl + F** in IDE or check components for its props.

This is how the example looks like

<div align="center"><img src="docs/source/_static/project-starter-gui.png" width="620" alt="project-starter-gui"/></div>

For a desktop version where the user does not have python installed, you have to build it first. Use mypythontools `build` module (trigger with tasks button).
{% endif %}
