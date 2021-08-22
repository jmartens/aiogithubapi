"""
Class object for AIOGitHubAPILoginOauth
Documentation: https://docs.github.com/en/developers/apps/authorizing-oauth-apps#device-flow

Generated by generate/generate.py - 2020-09-08 18:45:20.581868
"""
from ..base import AIOGitHubAPIBase


class AIOGitHubAPILoginOauth(AIOGitHubAPIBase):
    @property
    def access_token(self):
        return self.attributes.get("access_token", "")

    @property
    def token_type(self):
        return self.attributes.get("token_type", "")

    @property
    def scope(self):
        return self.attributes.get("scope", "")