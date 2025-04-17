# Scheme Script

## Configuration Format - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Load from JSON array (see format below)
  - Validate input
  - Display as object list
  - Give it a method to load json from `Path` and put it in clipboard
- Development Process:
  1. Write unit tests first
  2. Implement dataclass to pass tests
- Code Style:
  - No comments (self-documenting code only)
- Python dataclass named `SchemeInfo` with:

  - `Name`: lowercase string (max 50 chars)
  - `Description`: string (max 300 chars)
  - `Path`: string
  - **JSON Schema:**

  ```json
  [
    {
      "Name": "Max 50 chars",
      "Description": "Max 300 characters",
      "Path": "C:\\atari-monk\\code\\dev-blog\\design\\schemeName.json"
    }
  ]
  ```
