# SPDX-FileCopyrightText: 2022-2025 Greenbone AG
#
# SPDX-License-Identifier: GPL-3.0-or-later

from autohooks.plugins.pytest import precommit


def test_plugin_import():
    """Test that the plugin can be imported successfully."""
    assert callable(precommit)
