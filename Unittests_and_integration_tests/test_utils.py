#!/usr/bin/env python3
"""TestAccessNestedMap class"""
import unittest
from utils import access_nested_map
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """The start of the unit test class for utils"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected_output):
        """test access nested map for utils"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

if __name__ == '__main__':
    unittest.main()
