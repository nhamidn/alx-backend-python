#!/usr/bin/env python3
"""test_client module.
"""

import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict, Tuple, Union, Any
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Class that tests the GithubOrgClient."""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, expected_response: Dict,
                 mocked_function: MagicMock) -> None:
        """Function that tests GithubOrgClient.org."""
        mocked_function.return_value = MagicMock(
            return_value=expected_response)
        goclient = GithubOrgClient(org)
        self.assertEqual(goclient.org(), expected_response)
        mocked_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Function that tests GithubOrgClient.public_repos."""
        mock_repos_payload = [
            {"name": "pyccel", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = mock_repos_payload
        mock_repos_url = 'https://api.github.com/orgs/pyccel/repos'
        expected_repos = ['pyccel']
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = mock_repos_url
            client = GithubOrgClient("pyccel")
            repos = client.public_repos()
            self.assertEqual(repos, expected_repos)
            mock_get_json.assert_called_once_with(mock_repos_url)
            mock_public_repos_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
