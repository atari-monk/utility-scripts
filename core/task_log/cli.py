from core.task_log.db_path import DbPath
from core.task_log.db_table import DbTablePath
from core.task_log.models.project import Project
from core.task_log.record import Record
from core.task_log.task_info import TaskInfo

def main():
  db_info = DbPath(repoPath = r"C:\atari-monk\code\utility-scripts-data", dbFolder = "task_log")
  project_table = DbTablePath(db_info, lambda: "projects")
  task_table = DbTablePath(db_info, lambda: "tasks_1")
  record_table = DbTablePath(db_info, lambda: "records_2025_04")
  
  projects = Project.loadFromJson(project_table.get_path())  
  Project.getListString(projects)

  tasks = TaskInfo.load_from_json(task_table.get_path())
  TaskInfo.display_as_list(tasks)

  records = Record.load_from_json(record_table.get_path())
  Record.display_as_list(records)

if __name__ == '__main__':
  main()