import pytest
import mypythontools_cicd

# Has to be here because of doctest and has to be in tests scripts to be able to import from other folder
mypythontools_cicd.tests.setup_tests()


# Setup imports if using some local packages and global variables if you need
@pytest.fixture(autouse=True)
def setup_tests(doctest_namespace):
    my_global_tests_var = 666
    doctest_namespace["my_global_tests_var"] = my_global_tests_var
