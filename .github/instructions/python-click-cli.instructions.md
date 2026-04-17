---
description: "Use when writing Python code for aidev CLI module. Covers Click command patterns, configuration handling, API interactions, error handling, and project conventions."
applyTo: "aidev/**/*.py"
---

# Python Click CLI Development Guidelines

This project uses Click framework for CLI development with OpenAI API integration. Follow these patterns for consistency and maintainability.

## Click Command Patterns

### Basic Command Structure
```python
import click

@click.command()
@click.option('--name', default='value', type=str, help='Description')
def command_name(name):
    """Brief description of what this command does."""
    pass
```

### Command Groups (Multi-commands)
```python
@click.group()
def manage_config():
    """Manage configuration."""
    pass

@manage_config.command()
def show():
    """Display current settings."""
    pass
```

### Option Best Practices
- Use `default` for sensible defaults from config or user preferences
- Specify `type` explicitly (str, int, float, etc.)
- Provide clear `help` text for all options
- Store user inputs back to config using `store_config()`

## Configuration Management

- Use `read_config()` to retrieve stored settings
- Use `store_config(config)` to persist changes
- Check for missing required keys before using them:
  ```python
  config = read_config()
  if "api_key" not in config:
      # prompt user or handle gracefully
  ```
- Store validated user inputs back to config for CLI continuity

## API Integration (OpenAI)

- Initialize client once at module level: `client = OpenAI(api_key=config.get('api_key'))`
- Wrap API calls in try/except blocks:
  ```python
  try:
      result = client.models.list()
  except:
      return default_fallback_value
  ```
- Use config values for engine, temperature, max_tokens parameters

## Error Handling

- Use try/except for external API calls and file operations
- Return sensible defaults on errors (don't crash silently)
- Print user-friendly messages on failure
- Example: `except: return ['chatgpt-4o-latest']` provides fallback

## Import Organization

1. Standard library imports first
2. Third-party imports (click, openai, bullet, etc.)
3. Relative imports from local modules using dot notation:
   ```python
   from .config_utils import read_config, store_config
   from aidev.helpers import get_git_diff, get_ai_run_result
   ```

## Code Style

- Include docstrings for all commands (one-liner format):
  ```python
  def manage_config():
      """Manage AI Tester configuration."""
  ```
- Use meaningful variable names aligned with Click option names
- Keep functions focused on single responsibility
- Prefer explicit boolean checks: `if confirm == 'y':` rather than string truthiness

## Locale and Language Support

- Use `locale` module for detecting default language
- Support configurable output languages
- Store language preference in config

## Patterns to Avoid

- Don't create config at import time without fallback defaults
- Don't hardcode API keys or credentials
- Don't skip error handling for external service calls
- Don't mix CLI logic with business logic—use helper functions

