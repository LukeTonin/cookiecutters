#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_dir(path: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, path))


def remove_file(path: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, path))


def main():
    if "{{ cookiecutter.add_notebooks_directory }}" == "no":
        remove_dir("src/{{ cookiecutter.project_slug }}/notebooks")

    if "{{ cookiecutter.add_changelog }}" == "no":
        remove_file("CHANGELOG.md")


if __name__ == "__main__":
    main()
