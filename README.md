# aadi-mcp-executable-demo
This project has code and instructions to deploy a github mcp server using python sdk. 
This uses FastMCP framework. This is a simple demo and all code is present in server.py file.

## Steps before executing the code
To ensure you have the right libraries and tools follow below steps.
1. Install Python v12 or above. Use one of your favorite AI tools (e.g., google or MS Copilot) to get specific instructions
2. ```console
   pip install FastMCP mcp[cli]
   ```
4. Install Claude Desktop, follow this link for downloading appropriate version https://claude.ai/download
5. Install uv, the pyhton package manager, instructions are available at https://github.com/astral-sh/uv

Now take a deep breath, you installed lot of new stuff, they all need to work together. 
if you are having multiple python versions, a common pattern on macOS, run below command to make 
uv use the desired version of python.
``` uv python pin --global 3.12.7```

# Steps to install MCP server and test with Claude Desktop
1. ```cd mcp-server-demo```
2. Run below command to add MCP server to Claude Desktop app
```uv run mcp install server.py```
3. Find the Claude Desktop app on your computer and start the app
4. Using the chat input box and submit this prompt "get a happy greeting for Rajesh"
5. You may be prompted to click on "Allow Once" or "Allow always" to let Claude use local mcp server. Click the button of your choice and you will see Claude AI using the local MCP server to fetch a greeting for you.

Congratulations, your experiment is complete now and successful.


