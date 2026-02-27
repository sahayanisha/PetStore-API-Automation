import json
from jsonschema import validate
from pathlib import Path

def validate_schema(response_json,schema_path):
    schema_file = Path(schema_path)
    if not schema_file.exists():
        raise FileNotFoundError(f"File {schema_path} does not exiist")
    with schema_file.open("r",encoding="utf-8") as f:
        schema = json.load(f)
    validate(instance=response_json, schema = schema)
