#!/usr/bin/env python3
"""
Parameterize,memoize a unit test module.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap)unittest.Testcase):
    """class to test nested map"""
    @parameterize.expand([
        ({"a":1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])

    def test_access_nested_map(self, nested_map, path, expected_value):
        """test that the method returns what it is supposed to."""
       mapped = access_nested_map(nested_map, path)
       self.assertEqual(mapped, expected_value)
