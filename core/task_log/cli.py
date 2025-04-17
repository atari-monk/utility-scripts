from core.task_log.path_generator import PathGenerator
from core.task_log.project_info import ProjectInfo
from core.task_log.task_info import TaskInfo

def main():
  path_gen = PathGenerator(base_repo=r"C:\atari-monk\code\utility-scripts-data", db_name="task_log")
  file_path = path_gen.get_full_path("task_1.json")
  print(f'Saving to {file_path}')

  projects = ProjectInfo.from_json(r"C:\atari-monk\code\utility-scripts-data\task_log\projects.json")  
  ProjectInfo.display_as_list(projects)

  tasks = TaskInfo.from_json(file_path)
  TaskInfo.display_as_list(tasks)

if __name__ == '__main__':
  main()