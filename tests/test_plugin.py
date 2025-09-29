# SPDX-FileCopyrightText: 2022-2025 Greenbone AG
#
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest

from autohooks.plugins.pytest import precommit


class TestPlugin(unittest.TestCase):
    """Test the autohooks pytest plugin."""

    def test_plugin_import(self):
        """Test that the plugin can be imported successfully."""
        self.assertTrue(callable(precommit))


if __name__ == "__main__":
    unittest.main()
