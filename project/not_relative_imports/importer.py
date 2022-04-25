import imp
import sys
from pathlib import Path
import importlib.util


def import_module_from_home(*path):
    home = Path(__file__).parents[2]
    path = Path(home, *path)
    spec = importlib.util.spec_from_file_location(path.name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module