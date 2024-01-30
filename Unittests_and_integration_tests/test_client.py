#!/usr/bin/env python3
"""tests for the GithubOrg client class"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from requests.exceptions import HTTPError

class TestGithubOrgClient(unittest.TestCase):
    """"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org):
        pass

    def test_public_repos_url(self):
        pass

    def test_public_repos(self):
        pass

    def test_has_license(self):
        pass



class TestIntegrationGithubOrgClient(unittest.TestCase):
    """"""

    @classmethod
    def setUpClass(cls):
        pass
    
    def tearDownClass(cls):
        pass

    def test_public_repos(self):
        pass
