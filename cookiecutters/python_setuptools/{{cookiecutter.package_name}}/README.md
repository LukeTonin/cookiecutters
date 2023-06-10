# {{ cookiecutter.project_name }}

## Installation

{{ cookiecutter.project_name }} is a python package and can therefore be installed via pip. However, it is a private
package and therefore is not published to [https://pypi.org](https://pypi.org). You need to set up authentication to FundingCircle's private python package repository for the installation to work. To set up authenatication do the following:
- Login to Artifactory via Okta
- Click on the "Welcome" button in the top right of the screen
- Click on "Edit Profile"
- Scroll down and and generate an API Key. This API key is what will allow you to authenticate to Artifactory.
- We now need to configure pip so that it knows how to use that API key. Create the following file: `~/.pip/pip.conf`.
- In that file add the following (we're configuring pip so that it searches in our private repository in addition to the public one).
```
[global]
extra-index-url = https://YOUR-FC-EMAIL-ADDRESS:YOUR-API-KEY@fundingcircle.jfrog.io/artifactory/api/pypi/pypi/simple
```

Your are now set up to install python packages from our private python package repository using pip.

To install, follow the instructions in one of the following methods.

### From FC's private python package repository

This method is the easiest if you don't need to be working on the code and just need to use the package.

The `{{ cookiecutter.project_name }}` package is built and published to Funding Circle's private repository
manager: [https://fundingcircle.jfrog.io/ui/repos/tree/General/pypi](https://fundingcircle.jfrog.io/ui/repos/tree/General/pypi)

To install, make sure you have configured pip to authenticate to our private python package repository, and run:
```
pip install --pre {{ cookiecutter.package_name }}
```

Note: The `--pre` flag installs dev versions of the package if available (i.e package versions postfixed with .devN) when the true release has not yet been made. If you do not want dev releases of the package, remove the `--pre` flag.

### Install from source

This method is useful if you want to have the packages installed while developing them and make use of pip's "editable" installs (i.e the ability to change code dynamically without reinstalling.)

First, clone the repository for this project (this assumes you have your [SSH credentials](https://confluence.fundingcircle.com/display/RandA/How+to+Guide+-+Git+and+Github) set up):
```
git clone git@github.com:FundingCircle/<repository-name>.git
```
Followed by (replace `/path/to/repository` with the actual path to repository downloaded from github):
```
pip install --editable /path/to/repository
```

Note: This method does not require authentication to artifactory.

## Releasing

The package follows [semantic versioning](https://semver.org). To create a new versioned release of `{{ cookiecutter.project_name }}`:

1. Update the version in the [version file]({{  cookiecutter.package_name }}/_version.py) e.g. for a minor bump update the second number. 

2. Once the change has been merged, switch to the `main` locally and create a new git tag. (Make sure the tag is
   annotated) e.g.

```
git tag -a v1.1.3 -m "release notes here"
```

3. Push the tag to GitHub

```sh
git push origin --tags
```

4. The git push will trigger a build in drone that will publish the versioned artifact to https://fundingcircle.jfrog.io


## Testing

To test this repository, call:
```
make test
```

This action is defined in the Makefile

## Continuous integration: Drone

### Drone pipeline
The drone pipeline for this repository is defined in the [drone.yml](.drone.yml) file.

By default, the pipeline performs the following actions:
- Install and runs the package's tests using `make test`.
- Check the linting of the file using [black](https://github.com/psf/black).
- Create a snapshot (i.e dev) release in artifactory (see [installation](#installation)) every time the main branch is updated.
- Create a full release in artifactory (see [installation](#installation)) every time a tag is added to the main branch (see [releasing](#releasing) for more details on the release process).

### How to activate this repository in Drone

The [drone.yml](.drone.yml) file describes the continuous integration pipeline. However, by default drone will not execute the pipeline. For that, the repository needs to be activated from the drone UI. You must go to https://drone.fc-ops.com/FundingCircle/<repository-name> (replace repository name with the correct name) and click `Activate Respository`. That will enable drone to run the pipeline.

