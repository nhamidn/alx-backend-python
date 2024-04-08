#!/usr/bin/env python3
""" test_utils module.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
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


"""if __name__ == '__main__':
    unittest.main()"""
