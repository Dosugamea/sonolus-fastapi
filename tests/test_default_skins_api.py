# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_skin_list_response import GetSkinListResponse  # noqa: F401
from src.models.get_skin_response import GetSkinResponse  # noqa: F401
from src.models.skin import Skin  # noqa: F401


def test_add_skin(client: TestClient) -> None:
    """Test case for add_skin

    Add a skin
    """
    skin = {
        "updated_time": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
        "subtitle": "subtitle",
        "name": "name",
        "created_time": 0,
        "description": "description",
        "title": "title",
        "version": 1,
        "user_id": "userId",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/skins",
        headers=headers,
        json=skin,
    )

    assert response.status_code != 500


def test_delete_skin(client: TestClient) -> None:
    """Test case for delete_skin

    Delete a skin
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_skin(client: TestClient) -> None:
    """Test case for edit_skin

    Edit a skin
    """
    skin = {
        "updated_time": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
        "subtitle": "subtitle",
        "name": "name",
        "created_time": 0,
        "description": "description",
        "title": "title",
        "version": 1,
        "user_id": "userId",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PATCH",
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
        json=skin,
    )

    assert response.status_code != 500


def test_get_skin(client: TestClient) -> None:
    """Test case for get_skin

    Get a skin
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_skin_list(client: TestClient) -> None:
    """Test case for get_skin_list

    Get skin list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/skins/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
