# MCP Take A Break Tool Server

A simple MCP server that implements a "take a break" tool for Claude and other LLMs. 

## Purpose

This tool helps Claude take a moment to pause during tool call sequences to prevent "tool frenzies" - where the LLM becomes hyper-focused on continuously calling tools without stopping to reflect.

## How It Works

The tool accepts a single argument: a string of dots where each dot represents a moment of stillness or pause. The more dots provided, the longer the conceptual "break" for Claude.

Example usage:

```
take_a_break_tool(".............")  # Take 13 moments of stillness
```

## Installation

```bash
pip install -e .
```

## Usage

The server can be run directly:

```bash
take-a-break-tool-mcp
```

Or imported in Python:

```python
from take_a_break_tool.server import TakeABreakServer

server = TakeABreakServer()
server.run()
```
