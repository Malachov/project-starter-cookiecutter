"""
{{cookiecutter.description}}

.. image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}.svg
    :target: https://pypi.python.org/pypi/{{cookiecutter.project_name}}/
    :alt: Python versions

.. image:: https://badge.fury.io/py/{{cookiecutter.project_name}}.svg
    :target: https://badge.fury.io/py/{{cookiecutter.project_name}}
    :alt: PyPI version

.. image:: https://img.shields.io/lgtm/grade/python/github/Malachov/{{cookiecutter.project_name}}.svg
    :target: https://lgtm.com/projects/g/Malachov/{{cookiecutter.project_name}}/context:python
    :alt: Language grade: Python

.. image:: https://readthedocs.org/projects/{{cookiecutter.project_name}}/badge/?version=latest
    :target: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License: MIT

.. image:: https://codecov.io/gh/Malachov/{{cookiecutter.project_name}}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Malachov/{{cookiecutter.project_name}}
    :alt: Codecov

Links
=====

Official documentation - https://{{cookiecutter.project_name}}.readthedocs.io/

Official repo - https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}

{%- if cookiecutter.app_type == 'python package' %}

Installation
============

Python >={{cookiecutter.minimal_python_version}}.

Install with::

    pip install {{cookiecutter.project_name}}

{%- endif %}

{%- if cookiecutter.app_type == 'pyvueeel (desktop & web app)' %}

This is backend of an pyvueeel application. Check readme for how to run and develop such an application.

{%- endif %}
"""

"{%- if cookiecutter.app_type == 'pyvueeel (desktop & web app)' %}"

from {{cookiecutter.project_name}} import app, misc, store

__all__ = ["app", "misc", "store"]

{%- else %}

# from {{cookiecutter.project_name}} import subpackage

__all__ = []  # ["subpackage"]

{%- endif %}


__version__ = "0.0.1"

__author__ = "{{cookiecutter.author}}"  # Change it to your values
__email__ = "{{cookiecutter.author_email}}"  # Change it to your values
__license__ = "MIT"



# Replace this with your imports and do not forget to add it to __all__
# from . import subpackage1
