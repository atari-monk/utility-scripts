import json
from pathlib import Path
from core.scheme.scheme_info import SchemeInfo

def main():
    try:
        scheme_file = Path(r"C:\atari-monk\code\utility-scripts-data\schemes.json")
        schemes = SchemeInfo.from_json_file(scheme_file)
        
        print("Available schemes:")
        for scheme in schemes:
            print(f"- {scheme.Name}: {scheme.Description}")
        
        scheme_name = input("\nEnter scheme name to copy: ").strip().lower()
        
        SchemeInfo.load_and_copy_scheme(schemes, scheme_name)
        print(f"'{scheme_name}' copied to clipboard!")
        
    except FileNotFoundError:
        print(f"Error: Scheme file not found at {scheme_file}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {scheme_file}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()