import json
import os

def load_data(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
