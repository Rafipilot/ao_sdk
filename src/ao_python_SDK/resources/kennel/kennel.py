# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .agent import (
    AgentResource,
    AsyncAgentResource,
    AgentResourceWithRawResponse,
    AsyncAgentResourceWithRawResponse,
    AgentResourceWithStreamingResponse,
    AsyncAgentResourceWithStreamingResponse,
)
from ...types import kennel_list_params, kennel_create_params, kennel_delete_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.kennel_list_response import KennelListResponse
from ...types.kennel_create_response import KennelCreateResponse

__all__ = ["KennelResource", "AsyncKennelResource"]


class KennelResource(SyncAPIResource):
    @cached_property
    def agent(self) -> AgentResource:
        return AgentResource(self._client)

    @cached_property
    def with_raw_response(self) -> KennelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ao_python_SDK-python#accessing-raw-response-data-eg-headers
        """
        return KennelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KennelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ao_python_SDK-python#with_streaming_response
        """
        return KennelResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        arch_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        kennel_name: str | NotGiven = NOT_GIVEN,
        permissions: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KennelCreateResponse:
        """
        Upload an Arch to spawn Agents

        Args:
          arch_url: link to a raw URL arch file hosted on gists.github.com

          kennel_name: name your collection of Agents, possible after their/your application

          permissions: coming soon

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/kennel",
            body=maybe_transform(
                {
                    "arch_url": arch_url,
                    "description": description,
                    "kennel_name": kennel_name,
                    "permissions": permissions,
                },
                kennel_create_params.KennelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KennelCreateResponse,
        )

    def list(
        self,
        *,
        kennel_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KennelListResponse:
        """
        Get a list of your kennels

        Args:
          kennel_id: to view particular kennel by id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/kennel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"kennel_id": kennel_id}, kennel_list_params.KennelListParams),
            ),
            cast_to=KennelListResponse,
        )

    def delete(
        self,
        *,
        kennel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete kennel

        Args:
          kennel_id: id of kennel to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/kennel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"kennel_id": kennel_id}, kennel_delete_params.KennelDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncKennelResource(AsyncAPIResource):
    @cached_property
    def agent(self) -> AsyncAgentResource:
        return AsyncAgentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKennelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ao_python_SDK-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKennelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKennelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ao_python_SDK-python#with_streaming_response
        """
        return AsyncKennelResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        arch_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        kennel_name: str | NotGiven = NOT_GIVEN,
        permissions: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KennelCreateResponse:
        """
        Upload an Arch to spawn Agents

        Args:
          arch_url: link to a raw URL arch file hosted on gists.github.com

          kennel_name: name your collection of Agents, possible after their/your application

          permissions: coming soon

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/kennel",
            body=await async_maybe_transform(
                {
                    "arch_url": arch_url,
                    "description": description,
                    "kennel_name": kennel_name,
                    "permissions": permissions,
                },
                kennel_create_params.KennelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KennelCreateResponse,
        )

    async def list(
        self,
        *,
        kennel_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KennelListResponse:
        """
        Get a list of your kennels

        Args:
          kennel_id: to view particular kennel by id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/kennel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"kennel_id": kennel_id}, kennel_list_params.KennelListParams),
            ),
            cast_to=KennelListResponse,
        )

    async def delete(
        self,
        *,
        kennel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete kennel

        Args:
          kennel_id: id of kennel to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/kennel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"kennel_id": kennel_id}, kennel_delete_params.KennelDeleteParams),
            ),
            cast_to=NoneType,
        )


class KennelResourceWithRawResponse:
    def __init__(self, kennel: KennelResource) -> None:
        self._kennel = kennel

        self.create = to_raw_response_wrapper(
            kennel.create,
        )
        self.list = to_raw_response_wrapper(
            kennel.list,
        )
        self.delete = to_raw_response_wrapper(
            kennel.delete,
        )

    @cached_property
    def agent(self) -> AgentResourceWithRawResponse:
        return AgentResourceWithRawResponse(self._kennel.agent)


class AsyncKennelResourceWithRawResponse:
    def __init__(self, kennel: AsyncKennelResource) -> None:
        self._kennel = kennel

        self.create = async_to_raw_response_wrapper(
            kennel.create,
        )
        self.list = async_to_raw_response_wrapper(
            kennel.list,
        )
        self.delete = async_to_raw_response_wrapper(
            kennel.delete,
        )

    @cached_property
    def agent(self) -> AsyncAgentResourceWithRawResponse:
        return AsyncAgentResourceWithRawResponse(self._kennel.agent)


class KennelResourceWithStreamingResponse:
    def __init__(self, kennel: KennelResource) -> None:
        self._kennel = kennel

        self.create = to_streamed_response_wrapper(
            kennel.create,
        )
        self.list = to_streamed_response_wrapper(
            kennel.list,
        )
        self.delete = to_streamed_response_wrapper(
            kennel.delete,
        )

    @cached_property
    def agent(self) -> AgentResourceWithStreamingResponse:
        return AgentResourceWithStreamingResponse(self._kennel.agent)


class AsyncKennelResourceWithStreamingResponse:
    def __init__(self, kennel: AsyncKennelResource) -> None:
        self._kennel = kennel

        self.create = async_to_streamed_response_wrapper(
            kennel.create,
        )
        self.list = async_to_streamed_response_wrapper(
            kennel.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            kennel.delete,
        )

    @cached_property
    def agent(self) -> AsyncAgentResourceWithStreamingResponse:
        return AsyncAgentResourceWithStreamingResponse(self._kennel.agent)
