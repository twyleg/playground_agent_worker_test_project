# playground_agent_worker_test_project

A minimal Hello Planet Earth application using `GenericApplication` from
`simple-python-app` (0.4.1), based on
[template_project_python](https://github.com/twyleg/template_project_python).

## Install and run

With Python 3.10 or newer:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m playground_agent_worker_test_project
# Or: playground_agent_worker_test_project
```

Both entry points print `Hello Planet Earth` and exit. `--help` and `--version`
are also available. The redundant `hello.py` wrapper has been removed.
Configuration loading and logging initialization are disabled for the default command.

To demonstrate both, run from the repository root after installing the project:

```sh
python examples/example.py --config playground_agent_worker_test_project_config.json --logging-config logging.yaml
```

The example enables GenericApplication's configuration and logging initialization.
`Application.run()` reads `self.application_config["example_parameter_string"]`
and logs it with `self.logm.info(...)`, then prints `Hello Planet Earth`.
The supplied logging configuration writes to the console and a log file.
`--logging-dir` selects the log directory; `--verbose` enables debug logging.

`resources/__init__.py` makes resources a regular Python package discovered by
`find_packages()`. The manifest and `include_package_data=True` include the schema
and data in distributions. The marker is retained for explicit package discovery;
it does not by itself include data files.

## Development

```sh
python -m pip install -r requirements.txt
python -m tox
python -m tox -e docs
python -m tox -e pyinstaller
```

Tox runs pytest, formatting, type checks, and a package/CLI smoke test by default.
The CI matrix runs these checks on Linux and Windows with Python 3.10–3.14.
Development dependency lower bounds follow the template and allow newer releases
for newer Python interpreters.

The initialized template includes Sphinx documentation and source assets, examples,
resource directories, packaging manifests, a GPL-3.0 license, and PyInstaller
support. Template initialization files are omitted as specified by its
`template_config.yaml`. `setup.py` and `setup.cfg` use Versioneer to derive the
package and runtime version from Git tags and history; builds embed that version
for use outside a Git checkout. No release version is hardcoded.

The release workflow builds and publishes to PyPI after tests pass when a release
is published. It uses an existing `PYPI_API_TOKEN` repository secret; no credentials
or repository settings are configured by this change.
