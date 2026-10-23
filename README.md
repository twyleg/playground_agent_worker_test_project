# playground_agent_worker_test_project

A minimal Hello World application using `GenericApplication` from
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

Both entry points print `Hello, World!` and exit. `--help` and `--version`
are also available. The redundant `hello.py` wrapper has been removed.
Configuration loading and logging initialization are disabled for this minimal
application. The template's sample configuration, JSON schema, logging settings,
and package resources remain available as starting points for future development.

## Development

```sh
python -m pip install -r requirements.txt
python -m tox
python -m tox -e docs
python -m tox -e pyinstaller
```

Tox runs pytest, formatting, type checks, and a package/CLI smoke test by default.
The CI matrix runs these checks on Linux and Windows with Python 3.10–3.12.
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
