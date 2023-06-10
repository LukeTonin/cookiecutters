import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

from {{ cookiecutter.package_name }} import _version
__version__ = _version.__version__

from {{ cookiecutter.package_name }}.config.logging import configure_logger
configure_logger()