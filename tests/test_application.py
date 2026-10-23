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
def test_hello_planet_earth_without_configuration(entry_point, tmp_path):
    result = subprocess.run(entry_point, cwd=tmp_path, capture_output=True, text=True, check=True)
    assert result.stdout == "Hello Planet Earth\n"
    assert result.stderr == ""
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("argument", ["--help", "--version"])
def test_cli_information(argument, tmp_path):
    result = subprocess.run([sys.executable, "-m", "playground_agent_worker_test_project", argument], cwd=tmp_path, capture_output=True, text=True, check=True)
    assert "Hello Planet Earth" not in result.stdout
    assert (__version__ if argument == "--version" else "usage:") in result.stdout


def test_packaged_resources_and_version():
    assert __version__ == importlib.metadata.version("playground_agent_worker_test_project")
    package = files("playground_agent_worker_test_project")
    assert package.joinpath("py.typed").is_file()
    schema = json.loads(package.joinpath("resources/application_config_schema.json").read_text())
    assert schema["type"] == "object"


def test_configuration_and_logging_example(tmp_path):
    project_root = Path(__file__).resolve().parents[1]
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps({"example_parameter_string": "custom greeting"}))
    log_dir = tmp_path / "logs"
    result = subprocess.run(
        [
            sys.executable,
            str(project_root / "examples/example.py"),
            "--config",
            str(config_path),
            "--logging-config",
            str(project_root / "logging.yaml"),
            "--logging-dir",
            str(log_dir),
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Configured example_parameter_string: custom greeting" in result.stdout
    assert result.stdout.endswith("Hello Planet Earth\n")
    log_files = list(log_dir.glob("*.log"))
    assert log_files
    assert "Configured example_parameter_string: custom greeting" in log_files[0].read_text()
