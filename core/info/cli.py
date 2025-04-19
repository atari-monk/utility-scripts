from pathlib import Path
from core.info.cli_scripts_info import CliScriptsInfo


def main():
    json_file = Path(r"C:\atari-monk\code\utility-scripts-data\scripts.json")
    loaded_scripts = CliScriptsInfo.load_from_json(json_file)
    print("\nAll scripts:")
    print(CliScriptsInfo.to_string(loaded_scripts))
    print()


if __name__ == "__main__":
    main()
