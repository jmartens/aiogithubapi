"""
Class object for AIOGitHubAPIUsersUser
Documentation: https://docs.github.com/en/rest/reference/users#get-a-user

Generated by generate/generate.py - 2020-08-02 10:35:28.920747
"""
from aiogithubapi.objects.base import AIOGitHubAPIBase


class AIOGitHubAPIUsersUser(AIOGitHubAPIBase):
    @property
    def login(self):
        return self.attributes.get("login", "")

    @property
    def id(self):
        return self.attributes.get("id", None)

    @property
    def node_id(self):
        return self.attributes.get("node_id", "")

    @property
    def avatar_url(self):
        return self.attributes.get("avatar_url", "")

    @property
    def gravatar_id(self):
        return self.attributes.get("gravatar_id", "")

    @property
    def url(self):
        return self.attributes.get("url", "")

    @property
    def html_url(self):
        return self.attributes.get("html_url", "")

    @property
    def followers_url(self):
        return self.attributes.get("followers_url", "")

    @property
    def following_url(self):
        return self.attributes.get("following_url", "")

    @property
    def gists_url(self):
        return self.attributes.get("gists_url", "")

    @property
    def starred_url(self):
        return self.attributes.get("starred_url", "")

    @property
    def subscriptions_url(self):
        return self.attributes.get("subscriptions_url", "")

    @property
    def organizations_url(self):
        return self.attributes.get("organizations_url", "")

    @property
    def repos_url(self):
        return self.attributes.get("repos_url", "")

    @property
    def events_url(self):
        return self.attributes.get("events_url", "")

    @property
    def received_events_url(self):
        return self.attributes.get("received_events_url", "")

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def site_admin(self):
        return self.attributes.get("site_admin", False)

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def company(self):
        return self.attributes.get("company", "")

    @property
    def blog(self):
        return self.attributes.get("blog", "")

    @property
    def location(self):
        return self.attributes.get("location", "")

    @property
    def email(self):
        return self.attributes.get("email", "")

    @property
    def hireable(self):
        return self.attributes.get("hireable", False)

    @property
    def bio(self):
        return self.attributes.get("bio", "")

    @property
    def twitter_username(self):
        return self.attributes.get("twitter_username", "")

    @property
    def public_repos(self):
        return self.attributes.get("public_repos", None)

    @property
    def public_gists(self):
        return self.attributes.get("public_gists", None)

    @property
    def followers(self):
        return self.attributes.get("followers", None)

    @property
    def following(self):
        return self.attributes.get("following", None)

    @property
    def created_at(self):
        return self.attributes.get("created_at", "")

    @property
    def updated_at(self):
        return self.attributes.get("updated_at", "")