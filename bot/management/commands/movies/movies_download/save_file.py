import os
import json

FILE_ID_STORAGE = "file_ids.json"

def save_file_id(code, file_id):
    """Save file_id to a JSON file."""
    try:
        if os.path.exists(FILE_ID_STORAGE):
            with open(FILE_ID_STORAGE, 'r') as f:
                file_ids = json.load(f)
        else:
            file_ids = {}

        file_ids[code] = file_id

        with open(FILE_ID_STORAGE, 'w') as f:
            json.dump(file_ids, f)
    except Exception as e:
        print(f"Error saving file_id: {e}")

def get_file_id(code):
    """Retrieve file_id from a JSON file."""
    try:
        if os.path.exists(FILE_ID_STORAGE):
            with open(FILE_ID_STORAGE, 'r') as f:
                file_ids = json.load(f)
                return file_ids.get(code)
    except Exception as e:
        print(f"Error retrieving file_id: {e}")
    return None
