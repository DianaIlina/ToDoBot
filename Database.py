import json
from cfg import DB_PATH
import os


SAVES_FILENAME = os.path.join(DB_PATH, "Saves.json")
HELP_FILENAME = os.path.join(DB_PATH, "Help.txt")
TASKS_FILENAME = os.path.join(DB_PATH, "Tasks.json")

def read_help_from_file():
    return read_text(HELP_FILENAME)


def read_saves_from_file():
    return read_json(SAVES_FILENAME)


def write_saves_to_file(saves):
    write_json(SAVES_FILENAME, saves)


def read_tasks_from_file():
    return read_json(TASKS_FILENAME)


def write_tasks_to_file(tasks):
    write_json(TASKS_FILENAME, tasks)


# Functions for JSON

def read_json(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        return {}


def write_json(filename, obj):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4)


# Functions for text


def read_text(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        return {}



def write_text(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
