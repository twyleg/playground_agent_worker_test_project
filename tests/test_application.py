import importlib.metadata
import json
import subprocess
import sys
import sysconfig
from pathlib import Path
from importlib.resources import files

import pytest

from playground_agent_worker_test_project import __version__


@pytest.mark.parametrize(
    "entry_point",
    [
        [sys.executable, "-m", "playground_agent_worker_test_project"],
        [
            str(
                Path(sysconfig.get_path("scripts"))
                / ("playground_agent_worker_test_project.exe" if sys.platform == "win32" else "playground_agent_worker_test_project")
            )
        ],
    ],
)
def test_hello_world_without_configuration(entry_point, tmp_path):
    result = subprocess.run(entry_point, cwd=tmp_path, capture_output=True, text=True, check=True)
    assert result.stdout == "Hello, World!\n"
    assert result.stderr == ""
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("argument", ["--help", "--version"])
def test_cli_information(argument, tmp_path):
    result = subprocess.run([sys.executable, "-m", "playground_agent_worker_test_project", argument], cwd=tmp_path, capture_output=True, text=True, check=True)
    assert "Hello, World!" not in result.stdout
    assert (__version__ if argument == "--version" else "usage:") in result.stdout


def test_packaged_resources_and_version():
    assert __version__ == importlib.metadata.version("playground_agent_worker_test_project")
    package = files("playground_agent_worker_test_project")
    assert package.joinpath("py.typed").is_file()
    schema = json.loads(package.joinpath("resources/application_config_schema.json").read_text())
    assert schema["type"] == "object"
