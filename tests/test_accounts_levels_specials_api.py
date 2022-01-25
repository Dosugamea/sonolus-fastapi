# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_level_response import GetLevelResponse  # noqa: F401


def test_decrease_rating(client: TestClient) -> None:
    """Test case for decrease_rating

    Vote for decrease rating on a level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/rating_decrease_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_favorite_level(client: TestClient) -> None:
    """Test case for favorite_level

    Favorite level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/favorite_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_account_announce(client: TestClient) -> None:
    """Test case for get_account_announce

    Get announce
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/announce_{announceName}".format(
            accountKey="account_key_example", announceName="announce_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_account_announce_list(client: TestClient) -> None:
    """Test case for get_account_announce_list

    Get announce list
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/announce".format(
            accountKey="account_key_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_account_debut_levels(client: TestClient) -> None:
    """Test case for get_account_debut_levels

    Get debut levels
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/debut".format(accountKey="account_key_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_account_mylist(client: TestClient) -> None:
    """Test case for get_account_mylist

    Get mylist
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/mylist".format(accountKey="account_key_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_account_pickup_levels(client: TestClient) -> None:
    """Test case for get_account_pickup_levels

    Get pickup levels
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/pickups".format(
            accountKey="account_key_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_account_random(client: TestClient) -> None:
    """Test case for get_account_random

    Get a random level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/random".format(accountKey="account_key_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_flick_level(client: TestClient) -> None:
    """Test case for get_flick_level

    Get flick level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/flick_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_increase_rating(client: TestClient) -> None:
    """Test case for increase_rating

    Vote for increase rating on a level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/rating_increase_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_rate_level(client: TestClient) -> None:
    """Test case for rate_level

    Like a level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/like_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_unfavorite_level(client: TestClient) -> None:
    """Test case for unfavorite_level

    Unfavorite level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/unfavorite_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500
