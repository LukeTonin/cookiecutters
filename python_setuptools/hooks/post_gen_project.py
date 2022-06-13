#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove(path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, path))


def main():
    if "{{ cookiecutter.add_data_directory }}" == "no":
        remove("data")
    if "{{ cookiecutter.add_notebooks_directory }}" == "no":
        remove("notebooks")
    if "{{ cookiecutter.add_conf_directory }}" == "no":
        remove("conf")
    if "{{ cookiecutter.add_logd_directory }}" == "no":
        remove("logs")


if __name__ == "__main__":
    main()
