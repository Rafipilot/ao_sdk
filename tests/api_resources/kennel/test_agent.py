# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ao_python_SDK import AoPythonSDK, AsyncAoPythonSDK
from ao_python_SDK.types.kennel import AgentInvokeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AoPythonSDK) -> None:
        agent = client.kennel.agent.delete(
            agent_id="agent_id",
            kennel_id="kennel_id",
        )
        assert agent is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AoPythonSDK) -> None:
        response = client.kennel.agent.with_raw_response.delete(
            agent_id="agent_id",
            kennel_id="kennel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AoPythonSDK) -> None:
        with client.kennel.agent.with_streaming_response.delete(
            agent_id="agent_id",
            kennel_id="kennel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_invoke(self, client: AoPythonSDK) -> None:
        agent = client.kennel.agent.invoke()
        assert_matches_type(AgentInvokeResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_invoke_with_all_params(self, client: AoPythonSDK) -> None:
        agent = client.kennel.agent.invoke(
            agent_id="1st of Clams",
            control={
                "cn": False,
                "cp": False,
                "neuron": {
                    "dd": True,
                    "default": True,
                    "hamming": True,
                },
                "states": 1,
                "us": True,
            },
            input="000",
            instincts=True,
            kennel_id="TEST-Clamologist",
            label="0",
            request="story",
        )
        assert_matches_type(AgentInvokeResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_invoke(self, client: AoPythonSDK) -> None:
        response = client.kennel.agent.with_raw_response.invoke()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentInvokeResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_invoke(self, client: AoPythonSDK) -> None:
        with client.kennel.agent.with_streaming_response.invoke() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentInvokeResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAoPythonSDK) -> None:
        agent = await async_client.kennel.agent.delete(
            agent_id="agent_id",
            kennel_id="kennel_id",
        )
        assert agent is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAoPythonSDK) -> None:
        response = await async_client.kennel.agent.with_raw_response.delete(
            agent_id="agent_id",
            kennel_id="kennel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAoPythonSDK) -> None:
        async with async_client.kennel.agent.with_streaming_response.delete(
            agent_id="agent_id",
            kennel_id="kennel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_invoke(self, async_client: AsyncAoPythonSDK) -> None:
        agent = await async_client.kennel.agent.invoke()
        assert_matches_type(AgentInvokeResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_invoke_with_all_params(self, async_client: AsyncAoPythonSDK) -> None:
        agent = await async_client.kennel.agent.invoke(
            agent_id="1st of Clams",
            control={
                "cn": False,
                "cp": False,
                "neuron": {
                    "dd": True,
                    "default": True,
                    "hamming": True,
                },
                "states": 1,
                "us": True,
            },
            input="000",
            instincts=True,
            kennel_id="TEST-Clamologist",
            label="0",
            request="story",
        )
        assert_matches_type(AgentInvokeResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_invoke(self, async_client: AsyncAoPythonSDK) -> None:
        response = await async_client.kennel.agent.with_raw_response.invoke()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentInvokeResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_invoke(self, async_client: AsyncAoPythonSDK) -> None:
        async with async_client.kennel.agent.with_streaming_response.invoke() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentInvokeResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
