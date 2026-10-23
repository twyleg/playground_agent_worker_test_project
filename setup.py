from pathlib import Path

from setuptools import find_packages, setup


setup(
    name="playground_agent_worker_test_project",
    version="0.1.0",
    description="A minimal Hello World application using simple-python-app",
    long_description=Path(__file__).with_name("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["playground_agent_worker_test_project*"]),
    python_requires=">=3.10",
    install_requires=["simple-python-app==0.1.1"],
    entry_points={
        "console_scripts": [
            "playground_agent_worker_test_project = playground_agent_worker_test_project.main:main",
        ],
    },
)
