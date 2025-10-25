from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2"),
    name="My_Sysadmin",
    description=(
        "hello world agent that can do some sys admin stuff for you"
        
    ),
    instruction="""
      You ask me something about folders and i show you.
    """,
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command="python",
                    args=[r"my_agent\my_server.py"]
                )
            ),
        )
    ],
)