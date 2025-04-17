from core.task_log.path_generator import PathGenerator

def main():
  path_gen = PathGenerator(base_repo="my_repo", db_name="task_logs")
  file_path = path_gen.get_full_path("record_123.json")
  print(f'Saving to {file_path}')

if __name__ == '__main__':
  main()