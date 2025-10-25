from fastmcp import FastMCP
import os
mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello ffddff, {name}!"

@mcp.tool
def list_directory(dir_path: str) -> list[str]:
    return os.listdir(dir_path)


if __name__ == "__main__":
    mcp.run()