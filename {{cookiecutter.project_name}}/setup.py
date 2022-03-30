"""Install the package."""

from setuptools import setup, find_packages
import pkg_resources
import re

if __name__ == "__main__":

    with open("README.md") as readme_file:
        readme = readme_file.read()

    with open("requirements.txt") as f:
        my_requirements = [str(requirement) for requirement in pkg_resources.parse_requirements(f)]

    with open("{{cookiecutter.project_name}}/__init__.py") as version_file:
        version = re.findall('__version__ = "(.*)"', version_file.read())[0]

    setup(
        author="{{cookiecutter.author}}",
        author_email="{{cookiecutter.author_email}}",
        description="{{cookiecutter.description}}",
        include_package_data=True,
        install_requires=my_requirements,
        # extras_require={},
        license="mit",
        long_description_content_type="text/markdown",
        long_description=readme,
        name="{{cookiecutter.project_name}}",
        packages=find_packages(exclude=("tests**",)),
        platforms="any",
        project_urls={
            "Documentation": "https://{{cookiecutter.project_name}}.readthedocs.io/",
            "Homepage": "https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}",
        },
        python_requires=">={{cookiecutter.minimal_python_version}}",
        url="https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}",
        version=version,
        classifiers=[
            "Development Status :: 3 - Alpha",
            # "Development Status :: 4 - Beta
            # "Development Status :: 5 - Production/Stable",
            "Environment :: Other Environment",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Application Frameworks",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
