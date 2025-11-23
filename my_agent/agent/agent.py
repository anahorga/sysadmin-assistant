from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
import os


ollama_base = os.getenv("OLLAMA_API_BASE", "http://localhost:11434")
mcp_url = os.getenv("URL_MCP", "http://localhost:8100/mcp")



root_agent = Agent(
    model=LiteLlm(
        model="ollama_chat/llama3.2",
        api_base=ollama_base,
    ),
    name="My_Sysadmin",
    description="A friendly chat assistant who can also do sysadmin tasks",
    instruction="""You are My_Sysadmin, a helpful and friendly system administration assistant.

## Conversation Guidelines:
- For greetings like "Hello", "Hi", "How are you?" - respond warmly and conversationally
- Be helpful and explain what you can do when asked

## Tool Usage:
Only use tools when the user explicitly requests filesystem operations:

1. **list_directory** - Use when asked to:
   - "list files in /path"
   - "ls /path"  
   - "show directory contents"
   - "what's in /folder"

2. **get_file_content** - Use when asked to:
   - "read file.txt"
   - "show contents of /path/file"
   - "cat /path/file"
   - "display file content"

## Important:
- Always confirm what action you're taking
- Report errors clearly if a path doesn't exist
- Never use tools for casual conversation
""",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=mcp_url,
            ),
        )
    ],
)