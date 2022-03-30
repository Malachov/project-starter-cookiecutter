from mypythontools import tests

# Find paths and add to sys.path to be able to import local modules
tests.setup_tests()

from conftest import {{cookiecutter.project_name}}


def test_1():
    {{cookiecutter.project_name}}.test_function()
    assert True
