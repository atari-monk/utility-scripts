# Scheme Script

## Configuration Format - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Python dataclass named `SchemeInfo` with:
  - `Name`: lowercase string (max 50 chars)
  - `Description`: string (max 300 chars)
  - `Path`: string
  - validation methods
  - methods loading List[SchemeInfo] from json file
  - Method that takes name, selects scheme from list, loads file from `Path` and puts it in clipboard, lets handle text files
  - **JSON Schema:**
  ```json
  [
    {
      "Name": "Max 50 chars",
      "Description": "Max 300 characters",
      "Path": "C:\\atari-monk\\code\\dev-blog\\design\\schemeName.md"
    }
  ]
  ```
- Development Process:
  1. Write unit tests first
  2. Implement classes to pass tests
- Code Style:
  - No comments (self-documenting code only)
