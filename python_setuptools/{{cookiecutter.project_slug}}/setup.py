import setuptools


# Following is a trick to retrieve the version of the package from the package itself.
# https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
version = {}
with open("{{cookiecutter.project_slug}}/version.py") as fp:
    exec(fp.read(), version)

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

test_requirements = ['pytest']

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setuptools.setup(
{%- if cookiecutter.author %}
    author="{{ cookiecutter.author}}",
{%- endif %}
{%- if cookiecutter.author_email %}
    author_email='{{ cookiecutter.author_email }}',
{%- endif %}
    classifiers=[
{%- if cookiecutter.license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.license] }}',
{%- endif %}
        'Natural Language :: English',
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=install_requires,
{%- if cookiecutter.license in license_classifiers %}
    license="{{ cookiecutter.license }}",
{%- endif %}
    long_description=readme,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=setuptools.find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    test_suite='tests',
    tests_require=test_requirements,
{%- if cookiecutter.github_username %}
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
{%- endif %}
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)