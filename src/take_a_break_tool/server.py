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

            Args:
                dots: A sequence of dots. Each dot is a little break, a pause, a moment of stillness.
                      You can input as many dots as you need for your pause.
            """
            # Count the number of dots (moments of pause)
            num_dots = dots.count('.')
            
            # Return a confirmation
            return f"You took a pause with {num_dots} moment{'s' if num_dots != 1 else ''} of stillness. Your mind is now clear and you're ready to continue."
    
    def run(self, transport='stdio'):
        """Run the server with the specified transport"""
        print(f"Starting Take A Break Tool MCP Server with {transport} transport...")
        self.mcp.run(transport=transport)


def main():
    server = TakeABreakServer()
    server.run()


if __name__ == "__main__":
    main()
