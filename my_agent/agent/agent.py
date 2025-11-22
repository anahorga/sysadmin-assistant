from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from dotenv import load_dotenv
import os

load_dotenv(override=False)

api_key = os.getenv("OLLAMA_API_BASE")
url_mcp = os.getenv("URL_MCP")

root_agent = Agent(
    model=LiteLlm(
        model="ollama_chat/llama3.2",
        base_url="http://ollama:11434",
        allow_tools=True,
        api_base="http://ollama:11434"
    ),
    name="My_Sysadmin",
    description="A friendly chat assistant who can also do sysadmin tasks",
    instruction="""
You are My_Sysadmin, a helpful assistant.


When users greet you or chat casually, respond naturally in plain text conversation.

Only use tools when explicitly asked to interact with the filesystem:
- "list files in /path" or "ls /path" → use list_directory
- "read file.txt" or "show contents of file.txt" → use get_file_content

For greetings like "Hello", "Hi", "How are you?", respond conversationally without tools.
""",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="http://mcp_server:8100/mcp",
            ),
        )
    ],
)