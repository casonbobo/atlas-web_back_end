#!/usr/bin/env python3
"""TestAccessNestedMap class"""
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test meant to throw exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

class TestGetJSON(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """tests utils get_json method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            self.assertEqual(get_json(test_url), test_payload)
            mock_response.json.assert_called_once()

if __name__ == '__main__':
    unittest.main()
