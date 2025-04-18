from pathlib import Path
from core.task_log.db_path import DbPath
from core.task_log.db_table_path import DbTablePath
from core.task_log.models.project import Project
from core.task_log.models.record import Record
from core.task_log.models.task import Task

def main():
  db_path = DbPath(repo_path = Path(r"C:\atari-monk\code\utility-scripts-data"), db_folder = "task_log")
  
  project_db_table = DbTablePath(db_path, name_func = lambda: "projects")

  projects = Project.load_from_json(project_db_table.get_path())  

  print(Project.get_list_string(projects))


  # task_db_table = DbTablePath(db_path, lambda: "tasks_1")

  # record_table = DbTablePath(db_path, lambda: "records_2025_04")
  
  
  # tasks = Task.load_from_json(task_db_table.get_path())
  # Task.display_as_list(tasks)

  # records = Record.load_from_json(record_table.get_path())
  # Record.display_as_list(records)

if __name__ == '__main__':
  main()