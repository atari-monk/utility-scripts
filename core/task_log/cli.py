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

    add_new_project(project_db_table)

    add_new_task(db_path, project_db_table)

    read_all(db_path, project_db_table)


def add_new_project(project_db_table):
    new_project = Project.from_cli_input(project_db_table.get_path())
    Project.save_to_json([new_project], project_db_table.get_path())


def add_new_task(db_path, project_db_table):
    project = Project.select_project(project_db_table.get_path())
    task_db_table = DbTablePath(db_path, lambda: f"{project.name}_tasks")

    new_task = Task.from_cli_input(
        task_db_table.get_path(), project_db_table.get_path()
    )
    Task.save_to_json([new_task], task_db_table.get_path())


def read_all(db_path, project_db_table):
    projects = Project.load_from_json(project_db_table.get_path())

    print("\nProject:\n\n" + Project.get_list_string(projects) + "\n")

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
