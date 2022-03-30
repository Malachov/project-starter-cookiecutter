# TODO change on refactored standalone version

from pathlib import Path

import pandas as pd  # **DELETELINE
import numpy as np  # **DELETELINE

from pyvueeel import pyvueeel_internal
from pyvueeel.pyvueeel_internal import expose

from helpers.misc._misc import print_traceback
import store


# If error in exposed function, this function will log it in python and print out in gui
pyvueeel_internal.expose_error_callback = print_traceback


# If you are not using this template for the first time, you can delete all help unncecessary lines and comments.                   # **DELETELINE
# For example in VS Code, select some than hold ctrl + D after every is selected,                                                   # **DELETELINE
# use ctrl + L to select all lines and use                                                                                          # **DELETELINE


# Expose python functions to Js with decorator                                                                                      # **DELETELINE
# You don't need to use try / except blocks, because it is in expose wrapper                                                        # **DELETELINE
@expose  # **DELETELINE
def test_function(params, arg1="default", arg2="default"):  # **DELETELINE
    #                                                                                                                               # **DELETELINE
    # Passed args should have correct types                                                                                         # **DELETELINE
    print(params, arg1, arg2)  # **DELETELINE
    #                                                                                                                               # **DELETELINE
    # All functions are automatically wrapped by try / except block so if there is an error, it's printed in GUI                    # **DELETELINE
    # You can also use same function for custom errors and info printing                                                            # **DELETELINE
    if params == "fail":  # **DELETELINE
        8 / 0  # **DELETELINE
    #                                                                                                                               # **DELETELINE
    # If you would need to use json where only strings are, you can use                                                             # **DELETELINE
    # mypythontools.pyvueeel.json_to_py(kwargs)                                                                                     # **DELETELINE
    #                                                                                                                               # **DELETELINE
    # Call js function from Py with this syntax                                                                                     # **DELETELINE
    pyvueeel_internal.eel.create_alert(
        "It works",
        "I am js function called from Py",
        None,
    )  # **DELETELINE
    #                                                                                                                               # **DELETELINE
    # You are in function so variables are not global. Save it in store.py so you can use it again.                                 # **DELETELINE
    store.data = pd.DataFrame(
        np.random.randn(100, 3),
        columns=["One", "Two", "Three"],
    )  # **DELETELINE
    #                                                                                                                               # **DELETELINE
    # You can return dict - will be object in js                                                                                    # **DELETELINE
    # You can return list - will be an array in js                                                                                  # **DELETELINE
    #                                                                                                                               # **DELETELINE
    return pyvueeel_internal.to_vue_plotly(store.data)  # **DELETELINE


# Check misc module for how to call javascript from python                                                                          # **DELETELINE

if __name__ == "__main__":

    # If usin multiprocessing, add `is_multiprocessing=True`                                                                        # **DELETELINE
    # If you don't want to run it with pyinstaller, build with npm script and use devel=0 and start with this script                # **DELETELINE
    pyvueeel_internal.run_gui(builded_gui_path=Path(__file__).parent / "gui" / "web_builded")
