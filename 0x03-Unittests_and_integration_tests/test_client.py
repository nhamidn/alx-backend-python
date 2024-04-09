#!/usr/bin/env python3
""" test_utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict, Tuple, Union, Any


class TestGithubOrgClient(unittest.TestCase):
    """Class that tests the GithubOrgClient."""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(
            self, org_name: str, mock_get_json: Mock
            ) -> None:
        """
        method to test that GithubOrgClient.org returns the correct value.
        """
        mock_response = {"login": org_name, "id": 12345}
        mock_get_json.return_value = mock_response
        github_org_client = GithubOrgClient(org_name)
        response = github_org_client.org
        self.assertEqual(response, mock_response)
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == '__main__':
    unittest.main()
