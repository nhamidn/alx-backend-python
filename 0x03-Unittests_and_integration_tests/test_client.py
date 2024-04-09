#!/usr/bin/env python3
"""test_client module.
"""

import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
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
        expected_url = "https://api.github.com/orgs/{}".format(org_name)
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """Method that test _public_repos_url returns the expected URL."""
        mock_org_pl = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }
        expected_result = "https://api.github.com/orgs/test-org/repos"

        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = mock_org_pl
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
