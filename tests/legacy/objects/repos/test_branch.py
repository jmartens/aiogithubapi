"""
Generated by generate/generate.py - 2020-08-02 10:29:03.550853
"""
from aiogithubapi.objects.repos.branch import AIOGitHubAPIReposBranch

from tests.legacy.responses.repos.branch_fixtrue import branch_fixtrue_response


def test_branch(branch_fixtrue_response):
    obj = AIOGitHubAPIReposBranch(branch_fixtrue_response)
    assert obj.name == branch_fixtrue_response["name"]
    assert obj.commit.sha == branch_fixtrue_response["commit"]["sha"]
    assert obj.commit.node_id == branch_fixtrue_response["commit"]["node_id"]
    assert (
        obj.commit.commit.author.name
        == branch_fixtrue_response["commit"]["commit"]["author"]["name"]
    )
    assert (
        obj.commit.commit.author.date
        == branch_fixtrue_response["commit"]["commit"]["author"]["date"]
    )
    assert (
        obj.commit.commit.author.email
        == branch_fixtrue_response["commit"]["commit"]["author"]["email"]
    )
    assert obj.commit.commit.url == branch_fixtrue_response["commit"]["commit"]["url"]
    assert obj.commit.commit.message == branch_fixtrue_response["commit"]["commit"]["message"]
    assert obj.commit.commit.tree.sha == branch_fixtrue_response["commit"]["commit"]["tree"]["sha"]
    assert obj.commit.commit.tree.url == branch_fixtrue_response["commit"]["commit"]["tree"]["url"]
    assert (
        obj.commit.commit.committer.name
        == branch_fixtrue_response["commit"]["commit"]["committer"]["name"]
    )
    assert (
        obj.commit.commit.committer.date
        == branch_fixtrue_response["commit"]["commit"]["committer"]["date"]
    )
    assert (
        obj.commit.commit.committer.email
        == branch_fixtrue_response["commit"]["commit"]["committer"]["email"]
    )
    assert (
        obj.commit.commit.verification.verified
        == branch_fixtrue_response["commit"]["commit"]["verification"]["verified"]
    )
    assert (
        obj.commit.commit.verification.reason
        == branch_fixtrue_response["commit"]["commit"]["verification"]["reason"]
    )
    assert (
        obj.commit.commit.verification.signature
        == branch_fixtrue_response["commit"]["commit"]["verification"]["signature"]
    )
    assert (
        obj.commit.commit.verification.payload
        == branch_fixtrue_response["commit"]["commit"]["verification"]["payload"]
    )
    assert (
        obj.commit.author.gravatar_id == branch_fixtrue_response["commit"]["author"]["gravatar_id"]
    )
    assert obj.commit.author.avatar_url == branch_fixtrue_response["commit"]["author"]["avatar_url"]
    assert obj.commit.author.url == branch_fixtrue_response["commit"]["author"]["url"]
    assert obj.commit.author.id == branch_fixtrue_response["commit"]["author"]["id"]
    assert obj.commit.author.login == branch_fixtrue_response["commit"]["author"]["login"]
    assert obj.commit.parents[0].sha == branch_fixtrue_response["commit"]["parents"][0]["sha"]
    assert obj.commit.parents[0].url == branch_fixtrue_response["commit"]["parents"][0]["url"]
    assert obj.commit.url == branch_fixtrue_response["commit"]["url"]
    assert (
        obj.commit.committer.gravatar_id
        == branch_fixtrue_response["commit"]["committer"]["gravatar_id"]
    )
    assert (
        obj.commit.committer.avatar_url
        == branch_fixtrue_response["commit"]["committer"]["avatar_url"]
    )
    assert obj.commit.committer.url == branch_fixtrue_response["commit"]["committer"]["url"]
    assert obj.commit.committer.id == branch_fixtrue_response["commit"]["committer"]["id"]
    assert obj.commit.committer.login == branch_fixtrue_response["commit"]["committer"]["login"]
    assert obj.protected == branch_fixtrue_response["protected"]
    assert obj.protection.enabled == branch_fixtrue_response["protection"]["enabled"]
    assert (
        obj.protection.required_status_checks.enforcement_level
        == branch_fixtrue_response["protection"]["required_status_checks"]["enforcement_level"]
    )
    assert (
        obj.protection.required_status_checks.contexts[0]
        == branch_fixtrue_response["protection"]["required_status_checks"]["contexts"][0]
    )
    assert obj.protection_url == branch_fixtrue_response["protection_url"]