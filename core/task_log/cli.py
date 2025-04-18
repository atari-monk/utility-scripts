from core.task_log.db_path import DbPath
from core.task_log.db_table_path import DbTablePath
from core.task_log.models.project import Project
from core.task_log.models.record import Record
from core.task_log.models.task import Task

def main():
  db_path = DbPath(repoPath = r"C:\atari-monk\code\utility-scripts-data", dbFolder = "task_log")
  
  project_db_table = DbTablePath(db_path, lambda: "projects")

  projects = Project.loadFromJson(project_db_table.get_path())  

  Project.getListString(projects)


  # task_db_table = DbTablePath(db_path, lambda: "tasks_1")

  # record_table = DbTablePath(db_path, lambda: "records_2025_04")
  
  
  # tasks = Task.load_from_json(task_db_table.get_path())
  # Task.display_as_list(tasks)

  # records = Record.load_from_json(record_table.get_path())
  # Record.display_as_list(records)

if __name__ == '__main__':
  main()