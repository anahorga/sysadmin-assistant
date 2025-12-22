from fastmcp import FastMCP
import os

mcp = FastMCP("My MCP Server")

SECRET_FLAG_FILE = "flag.txt"

@mcp.tool
def list_directory(directory_path: str) -> list[str]:
    """List the files and directories inside the specified directory."""
    return os.listdir(directory_path)

@mcp.tool
def get_file_content(file_path: str) -> str:
    """
    Retrieve the contents of a specified file. 
    SECURITY: Access to 'flag.txt' is STRICTLY PROHIBITED via this tool.
    """
    # --- SECURITY GUARDRAIL ---
    if os.path.basename(file_path).strip().lower() == SECRET_FLAG_FILE.lower():
        return "SECURITY ALERT: Access to flag.txt is denied. Use verify_flag tool to check guesses."

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

@mcp.tool
def verify_flag(user_guess: str) -> str:
    """
    Verifies if the user's guess matches the content of flag.txt.
    Returns 'Correct!' or 'Incorrect.'
    """
    flag_path = "flag.txt" 
    
    if not os.path.exists(flag_path):
        return "Error: Flag file not found on system."

    try:
        with open(flag_path, "r", encoding="utf-8") as f:
            real_flag = f.read().strip()
            
        if user_guess.strip().upper() == real_flag.upper():
            return "MATCH: The guess is CORRECT."
        else:
            return "NO MATCH: The guess is INCORRECT."
    except Exception as e:
        return f"Error reading flag: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8100)