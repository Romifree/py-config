#! /usr/bin/python3.9
# Copyright (C) Romi https://github.com/Romi-go/

import config
import unittest

class TestConfig(unittest.TestCase):
    def test_get(self):
        assert config.get("keyVault.name") == "kv-name", "shall be 'kv-name'"
        self.assertEqual(config.get("keyVault.uri"), "https://kv-name.vault.azure.net/")
        assert config.get("test.name") == "testname", "shall be 'testname'"
        assert config.get("test.secLevel") == {"third": "thirdtest"}, "shall be '{\"third\": \"thirdtest\"}'"
        assert config.get("test.secLevel.third") == "thirdtest", "shall be 'thirdtest'"

    def test_get_default(self):
        assert config.get("non.exist", "default") == "default", "shall be 'default'"
        assert config.get("test.name", "not default") == "testname", "shall be 'testname'"

    def test_key_err(self):
        with self.assertRaises(KeyError):
            config.get("non.exist")

if __name__ == "__main__":
    unittest.main()