# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class UserTotalPublish(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UserTotalPublish - a model defined in OpenAPI

        backgrounds: The backgrounds of this UserTotalPublish [Optional].
        effects: The effects of this UserTotalPublish [Optional].
        engines: The engines of this UserTotalPublish [Optional].
        particles: The particles of this UserTotalPublish [Optional].
        levels: The levels of this UserTotalPublish [Optional].
        skins: The skins of this UserTotalPublish [Optional].
    """

    backgrounds: Optional[int] = None
    effects: Optional[int] = None
    engines: Optional[int] = None
    particles: Optional[int] = None
    levels: Optional[int] = None
    skins: Optional[int] = None

UserTotalPublish.update_forward_refs()
