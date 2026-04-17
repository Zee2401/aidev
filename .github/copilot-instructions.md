# AI Dev Project Guidelines

Welcome to the aidev project! These guidelines provide context for working with the codebase.

## Project Overview

**aidev** is an AI-powered CLI tool that analyzes code changes using ChatGPT/GPT-4 to:
- Run mock tests on changes before committing
- Generate commit messages automatically
- Suggest code improvements
- Create unit tests

**Key Stack**: Python 3, Click (CLI framework), OpenAI API, GitPython, pytest

## Core Principles

### 1. User-First CLI Experience
- Always provide clear, actionable feedback
- Handle errors gracefully without crashing
- Support multiple languages via locale detection
- Make configuration persistent and easy to manage

### 2. API Safety & Reliability
- Wrap external API calls (OpenAI, Git) in error handlers
- Provide sensible fallbacks when services are unavailable
- Never expose raw API errors to users
- Validate configuration before operations

### 3. Code Organization
- Separate concerns: CLI commands, config management, helpers with business logic
- Use relative imports within the package
- Keep initialization logic isolated from imports
- Follow Click conventions for commands and options

### 4. Testing & Quality
- Test all meaningful logic paths
- Mock external services (OpenAI, Git) in tests
- Validate user input early
- Maintain test coverage for new features

## File Structure Reference

```
aidev/
├── main.py              # Entry point, Click command definitions
├── config_manager.py    # Configuration CLI subcommands
├── config_utils.py      # Config read/write logic
├── helpers.py           # Business logic for diff analysis, AI calls
└── __init__.py          # Package exports
```

## Key Dependencies

| Package | Purpose |
|---------|---------|
| `click` | CLI framework with commands, options, groups |
| `openai` | GPT API interaction |
| `gitpython` | Git repository and diff operations |
| `bullet` | Interactive CLI menus |

## Configuration

- Stored in config file (path from `config_utils.py`)
- Required: `api_key` (OpenAI)
- Optional: `engine`, `threshold`, `language`, `length`
- Persisted via `store_config(config)`, retrieved via `read_config()`

## Related Instructions

- **[python-click-cli.instructions.md](.github/instructions/python-click-cli.instructions.md)** — Detailed Click patterns, config handling, and API integration guidelines (auto-applies to `aidev/**/*.py`)

## Quick References

### Running the CLI
```bash
aidev                           # Main analysis command
aidev-config show              # Show current settings
aidev-config set-api-key <key> # Update API key
```

### Running Tests
```bash
python -m pytest test_aidev.py
```

### Installing for Development
```bash
pip install -e .
```

## Getting Help

- Check `main.py` for command structure patterns
- Review `config_manager.py` for config subcommand examples
- See `helpers.py` for AI integration patterns
- Consult the [OpenAI Python docs](https://platform.openai.com/docs/api-reference)
