from core.task_log.db_info import DbInfo
from core.task_log.db_table import DbTable
from core.task_log.project_info import ProjectInfo
from core.task_log.record import Record
from core.task_log.task_info import TaskInfo

def main():
  db_info = DbInfo(repo_path = r"C:\atari-monk\code\utility-scripts-data", db_name = "task_log")
  project_table = DbTable(db_info, lambda: "projects")
  task_table = DbTable(db_info, lambda: "tasks_1")
  record_table = DbTable(db_info, lambda: "records_2025_04")
  
  projects = ProjectInfo.load_from_json(project_table.get_path())  
  ProjectInfo.display_as_list(projects)

  tasks = TaskInfo.load_from_json(task_table.get_path())
  TaskInfo.display_as_list(tasks)

  records = Record.load_from_json(record_table.get_path())
  Record.display_as_list(records)

if __name__ == '__main__':
  main()