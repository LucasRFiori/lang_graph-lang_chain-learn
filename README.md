# LangChain & LangGraph Studies — Modern Python Environment 2025

Hands-on study notes and examples for LangChain and LangGraph, built on top of a modern Python project setup with VS Code.

**Want to understand the environment setup behind this project?**

I walk through it step by step in the videos below:

- Part 1: [Modern Python Environment - Traditional](https://youtu.be/QTw5eB6GTM8)
- Part 2: [Modern Python Environment - Pyenv and Pyenv-win](https://youtu.be/X38M7C_A2XU)
- Part 3: [Modern Python Environment - UV Astral](https://youtu.be/HuAc85cLRx0)
- Part 4: [Starting new projects with the Modern Python Environment](https://youtu.be/TcfFXur4YKg)

---

## About

This repository contains practical examples and experiments for learning LangChain and LangGraph, including:

- LLM invocation with local models via Ollama
- Chat history and message management with LangChain
- StateGraph construction and execution with LangGraph
- Conditional edges and branching in LangGraph graphs
- Custom state reducers

The project also serves as a reference for a modern Python development environment using:

- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/) for dependency and virtual environment management
- [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- [Pyright](https://github.com/microsoft/pyright) for static type checking
- VS Code with recommended extensions

---

## Examples

| Example | Description |
|---------|-------------|
| `ex001` | Basic LLM invocation with Ollama and LangChain |
| `ex002` | Multi-turn chat with system prompt and message history |
| `ex003/ex003_1` | LangGraph StateGraph with sequential nodes and a reducer |
| `ex003/ex003_2` | LangGraph with conditional edges and branching logic |

---

## Initial Requirements

Make sure you have the following installed:

1. [Python](https://www.python.org/downloads/)
2. [Git](https://git-scm.com/downloads)
3. [VS Code](https://code.visualstudio.com/)
4. [Ollama](https://ollama.com/) with `llama3.2` pulled — required to run the LangChain examples

If you're on Windows, allow PowerShell to run scripts:

1. Open Terminal or PowerShell **as administrator**
2. Run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Getting Started

```sh
# Install uv (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install uv (Windows PowerShell)
iwr https://astral.sh/uv/install.ps1 -useb | iex
```

```sh
# Install Python, create venv, and install all dependencies
uv sync
```

```sh
# Run an example
uv run src/examples/ex001/main.py
```

---

## Managing Dependencies with uv

```sh
# Add a package
uv add langchain langgraph

# Remove a package
uv remove requests

# Install from requirements.txt
uv add -r requirements.txt

# Run without activating the venv
uv run src/examples/ex002/main.py
```

---

## Git Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --global init.defaultBranch main
git config --global core.autocrlf input
git config --global core.eol lf
```

---

## `.env` and `.env-example`

Copy `.env-example` to `.env` to set up your environment variables. The project uses `python-dotenv` to load them automatically.

```bash
uv sync  # installs python-dotenv along with other dependencies
```

If the dotenv check in the main entry point prints `Not working`, you likely forgot to copy the `.env-example` file.
