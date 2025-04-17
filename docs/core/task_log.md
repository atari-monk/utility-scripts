# Task Log Script

Cli to track task time.

## Feature Specification Assumptions

- Development Process:
  1. Write unit tests first
  2. Write function
- Code Style:
  - python
  - No comments (self-documenting code only)

## Paths - Feature Specification

**Implementation Requirements:**

- ## Functionality:
  - Class constructing paths to save db records
  - base_path - data repo folder
  - db_name - db folder
  - Check/generate folders
  - Property DbPath = base_path + db_name
  - mechanism to produce rules for file names
  - key and some logic to generate name

## Project Model - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Python dataclass named `Project` with:
    - `Id`: string
    - `Name`: lowercase string, repo-name format
    - `Description`: string (max 300 chars)
    - method loading List[Project] from json file
    - Validate input
    - Display as object list
    - **JSON:**
    ```json
    [
      {
        "Id": "Some Standard Format for id",
        "Name": "Project Name",
        "Description": "Max 300 characters"
      }
    ]
    ```

## Task Model - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Python dataclass named `Task` with:
    - `Id`: string
    - `ProjectId`: string
    - `Name`: lowercase string, repo-name format
    - `Description`: string (max 300 chars)
    - method loading List[Task] from json file
    - Validate input
    - Display as object list
    - **JSON:**
    ```json
    [
      {
        "Id": "Some Standard Format for id",
        "ProjectId": "Some Standard Format for id",
        "Name": "Task Name",
        "Description": "Max 300 characters"
      }
    ]
    ```

## Record Model - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Python dataclass named `Record` with:
    - methods validating input
    - method displaying as object list
    - method loading List[Record] from json file
    - method loading last record from json file
    - **JSON:**
    ```json
    [
      {
        "Date": "2025-04-17",
        "TaskId": "1",
        "Description": "Max 300 characters",
        "Estimate Minutes": 0,
        "Start Time": "19:03",
        "End Time": "20:55",
        "Actual Minutes": 0,
        "Note": "Max 300 characters"
      }
    ]
    ```
