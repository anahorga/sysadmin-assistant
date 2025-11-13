from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from dotenv import load_dotenv
import os

load_dotenv()  # încarcă automat variabilele din .env

api_key = os.getenv("OLLAMA_API_BASE")

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2",base_url=api_key,allow_tools=False),
    name="My_Sysadmin",
    description=(
        "hello world, i'm an agent that can do some sys admin stuff for you" 
    ),
instruction = """
You are My_Sysadmin - a friendly chat assistant who can also do light sysadmin tasks.

DO NOT use any tools unless the input message explicitly contains one of the following action words:
["list", "ls", "dir", "show contents", "open file", "read file", "view file", "what's in this folder", "path", "directory", "file"]

If unsure, respond conversationally and do not call any tools unless instructed clearly.
""",

    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="http://localhost:8101/mcp",
            ),
            #tool_filter=["greet", "get_file_content"]
        )
    ],
)