# Task Log Script

Cli to track task time.

## Feature Specification Assumptions

- Development Process:
  1. Write unit tests first
  2. Write feature code to pass tests
- Code Style:
  - python
  - No comments, self-documenting code only

## Paths - Feature Specification

**Implementation Requirements:**

- ## Functionality:
  - Class DbPath constructing path to db
  - data_repo_path
  - db_folder
  - Check/generate folders logic
  - Property DbPath = data_repo_path + db_name
  - Class DbTable constructing path to db table
  - DbPath as param
  - function to generate name, with file extension as param, default json

## Project Model - Feature Specification

**Implementation Requirements:**

- Functionality:
  - Python dataclass named `Project` with:
    - methods to validate
    - method loading List[Project] from json file
    - method to produce string as object list
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
    - methods to validate
    - method loading List[Task] from json file
    - method to produce string as object list
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
    - methods to validate
    - method loading List[Record] from json file
    - method loading last record from json file
    - method to produce string as object list
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
