import traceback

import mylogging
import pyvueeel


def print_traceback(caption="Error", message=""):
    """Print python error to user web based GUI.

    Note:
        Suppose exposed function create_alert from Vue.

    Args:
        message (str, optional): Heading of detailed traceback. Defaults to "Error".
    """
    mylogging.traceback(
        f"Caught error - server still running.\n\n{message}",
        caption,
    )
    pyvueeel.eel.create_alert(
        caption,
        message,
        traceback.format_exc(),
        "error",
    )
