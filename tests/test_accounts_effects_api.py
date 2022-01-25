# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401


def test_get_accounts_effect(client: TestClient) -> None:
    """Test case for get_accounts_effect

    Get accounts effect
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/effects/{effectName}".format(
            accountKey="account_key_example", effectName="effect_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_accounts_effects(client: TestClient) -> None:
    """Test case for get_accounts_effects

    Get accounts effect list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/effects/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
