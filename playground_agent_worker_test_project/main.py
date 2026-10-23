import argparse

from simple_python_app.generic_application import GenericApplication

from playground_agent_worker_test_project import __version__


class Application(GenericApplication):
    def __init__(self, example_enabled: bool = False):
        super().__init__(
            application_name="playground_agent_worker_test_project",
            version=__version__,
            application_config_init_enabled=example_enabled,
            logging_init_custom_logging_enabled=example_enabled,
            logging_init_default_logging_enabled=False,
        )

    def run(self, args: argparse.Namespace) -> None:
        if self.application_config is not None:
            # GenericApplication loads the JSON selected by --config or its search paths.
            example_value = self.application_config["example_parameter_string"]
            self.logm.info("Configured example_parameter_string: %s", example_value)
        print("Hello, Planet!")


def main() -> None:
    Application().start()
