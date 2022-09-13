#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove(path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, path))


def main():
    if "{{ cookiecutter.add_notebooks_directory }}" == "no":
        remove("notebooks")


if __name__ == "__main__":
    main()
