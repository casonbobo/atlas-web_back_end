#!/usr/bin/env python3
"""TestAccessNestedMap class"""
import unittest
from utils import access_nested_map, get_json, memoize
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


class TestGetJson(unittest.TestCase):
    """The class for the get Json test"""

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


class TestMemoize(unittest.TestCase):
    """Tests the memoize decorator"""

    def test_memoize(self):
        """make the test class and test it"""
        class TestClass:
            """Test class struct"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """Test method """
                return self.a_method()

        # """test memoize and test the test"""
        # with patch.object(TestClass, 'a_method', return_value=42) as mock:
        #     test_class = TestClass()
        #     self.assertEqual(test_class.a_property(), mock.return_value)
        #     self.assertEqual(test_class.a_property(), mock.return_value)
        #     mock.assert_called_once()
