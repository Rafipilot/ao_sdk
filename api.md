# Kennel

Types:

```python
from ao_python_SDK.types import KennelCreateResponse, KennelListResponse
```

Methods:

- <code title="post /kennel">client.kennel.<a href="./src/ao_python_SDK/resources/kennel/kennel.py">create</a>(\*\*<a href="src/ao_python_SDK/types/kennel_create_params.py">params</a>) -> <a href="./src/ao_python_SDK/types/kennel_create_response.py">KennelCreateResponse</a></code>
- <code title="get /kennel">client.kennel.<a href="./src/ao_python_SDK/resources/kennel/kennel.py">list</a>(\*\*<a href="src/ao_python_SDK/types/kennel_list_params.py">params</a>) -> <a href="./src/ao_python_SDK/types/kennel_list_response.py">KennelListResponse</a></code>
- <code title="delete /kennel">client.kennel.<a href="./src/ao_python_SDK/resources/kennel/kennel.py">delete</a>(\*\*<a href="src/ao_python_SDK/types/kennel_delete_params.py">params</a>) -> None</code>

## Agent

Types:

```python
from ao_python_SDK.types.kennel import AgentInvokeResponse
```

Methods:

- <code title="delete /kennel/agent">client.kennel.agent.<a href="./src/ao_python_SDK/resources/kennel/agent.py">delete</a>(\*\*<a href="src/ao_python_SDK/types/kennel/agent_delete_params.py">params</a>) -> None</code>
- <code title="post /kennel/agent">client.kennel.agent.<a href="./src/ao_python_SDK/resources/kennel/agent.py">invoke</a>(\*\*<a href="src/ao_python_SDK/types/kennel/agent_invoke_params.py">params</a>) -> <a href="./src/ao_python_SDK/types/kennel/agent_invoke_response.py">AgentInvokeResponse</a></code>
