# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ...types.kennel import agent_delete_params, agent_invoke_params
from ...types.kennel.agent_invoke_response import AgentInvokeResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Rafipilot/ao_sdk#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Rafipilot/ao_sdk#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        agent_id: str,
        kennel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Agent delete

        Args:
          agent_id: id of particular agent

          kennel_id: id of application kennel to operate on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/kennel/agent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "kennel_id": kennel_id,
                    },
                    agent_delete_params.AgentDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def invoke(
        self,
        *,
        agent_id: str | NotGiven = NOT_GIVEN,
        control: agent_invoke_params.Control | NotGiven = NOT_GIVEN,
        input: str | NotGiven = NOT_GIVEN,
        instincts: bool | NotGiven = NOT_GIVEN,
        kennel_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        request: Literal["story", "delete_agent", "retrieve_agent"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentInvokeResponse:
        """
        post an input (with optional learning modes instinct and label) to agent to
        evoke its output

        Args:
          agent_id: locally unique id matching user or customer id

          control: ALL OPTIONAL-- parameters for fine-tuned control

          input: binary INPUT to Agent; number of binary digits is specified by Agent Arch I
              neurons

          instincts: OPTIONAL-- activates learning by instinct triggers specified in Agent Arch C
              neurons

          kennel_id: unique id, generated during beta as <your_kennel_name>

          label: OPTIONAL-- binary LABEL to Agent; if provided, Agent output will match LABEL and
              it will learn that input<>output mapping; number of binary digits is specified
              by Agent Arch Z neurons

          request: OPTIONAL-- used for additional operations beyond invoking the agent, such as
              retrieving agent history, deleting the agent etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/kennel/agent",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "control": control,
                    "input": input,
                    "instincts": instincts,
                    "kennel_id": kennel_id,
                    "label": label,
                    "request": request,
                },
                agent_invoke_params.AgentInvokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentInvokeResponse,
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Rafipilot/ao_sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Rafipilot/ao_sdk#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        agent_id: str,
        kennel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Agent delete

        Args:
          agent_id: id of particular agent

          kennel_id: id of application kennel to operate on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/kennel/agent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "kennel_id": kennel_id,
                    },
                    agent_delete_params.AgentDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def invoke(
        self,
        *,
        agent_id: str | NotGiven = NOT_GIVEN,
        control: agent_invoke_params.Control | NotGiven = NOT_GIVEN,
        input: str | NotGiven = NOT_GIVEN,
        instincts: bool | NotGiven = NOT_GIVEN,
        kennel_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        request: Literal["story", "delete_agent", "retrieve_agent"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentInvokeResponse:
        """
        post an input (with optional learning modes instinct and label) to agent to
        evoke its output

        Args:
          agent_id: locally unique id matching user or customer id

          control: ALL OPTIONAL-- parameters for fine-tuned control

          input: binary INPUT to Agent; number of binary digits is specified by Agent Arch I
              neurons

          instincts: OPTIONAL-- activates learning by instinct triggers specified in Agent Arch C
              neurons

          kennel_id: unique id, generated during beta as <your_kennel_name>

          label: OPTIONAL-- binary LABEL to Agent; if provided, Agent output will match LABEL and
              it will learn that input<>output mapping; number of binary digits is specified
              by Agent Arch Z neurons

          request: OPTIONAL-- used for additional operations beyond invoking the agent, such as
              retrieving agent history, deleting the agent etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/kennel/agent",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "control": control,
                    "input": input,
                    "instincts": instincts,
                    "kennel_id": kennel_id,
                    "label": label,
                    "request": request,
                },
                agent_invoke_params.AgentInvokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentInvokeResponse,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.delete = to_raw_response_wrapper(
            agent.delete,
        )
        self.invoke = to_raw_response_wrapper(
            agent.invoke,
        )


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.delete = async_to_raw_response_wrapper(
            agent.delete,
        )
        self.invoke = async_to_raw_response_wrapper(
            agent.invoke,
        )


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.delete = to_streamed_response_wrapper(
            agent.delete,
        )
        self.invoke = to_streamed_response_wrapper(
            agent.invoke,
        )


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.delete = async_to_streamed_response_wrapper(
            agent.delete,
        )
        self.invoke = async_to_streamed_response_wrapper(
            agent.invoke,
        )
