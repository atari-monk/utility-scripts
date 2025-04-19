from datetime import datetime
from pathlib import Path
from core.task_log.db_path import DbPath
from core.task_log.db_table_path import DbTablePath
from core.task_log.models.project import Project
from core.task_log.models.record import Record
from core.task_log.models.task import Task


def main():
    db_path = DbPath(
        repo_path=Path(r"C:\atari-monk\code\utility-scripts-data"), db_folder="task_log"
    )
    project_db_table = DbTablePath(db_path, name_func=lambda: "projects")

    newProject = Project.from_cli_input(project_db_table.get_path())
    Project.save_to_json([newProject], project_db_table.get_path())

    projects = Project.load_from_json(project_db_table.get_path())

    print("\nProject:\n\n" + Project.get_list_string(projects) + "\n")

    projectId = Project.select_project_id(project_db_table.get_path())
    print(projectId)

    for project in projects:
        task_db_table = DbTablePath(db_path, lambda: f"{project.name}_tasks")
        try:
            tasks = Task.load_from_json(task_db_table.get_path())

            print("Task:\n\n" + Task.get_list_string(tasks) + "\n")

            today = datetime.today()
            record_db_table = DbTablePath(
                db_path,
                lambda: f"{project.name}_records_{today.year}_{today.month:02d}",
            )
            records = Record.load_from_json(record_db_table.get_path())

            print("Record:\n\n" + Record.get_list_string(records) + "\n")

        except FileNotFoundError:
            continue


if __name__ == "__main__":
    main()
