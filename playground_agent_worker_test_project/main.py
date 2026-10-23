import argparse

from simple_python_app.generic_application import GenericApplication

from playground_agent_worker_test_project import __version__


class Application(GenericApplication):
    def __init__(self):
        super().__init__(
            application_name="playground_agent_worker_test_project",
            version=__version__,
            application_config_init_enabled=False,
            logging_init_custom_logging_enabled=False,
            logging_init_default_logging_enabled=False,
        )

    def run(self, args: argparse.Namespace) -> None:
        print("Hello, World!")


def main() -> None:
    Application().start()
