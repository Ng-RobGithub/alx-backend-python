#!/usr/bin/env python3
"""
test_client.py

Integration tests for the GithubOrgClient
"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient
    """

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test the public_repos method to ensure it returns the expected result
        """
        # Fixtures
        org_name = "test_org"
        repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Mocking the get_json return value
        mock_get_json.return_value = repos_payload

        # Creating an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Calling the public_repos method and checking the result
        repos = client.public_repos()
        self.assertEqual(repos, ["repo1", "repo2", "repo3"])

        # Ensure the mock was called with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}/repos")

    @patch('client.get_json')
    def test_public_repos_with_license(self, mock_get_json):
        """
        Test the public_repos method with a license filter
        """
        # Fixtures
        org_name = "test_org"
        repos_payload = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}}
        ]

        ''' Mocking the get_json return value '''
        mock_get_json.return_value = repos_payload

        # Creating an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        ''' Calling the public_repos method with a license
        filter and checking the result '''
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, ["repo1", "repo3"])

        # Ensure the mock was called with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}/repos")


if __name__ == "__main__":
    unittest.main()
