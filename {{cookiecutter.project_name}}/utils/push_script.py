"""Push the CI pipeline. Format, create commit from all the changes, push and deploy to PyPi."""

from mypythontools_cicd.project_utils import project_utils_pipeline

if __name__ == "__main__":
    # All the parameters can be overwritten via CLI args
    project_utils_pipeline(
        reformat=True,
        test=True,
        test_options={
            "virtualenvs": ["venv/37", "venv/310"],
            "wsl_virtualenvs": "venv/linux",
            "sync_requirements": "infer",
        },
        version="increment",
        docs=True,
        sync_requirements=None,
        commit_and_push_git=True,
        commit_message="New commit",
        tag="__version__",
        tag_message="New version",
        deploy=True,
        allowed_branches=("master", "main"),
    )

    # project_utils_pipeline(
    #     do_only="deploy",
    # )
