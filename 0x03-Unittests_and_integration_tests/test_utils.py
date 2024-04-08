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


"""if __name__ == '__main__':
    unittest.main()"""
