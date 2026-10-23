# playground_agent_worker_test_project

A minimal Hello World application using `GenericApplication` from
`simple-python-app`, following the package and application structure of
[template_project_python](https://github.com/twyleg/template_project_python/tree/1a7855da288716919a68dbdc1e3c5d603368e9ca).
Package metadata, dependencies, and the console entry point are defined in
`setup.py`, following the template.

Install with Python 3.10 or newer:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Run using any of the entry points:

```sh
python3 hello.py
python3 -m playground_agent_worker_test_project
playground_agent_worker_test_project
```

Each prints `Hello, World!` and exits. No configuration file is required;
application configuration loading and logging initialization are disabled.
The framework also provides `--help` and `--version`.
