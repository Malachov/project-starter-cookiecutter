"""Utils script helps to build an application."""

from mypythontools_cicd import build


if __name__ == "__main__":

    build.build_app(
        preset="eel",
        console=True,  # True if develop, False in prod
        debug=True,  # True if develop, False in prod
        build_web=True,
        clean=False,
        icon=None,  # "logo.ico"
        datas=[],  # Example: [(file1, "file1")]
        ignored_packages=[],  # Can be dependencies of imported libraries
        hidden_imports=[
            # If app not working, set console to True, open in console and then add library that's missing
        ],
    )
