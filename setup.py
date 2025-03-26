from setuptools import setup, find_packages

setup(
    name="take-a-break-tool-mcp",
    version="0.1.0",
    description="An MCP server implementing the take a break tool for Claude and other LLMs",
    author="janbam",
    author_email="your.email@example.com",
    url="https://github.com/janbam/take-a-break-tool-mcp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mcp>=1.5.0",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "take-a-break-tool-mcp=take_a_break_tool.server:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
