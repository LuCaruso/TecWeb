import json
from pathlib import Path

CUR_DIR = Path(__file__).parent

def extract_route(request):
    linhas = request.split(" ")
    return linhas[1][1:]

def read_file(path) -> bytes:
    with open(path, "rb") as file:
        content = file.read()
    return content

def load_data(nome):
    with open("data/" + nome, "r",encoding='UTF-8') as file:
        content = file.read()
    return json.loads(content)

def load_template(nome):
    with open("templates/" + nome, "r",encoding='UTF-8') as file:
        content = file.read()
    return str(content)

def add_note(new_note):
    notes_file = Path("notes.json")
    if notes_file.exists():
        with open(notes_file, "r") as file:
            notes = json.load(file)
    else:
        notes = []
    notes.append(new_note)
    with open(notes_file, "w") as file:
        json.dump(notes, file)