import os
from pathlib import Path
import shutil

REMOVE_PATHS = [
    "{% if cookiecutter.app_type == 'python package' -%}",
    
        "gui",
        "utils/build_script.py"
        "{{cookiecutter.project_name}}/app.py"
        "{{cookiecutter.project_name}}/misc.py"
        "{{cookiecutter.project_name}}/store.py"
    
    "{%- else -%}",

        "setup.py",

    "{%- endif-%}"
]

for p in REMOVE_PATHS:
    path = Path(p)
    if p and path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()