# Info Script

Cli to print scripts available in utility-scripts module.

## Configuration Format - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Python dataclass named `CliScriptsInfo` with:
    - `CliName`: 4-character lowercase string
    - `Description`: string (max 300 chars)
    - Load from JSON array (see format below)
    - Validate input
    - Display as object list
    - **JSON Schema:**
    ```json
    [
      {
        "CliName": "abcd",
        "Description": "Max 300 characters"
      }
    ]
    ```
- Development Process:
  1. Write unit tests first
  2. Implement dataclass to pass tests
- Code Style:
  - No comments (self-documenting code only)
