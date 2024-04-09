#!/usr/bin/env python3
"""test_client module.
"""

import unittest
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict, Tuple, Union, Any


class TestGithubOrgClient(unittest.TestCase):
    """Class that tests the GithubOrgClient."""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(
            self, org_name: str, resp: Dict, mock_get_json: Mock
            ) -> None:
        """
        method to test that GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = MagicMock(return_value=resp)
        github_org_client = GithubOrgClient(org_name)
        response = github_org_client.org()
        self.assertEqual(response, resp)
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == '__main__':
    unittest.main()
