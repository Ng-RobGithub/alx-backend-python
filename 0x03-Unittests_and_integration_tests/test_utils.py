#!/usr/bin/env python3
"""
test_utils.py

Unit tests for utils functions
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the correct result
        for a given nested_map and path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises a KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to test the get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns the expected result for a given URL
        """
        ''' Create a mock response object with a json method '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        ''' Call get_json and check the result '''
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        ''' Ensure the mocked get method was called exactly
        once with the test_url '''
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class to test the memoize decorator
    """

    def test_memoize(self):
        """
        Test that a_property returns the correct result and that
        a_method is only called once.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) \
             as mock_method:
            test_instance = TestClass()
            ''' Access the property twice '''
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            ''' Check that the result is correct '''
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            ''' Ensure that a_method was called only once '''
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
