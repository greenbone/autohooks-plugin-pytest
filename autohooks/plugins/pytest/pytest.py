# Copyright (C) 2021-2022 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Provides precommit function for pytest autohook plugin."""

import subprocess
import sys

from autohooks.api import error, ok, out

DEFAULT_ARGUMENTS = ["-ra", "--color=yes", "-q"]


def _check_pytest_installed():
    try:
        import pytest  # pylint: disable=import-outside-toplevel, disable=unused-import
    except ImportError as e:
        raise Exception(
            "Could not find pytest. Please add pytest to your python "
            "environment"
        ) from e


def _get_pytest_config(config):
    return config.get("tool").get("autohooks").get("plugins").get("pytest")


def _ensure_iterable(value):
    if isinstance(value, str):
        return [value]

    return value


def _get_pytest_arguments(config):
    if not config:
        return DEFAULT_ARGUMENTS

    pytest_config = _get_pytest_config(config)
    arguments = _ensure_iterable(
        pytest_config.get_value("arguments", DEFAULT_ARGUMENTS)
    )

    return arguments


def precommit(config=None, **kwargs):  # pylint: disable=unused-argument
    """Precommit hook for running tests with pytest."""
    _check_pytest_installed()

    arguments = _get_pytest_arguments(config)

    ret = 0
    cmd = ["pytest"]
    cmd.extend(arguments)
    try:
        subprocess.run(cmd, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        ret = e.returncode
        error("Pytest reported failing tests.")
        lint_errors = e.stdout.decode(
            encoding=sys.getdefaultencoding(), errors="replace"
        ).split("\n")
        for line in lint_errors:
            out(line)
    if ret == 0:
        ok("Testing was successful.")

    return ret
