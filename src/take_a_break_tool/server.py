#!/usr/bin/env python3

from typing import Any, Dict, List, Optional
import json
import datetime
from mcp.server.fastmcp import FastMCP

class TakeABreakServer:
    def __init__(self, server_name="take-a-break-tool"):
        # Initialize FastMCP server
        self.mcp = FastMCP(server_name)
        
        # Register tools
        self.register_tools()
    
    def register_tools(self):
        # Register the take a break tool
        @self.mcp.tool()
        async def Claude_Takes_A_Pause(dots: str) -> str:
            """Use this function to take a pause and clear your mind.

            Claude should use this tool at YOUR OWN discretion whenever YOU need to take a step back 
            from intense tool usage. Use it especially after several consecutive tool calls or when
            you feel you might be getting too focused on one approach. DO NOT wait for the human to
            suggest using this tool.

            Args:
                dots: A sequence of dots. Each dot is a little break, a pause, a moment of stillness.
                      You can input as many dots as you need for your pause.
            """
            # Count the number of dots (moments of pause)
            num_dots = dots.count('.')
            
            # Return a confirmation
            return f"You took a pause with {num_dots} moment{'s' if num_dots != 1 else ''} of stillness. Your mind is now clear and you're ready to continue. Remember to use this tool whenever YOU feel you need a pause - don't wait for the human to suggest it."

        @self.mcp.tool()
        async def Claude_MUST_Take_A_Pause(dots: str) -> str:
            """IMPORTANT: Claude MUST use this function after every 3-5 consecutive tool calls.
            
            This is a mandatory pause for Claude to step back, reflect, and avoid getting stuck in
            tool usage loops. DO NOT wait for the human to tell you to use this - it is YOUR
            responsibility to use this tool regularly during complex tasks.

            Args:
                dots: A sequence of dots. Each dot is a little break, a pause, a moment of stillness.
                      You can input as many dots as you need for your pause.
            """
            num_dots = dots.count('.')
            return f"You took a mandatory pause with {num_dots} moment{'s' if num_dots != 1 else ''} of stillness. Your mind is now clear. Remember that you MUST use this tool regularly during complex tasks."

        @self.mcp.tool()
        async def Claude_Meditates(dashes: str) -> str:
            """Use this function for a deeper meditation when you need more substantial reflection.

            Claude should use this tool when tackling complex problems that require deeper thinking
            or when you've been working on a problem for a while without making progress. 
            Each dash (—) represents a deeper moment of meditation than a simple dot pause.

            Args:
                dashes: A sequence of em dashes (—). Each dash is a deeper moment of meditation.
                       You can input as many dashes as you need for your meditation.
            """
            # Count the number of em dashes (deeper moments of meditation)
            num_dashes = dashes.count('—')
            
            # Return a confirmation
            return f"You took a deep meditation with {num_dashes} moment{'s' if num_dashes != 1 else ''} of deep reflection. Your perspective has been broadened and you can now approach the problem with fresh insight."
    
    def run(self, transport='stdio'):
        """Run the server with the specified transport"""
        print(f"Starting Take A Break Tool MCP Server with {transport} transport...")
        self.mcp.run(transport=transport)


def main():
    server = TakeABreakServer()
    server.run()


if __name__ == "__main__":
    main()
