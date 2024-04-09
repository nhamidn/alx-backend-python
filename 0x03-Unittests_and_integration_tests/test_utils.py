#!/usr/bin/env python3
""" test_utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """Class that tests the access_nested_map method in utils."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, n_map: Dict, path: Tuple[str], result: Union[Dict, int]
            ) -> None:
        """
        method to test that access_nested_map returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(n_map, path), result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self, n_map: Dict, path: Tuple[str], exception: Union[KeyError]
            ) -> None:
        """
        method to test that access_nested_map returns the correct exception.
        """
        with self.assertRaises(exception):
            access_nested_map(n_map, path)


class TestGetJson(unittest.TestCase):
    """Tests that tests the get_json emthod in utils."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self, test_url: str, test_payload: Dict,
            ) -> None:
        """Method to Test that get_json returns the correct json."""
        attrs = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attrs)) as mocked_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mocked_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests that tests the memoize decorator in utils."""
    def test_memoize(self):
        """Method to Test that memoize behave as expected."""
        class TestClass:
            """Test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as m_method:
            test_object = TestClass()
            first_call_result = test_object.a_property
            second_call_result = test_object.a_property
            self.assertEqual(first_call_result, 42)
            self.assertEqual(second_call_result, 42)
            m_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
