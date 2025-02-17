# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AgentInvokeResponse"]


class AgentInvokeResponse(BaseModel):
    state: Optional[str] = None
    """state counter of Agent"""

    story: Optional[str] = None
    """OUTPUT response of Agent to INPUT (will force-match LABEL if provided)"""
