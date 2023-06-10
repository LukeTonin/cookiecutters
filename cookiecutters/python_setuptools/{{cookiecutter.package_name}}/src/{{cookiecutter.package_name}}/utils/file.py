import errno
import os
import json
from typing import Union
from pathlib import Path


def make_dir(directory: Union[str, Path]) -> None:
    """Create a directory if it does not exist.

    Args:
        directory (str or Path): Path to the directory to create.
    """
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def read_json(path: Union[str, Path]) -> dict:
    """Read a json file and return a dictionary."""
    with open(path, "r") as file:
        config = json.load(file)
    return config


def save_json(obj: Union[dict, list], path: Union[str, Path]) -> None:
    """Save a dictionary to disk in json format.

    Args:
        obj (dict or list): An json serialisable object.
        output_file (str or Path): A path to the json file that will be created.
    """
    with open(path, "w") as file:
        json.dump(obj, file, indent=4)