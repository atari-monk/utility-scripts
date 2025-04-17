from pathlib import Path
from core.scheme.scheme_loader import SchemeLoader

scheme_file = Path("C:/path/to/your/schemes.json")
SchemeLoader.load_to_clipboard(scheme_file)
print(f'{scheme_file} copied to clipboard')