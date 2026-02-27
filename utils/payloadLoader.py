import json
from pathlib import Path

def load_json(file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File {file_path} does not exist")
    with path.open("r",encoding = "utf-8") as f:
        return json.load(f)
