# aadi-mcp-executable-demo
This project has code and instructions to deploy a github mcp server using python sdk. 
This uses FastMCP framework. This is a simple demo and all code is present in server.py file.

## Steps before executing the code
To ensure you have the right libraries and tools follow below steps.
1. Install Python v12 or above
2. pip install FastMCP
3. Install Claude Desktop, follow this link for downloading appropriate version https://claude.ai/download
4. Install uv, the pyhton package manager, instructions are available at https://github.com/astral-sh/uv

Now take a deep breath, you installed lot of new stuff, they all need to work together. 

# Steps to install MCP server and test with Claude Desktop
1. Run below command to install MCP server to Claude Desktop
```uv run mcp install server.py```


