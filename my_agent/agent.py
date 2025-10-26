from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2"),
    name="My_Sysadmin",
    description=(
        "hello world, i'm an agent that can do some sys admin stuff for you"
        
    ),
    instruction="""
      You ask me something about folders and i show you.
    """,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="http://127.0.0.1:8100/mcp",
            ),
            #tool_filter=["greet", "get_file_content"]
        )
    ],
)