#!/usr/bin/env python3
"""tests for the GithubOrg client class"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from requests.exceptions import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing the GitHubOrg func in client"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org):
        pass

    def test_public_repos_url(self):
        pass

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        pass

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected_output):
        pass


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class for testing integration in GitHubOrg"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_public_repos(self):
        pass
