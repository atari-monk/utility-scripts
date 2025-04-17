# Task Log Script

Cli to track task time.

## Paths - Feature Specification

**Implementation Requirements:**

- ## Functionality:
  - Class validating path to save db record
  - Base path with db repo
  - Folder name for db
  - Folder of year yyyy
  - Folder of moth mm
  - path = repo/db/yyyy/mm/fileName
  - path should update according to current time to generate files structure
  - Check/generate folders, return path
  - will be used to save records
- Development Process:
  1. Write unit tests first
  2. Write function
- Code Style:
  - python
  - No comments (self-documenting code only)

## Project Model - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Python dataclass named `ProjectInfo` with:
    - `Name`: lowercase string, repo-name format
    - `Description`: string (max 300 chars)
    - Load from JSON file (see format below)
    - Validate input
    - Display as object list
    - **JSON Schema:**
    ```json
    [
      {
        "Id": "Some Standard Format for id",
        "Name": "Project Name",
        "Description": "Max 300 characters"
      }
    ]
    ```
- Development Process:
  1. Write unit tests first
  2. Implement dataclass to pass tests
- Code Style:
  - No comments (self-documenting code only)

