#!/usr/bin/env python3
"""tests for the GithubOrg client class"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from requests.exceptions import HTTPError
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing the GitHubOrg func in client"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org):
        """test the org"""
        pass

    def test_public_repos_url(self):
        """test public repos"""
        pass

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test public repos"""
        pass

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """test has license"""
        self.assertEqual(GithubOrgClient.has_license(repo, key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class for testing integration in GitHubOrg"""

    @classmethod
    def setUpClass(cls):
        """Set Up class"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect \
            = [cls.org_payload, cls.repos_payload]

    @classmethod
    def tearDownClass(cls):
        """Tear Down class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public repos"""
        pass
