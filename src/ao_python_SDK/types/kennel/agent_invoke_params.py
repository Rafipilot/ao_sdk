# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AgentInvokeParams", "Control", "ControlNeuron"]


class AgentInvokeParams(TypedDict, total=False):
    agent_id: str
    """locally unique id matching user or customer id"""

    control: Control
    """ALL OPTIONAL-- parameters for fine-tuned control"""

    input: Annotated[str, PropertyInfo(alias="INPUT")]
    """
    binary INPUT to Agent; number of binary digits is specified by Agent Arch I
    neurons
    """

    instincts: Annotated[bool, PropertyInfo(alias="INSTINCTS")]
    """
    OPTIONAL-- activates learning by instinct triggers specified in Agent Arch C
    neurons
    """

    kennel_id: str
    """unique id, generated during beta as <your_kennel_name>"""

    label: Annotated[str, PropertyInfo(alias="LABEL")]
    """
    OPTIONAL-- binary LABEL to Agent; if provided, Agent output will match LABEL and
    it will learn that input<>output mapping; number of binary digits is specified
    by Agent Arch Z neurons
    """

    request: Literal["story", "delete_agent", "retrieve_agent"]
    """
    OPTIONAL-- used for additional operations beyond invoking the agent, such as
    retrieving agent history, deleting the agent etc.
    """


class ControlNeuron(TypedDict, total=False):
    dd: Annotated[bool, PropertyInfo(alias="DD")]
    """
    neuron look-up happens 1st according to discrimination distance (treating the
    lookup table 1-D weights)
    """

    default: Annotated[bool, PropertyInfo(alias="Default")]
    """
    if neither DD or Hamming converge or are disabled, neuron will default to random
    binary response
    """

    hamming: Annotated[bool, PropertyInfo(alias="Hamming")]
    """neuron look-up happens 2nd according to Hamming distance"""


class Control(TypedDict, total=False):
    cn: Annotated[bool, PropertyInfo(alias="CN")]
    """forces a Negative (painful) learning event"""

    cp: Annotated[bool, PropertyInfo(alias="CP")]
    """forces a Positive (pleasurable) learning event"""

    neuron: ControlNeuron
    """neuron-level learning settings"""

    states: int
    """number of times an Agent moves to the next state"""

    us: Annotated[bool, PropertyInfo(alias="US")]
    """
    Agents learn sequenced info by default, so set as True if data stream is
    UnSequenced and needs a reset state between each data input
    """
