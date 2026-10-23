"""Demonstrate GenericApplication configuration loading and logging."""

from playground_agent_worker_test_project.main import Application

if __name__ == "__main__":
    raise SystemExit(Application(example_enabled=True).start())
