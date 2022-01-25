# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class SearchTextOption(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SearchTextOption - a model defined in OpenAPI

        query: The query of this SearchTextOption.
        name: The name of this SearchTextOption.
        type: The type of this SearchTextOption.
        placeholder: The placeholder of this SearchTextOption.
    """

    query: str
    name: str
    type: str
    placeholder: str

SearchTextOption.update_forward_refs()
