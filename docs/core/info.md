# Info Script

## Configuration Format - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Load from JSON array (see format below)
  - Validate input
  - Display as object list
- Development Process:
  1. Write unit tests first
  2. Implement dataclass to pass tests
- Code Style:
  - No comments (self-documenting code only)
- Python dataclass named `CliScriptsInfo` with:
  - `CliName`: 4-character lowercase string
  - `Description`: string (max 300 chars)
  - **JSON Schema:**
  ```json
  [
    {
      "CliName": "abcd",
      "Description": "Max 300 characters"
    }
  ]
  ```
