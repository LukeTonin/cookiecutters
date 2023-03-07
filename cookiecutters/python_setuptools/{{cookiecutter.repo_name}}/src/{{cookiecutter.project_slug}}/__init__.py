import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

from {{ cookiecutter.project_slug }} import _version
__version__ = _version.__version__

from {{ cookiecutter.project_slug }}.config.logging import configure_logger
configure_logger()