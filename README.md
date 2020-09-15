# Cookiecutter Platform

A "cookiecutter" for generating software platform boilerplate.

## Introduction

[Cookiecutter](https://github.com/audreyr/cookiecutter) is a cross-platform software tool that generates [boilerplate](https://en.wikipedia.org/wiki/Boilerplate_code) for [software projects](https://en.wikipedia.org/wiki/Software_project_management) from special templates.  These templates, called *cookiecutters*, can be used to define:

* How a project's directories and files are named and organized;
* The content of each of a project's starter files.

They can also facilitate, both manually and automatically, the run-time customization of the generated names and content.

The cookiecutter presented here, Cookiecutter Platform, defines boilerplate templates for creating platform-focused software projects, where "platform" here loosely means a programming language (Python, Swift, etc.), file format specification (HTML, JSON, etc), or software tool (Cookiecutter, Docker, etc.).  The generated boilerplate is a basic directory tree and a starter set of software files that can then be used to begin building software targeting a particular software platform.

## Getting Started

### System Requirements

Cookiecutter Platform supports the 3 major operating systems:

* Linux
* macOS
* Windows

To use Cookiecutter Platform, the following software must first be installed on your system:

* [Python](https://www.python.org/downloads/) 3.6, 3.7, 3.8, or PyPy3
* [Cookiecutter](https://github.com/audreyr/cookiecutter) Python package 1.7.2 or higher

### Installation

For info on installing any of the prerequisite software, go to the [official](https://cookiecutter.readthedocs.io/en/latest/installation.html) installation document.

### Usage

Cookiecutter Platform can generate boilerplate by running shell or Python scripts.  Furthermore, its cookiecutter can be sourced remotely via a direct download or locally via a cached copy from a prior download.

#### Shell

To generate boilerplate from a shell's command-line interface (CLI), run the command `cookiecutter`.  The argument following `cookiecutter` specifies both the cookiecutter and whether its source is remote or local.

* Remote source:

    ```sh
    # The following syntax options are semantically equivalent.

    # Option 1: URL
    $ cookiecutter https://github.com/djrlj694/cookiecutter-platform.git

    # Option 2: 'gh' prefix
    $ cookiecutter gh:djrlj694/cookiecutter-platform

    # Option 3: 'git+ssh' prefix
    $ cookiecutter git+ssh://git@github.com/djrlj694/cookiecutter-platform.git
    ```

* Local source:

    ```sh
    $ cookiecutter cookiecutter-platform/
    ```

### Python

The Python library `cookiecutter.main` provides an application programming interface (API) for calling Cookiecutter functions to generate boilerplate.

* Remote source:

    ```python
    from cookiecutter.main import cookiecutter

    cookiecutter('https://github.com/djrlj694/cookiecutter-platform.git')
    ```

* Local source:

    ```python
    from cookiecutter.main import cookiecutter

    cookiecutter('cookiecutter-platform/')
    ```

## Builds and Testing

TODO: *Describe and show how to build artifacts and run tests.*

## Documentation

Documentation for this project is pending but eventually will be found [here](https://djrlj694.github.io/cookiecutter-platform/).

## Known Issues

Currently, there are no known issues.  If you discover any, please kindly submit a [pull request](CONTRIBUTING.md).

## Contributing

Code and codeless (documentation, donations, etc.) contributions are welcome. To contribute yours, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Cookiecutter Platform is released under the [MIT License](LICENSE).

## References

References for this project are pending but eventually will be found [here](REFERENCES.md).
