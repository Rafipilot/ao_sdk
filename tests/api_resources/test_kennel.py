# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ao_python_SDK import AoPythonSDK, AsyncAoPythonSDK
from ao_python_SDK.types import (
    KennelListResponse,
    KennelCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKennel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AoPythonSDK) -> None:
        kennel = client.kennel.create()
        assert_matches_type(KennelCreateResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AoPythonSDK) -> None:
        kennel = client.kennel.create(
            arch_url="https://gist.githubusercontent.com/mi3law/8012fc6e6adceab35d03fd3e5da8db34/raw/58df93994f5341541809547a1d963e8ed0570a07/0_basic_clam.py",
            description="the simplest, atomic arch reference design, our hello, world",
            kennel_name="TEST-Clamologist",
            permissions="free and open as the sea!",
        )
        assert_matches_type(KennelCreateResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AoPythonSDK) -> None:
        response = client.kennel.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kennel = response.parse()
        assert_matches_type(KennelCreateResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AoPythonSDK) -> None:
        with client.kennel.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kennel = response.parse()
            assert_matches_type(KennelCreateResponse, kennel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AoPythonSDK) -> None:
        kennel = client.kennel.list()
        assert_matches_type(KennelListResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: AoPythonSDK) -> None:
        kennel = client.kennel.list(
            kennel_id="kennel_id",
        )
        assert_matches_type(KennelListResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AoPythonSDK) -> None:
        response = client.kennel.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kennel = response.parse()
        assert_matches_type(KennelListResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AoPythonSDK) -> None:
        with client.kennel.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kennel = response.parse()
            assert_matches_type(KennelListResponse, kennel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AoPythonSDK) -> None:
        kennel = client.kennel.delete(
            kennel_id="kennel_id",
        )
        assert kennel is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AoPythonSDK) -> None:
        response = client.kennel.with_raw_response.delete(
            kennel_id="kennel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kennel = response.parse()
        assert kennel is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AoPythonSDK) -> None:
        with client.kennel.with_streaming_response.delete(
            kennel_id="kennel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kennel = response.parse()
            assert kennel is None

        assert cast(Any, response.is_closed) is True


class TestAsyncKennel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAoPythonSDK) -> None:
        kennel = await async_client.kennel.create()
        assert_matches_type(KennelCreateResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAoPythonSDK) -> None:
        kennel = await async_client.kennel.create(
            arch_url="https://gist.githubusercontent.com/mi3law/8012fc6e6adceab35d03fd3e5da8db34/raw/58df93994f5341541809547a1d963e8ed0570a07/0_basic_clam.py",
            description="the simplest, atomic arch reference design, our hello, world",
            kennel_name="TEST-Clamologist",
            permissions="free and open as the sea!",
        )
        assert_matches_type(KennelCreateResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAoPythonSDK) -> None:
        response = await async_client.kennel.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kennel = await response.parse()
        assert_matches_type(KennelCreateResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAoPythonSDK) -> None:
        async with async_client.kennel.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kennel = await response.parse()
            assert_matches_type(KennelCreateResponse, kennel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAoPythonSDK) -> None:
        kennel = await async_client.kennel.list()
        assert_matches_type(KennelListResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAoPythonSDK) -> None:
        kennel = await async_client.kennel.list(
            kennel_id="kennel_id",
        )
        assert_matches_type(KennelListResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAoPythonSDK) -> None:
        response = await async_client.kennel.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kennel = await response.parse()
        assert_matches_type(KennelListResponse, kennel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAoPythonSDK) -> None:
        async with async_client.kennel.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kennel = await response.parse()
            assert_matches_type(KennelListResponse, kennel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAoPythonSDK) -> None:
        kennel = await async_client.kennel.delete(
            kennel_id="kennel_id",
        )
        assert kennel is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAoPythonSDK) -> None:
        response = await async_client.kennel.with_raw_response.delete(
            kennel_id="kennel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kennel = await response.parse()
        assert kennel is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAoPythonSDK) -> None:
        async with async_client.kennel.with_streaming_response.delete(
            kennel_id="kennel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kennel = await response.parse()
            assert kennel is None

        assert cast(Any, response.is_closed) is True
