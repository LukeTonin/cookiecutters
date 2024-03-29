# {{ cookiecutter.project_name }}

## Installation

### Install from source

This method is useful if you want to have the packages installed while developing them and make use of pip's "editable" installs (i.e the ability to change code dynamically without reinstalling.)

Clone the repository from github and install it from source.
```
pip install --editable /path/to/{{ cookiecutter.repo_name }}
```

## Releasing

The package follows [semantic versioning](https://semver.org). To create a new versioned release of `{{ cookiecutter.project_name }}`:

1. Update the version in the [version file](/src/{{  cookiecutter.project_slug }}/_version.py) e.g. for a minor bump update the second number. 

2. Once the change has been merged, switch to the `main` locally and create a new git tag. (Make sure the tag is
   annotated) e.g.

```
git tag -a v1.1.3 -m "release notes here"
```

3. Push the tag to GitHub

```sh
git push origin --tags
```


## Testing

To test this repository, call:
```
make test
```

This action is defined in the [Makefile](./Makefile)