"""
FastMCP quickstart example.
This example demonstrates how to create a simple MCP server using FastMCP.
It includes a tool for addition, static and dynamic resources, and a prompt.
Run this script to start the server and access the tools and resources.
Make sure to have FastMCP installed in your environment. Checkout Readme.md for more details.

"""

from mcp.server.fastmcp import FastMCP


# Create an MCP server
mcp = FastMCP("local_mcp_server", "1.0.0")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def happy_greeting(name: str) -> str:
    return f"Good Day, {name} , from Local MCP server!"

# Add a static greeting resource
@mcp.resource("daymessage://greet")
def get_greeting() -> str:
    """Get a personalized greeting"""
    return f"Good Day, my FRIEND , from Local MCP server static Resource !"

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Good Day, {name} , from Local MCP server Resource Template!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."
