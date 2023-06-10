# Cookiecutter: python package

A cookiecutter is a directory template used to create directories with a predefined format.
For instance, this repository contains cookie cutters to build python packages.  

## Cookiecutter Installation
Cookiecutter is an open source application. It can be installed using the following instructions:
https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter

## Features
The directory created from this cookiecutter has the following features:

- Python package that is pip installable.
- Some modules and files that support configuration of the package/application.
- A module to support logging configuration.
- Contains a test directory to support the implementation and execution of tests using pytest.
- Contains a [drone.yml](%7B%7Bcookiecutter.repo_name%7D%7D/.drone.yml) file that configures a continuous integration pipeline that does the following:
  - Executes tests
  - Uploads the package to FundingCircle's private python package repository (e.g [this package](https://fundingcircle.jfrog.io/ui/packages/pypi:%2F%2Fprobability-of-default-model?name=probability&type=packages)).  
- Contains a [Makefile](%7B%7Bcookiecutter.repo_name%7D%7D/Makefile) with various useful commands (e.g test, build, upload)

## Set up
1. Make sure you have cookiecutter installed (e.g by calling `cookiecutter --help` from the command line). If not, follow the [Cookiecutter Installation](#cookiecutter-installation) instructions from above.
2. Clone this repository to a location of your choice (named `/path/to/cookiecutter-python-package` in the rest of the documentation)
3. To create a package from this cookiecutter, run the following command and answer the questions when prompted, this will allow you to create your package with an acceptable name etc. Most fields can be left as default if you do not know what to change. Note: The package directory will be created in the working directory of the terminal in which you execute the command.
```
cookiecutter /path/to/cookiecutter-python-package
```

This cookiecutter will create a directory that looks something like this:

<img src="./docs/images/python_package.png" height="300" />

In the following documentation, we will assume that you have created a package called `My Package` (slug: `my_package`, repo name: `my-package`).

4. (Optional but recommended) Store your package in github. If you're not sure how to create a github repository, follow the "Create a repository" section from [this article](https://docs.github.com/en/get-started/quickstart/create-a-repo).

5. (Optional) If needed, you can enable continuous integration using drone. To do this, follow the instructions in the (`Continuous integration: Drone`) section of the [README.md](%7B%7Bcookiecutter.repo_name%7D%7D/README.md) in the package directory you created in step 2.
Enabling continuous integration using drone is recommended if you intend to share you package with your team members. With the continuous integration pipeline, you will get automatic testing and deployment of the package to our artifactory repository (see your packages README.md file for more details). For an example of what the continuous integration pipeline looks like, check [this example](https://drone.fc-ops.com/FundingCircle/probability-of-default-model).

## Usage

After following the [Set up](#set-up) instructions, you now have a python package that is fully functional (i.e can be installed via pip, deployed to drone etc...). However, your package doesn't do anything yet!

1. To begin, start by installing you python package within a new conda environment.

Note: If you're not familiar with conda or how to do this first install [miniconda](https://docs.conda.io/en/latest/miniconda.html) and learn how to create and manage [conda environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). This is outside the scope of these instructions, if you need help, speak to a team member.

```
pip install --editable /path/to/my-package
```

2. Then, become familiar with using your python package in jupyter notebooks. To do this open the `notebooks/example.ipynb` from your package. For instance, see what happens when you modify the main function from `/src/my_package/main.py`.

