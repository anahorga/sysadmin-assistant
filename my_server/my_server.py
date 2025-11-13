from fastmcp import FastMCP
import os

mcp = FastMCP("My MCP Server")


@mcp.tool
def list_directory(directory_path: str) -> list[str]:
    """
    List the files and directories inside the specified directory.

    Args:
        directory_path (str): Absolute path to the directory to list.

    Returns:
        list[str]: A list of names (files and folders) contained in the directory.

    Raises:
        FileNotFoundError: If the directory does not exist.
        PermissionError: If access to the directory is denied.
    """
    return os.listdir(directory_path)


@mcp.tool
def get_file_content(file_path: str) -> str:
    """
    Retrieve the contents of a specified file as a string.

    Args:
        file_path (str): Absolute path to the file to read.

    Returns:
        str: The contents of the file as text.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If access to the file is denied.
        UnicodeDecodeError: If the file contents cannot be decoded as UTF-8.
    """
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8100)