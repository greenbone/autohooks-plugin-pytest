![Greenbone Logo](https://www.greenbone.net/wp-content/uploads/gb_new-logo_horizontal_rgb_small.png)

# autohooks-plugin-pytest

[![PyPI release](https://img.shields.io/pypi/v/autohooks-plugin-pytest.svg)](https://pypi.org/project/autohooks-plugin-pytest/)

An [autohooks](https://github.com/greenbone/autohooks) plugin for [pytest](https://github.com/pytest-dev/pytest/).

## Installation

### Install using pip

You can install the latest stable release of autohooks-plugin-pytest from the
Python Package Index using [pip](https://pip.pypa.io/):

    python3 -m pip install autohooks-plugin-pytest

### Install using poetry

It is highly encouraged to use [poetry](https://python-poetry.org) for
maintaining your project's dependencies. Normally autohooks-plugin-pytest is
installed as a development dependency.

    poetry install

## Usage

To activate the pytest autohooks plugin please add the following setting to your
*pyproject.toml* file.

```toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.pytest"]
```

By default, autohooks plugin pytest checks all files with a *.py* ending. If
only files in a sub-directory or files with different endings should be
tested, just add the following setting:

```toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.pytest"]

[tool.autohooks.plugins.pytest]
include = ['foo/*.py', '*.foo']
```

By default, autohooks plugin pytest executes pytest without any arguments and
pytest settings are loaded from the *.pytestrc* file in the root directory of
git repository. To change specific settings or to define a different pytest rc
file the following plugin configuration can be used:

```toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.pytest"]

[tool.autohooks.plugins.pytest]
arguments = ["--rcfile=/path/to/pytestrc", "-s", "n"]
```

## Maintainer

This project is maintained by [Greenbone Networks GmbH](https://www.greenbone.net/).

## Contributing

Your contributions are highly appreciated. Please
[create a pull request](https://github.com/greenbone/autohooks-plugin-pytest/pulls)
on GitHub. Bigger changes need to be discussed with the development team via the
[issues section at GitHub](https://github.com/greenbone/autohooks-plugin-pytest/issues)
first.

## License

Copyright (C) 2021-2022 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
