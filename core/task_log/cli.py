from core.task_log.path_generator import PathGenerator
from core.task_log.project_info import ProjectInfo

def main():
  path_gen = PathGenerator(base_repo="my_repo", db_name="task_logs")
  file_path = path_gen.get_full_path("record_123.json")
  print(f'Saving to {file_path}')

  projects = ProjectInfo.from_json(r"C:\atari-monk\code\utility-scripts-data\task_log\projects.json")  
  ProjectInfo.display_as_list(projects)

if __name__ == '__main__':
  main()