# Copyright (C) 2024 twyleg
import versioneer
from pathlib import Path
from setuptools import find_packages, setup


def read(relative_filepath):
    return open(Path(__file__).parent / relative_filepath).read()


def read_long_description() -> str:
    return read("README.md")


# fmt: off
setup(
    name="playground_agent_worker_test_project",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Torsten Wylegala",
    author_email="mail@twyleg.de",
    description="A minimal Hello World application using simple-python-app",
    license="GPL 3.0",
    keywords="",
    url="https://github.com/twyleg/playground_agent_worker_test_project",
    packages=find_packages(include=["playground_agent_worker_test_project*"]),
    python_requires=">=3.10",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "simple-python-app==0.4.1"
    ],
    entry_points={
        "console_scripts": [
            "playground_agent_worker_test_project = playground_agent_worker_test_project.main:main",
        ]
    },
)
