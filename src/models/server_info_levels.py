# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.level import Level
from src.models.search import Search


class ServerInfoLevels(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServerInfoLevels - a model defined in OpenAPI

        items: The items of this ServerInfoLevels.
        search: The search of this ServerInfoLevels.
    """

    items: List[Level]
    search: Search


ServerInfoLevels.update_forward_refs()
