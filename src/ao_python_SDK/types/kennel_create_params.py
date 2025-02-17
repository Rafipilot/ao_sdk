# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KennelCreateParams"]


class KennelCreateParams(TypedDict, total=False):
    arch_url: Annotated[str, PropertyInfo(alias="arch_URL")]
    """link to a raw URL arch file hosted on gists.github.com"""

    description: str

    kennel_name: str
    """name your collection of Agents, possible after their/your application"""

    permissions: str
    """coming soon"""
