# Copyright (C) 2024 twyleg
import sys
from importlib.metadata import version

from . import _version

# Frozen executables have no Git checkout; PyInstaller bundles package metadata.
__version__ = version(__package__) if getattr(sys, "frozen", False) else _version.get_versions()["version"]
