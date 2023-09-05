from pathlib import Path
from database import Database, Note

CUR_DIR = Path(__file__).parent

def extract_route(request):
    if request == '':
        return ''
    retorno = request.split(' ')[1]
    retorno = retorno[1:]
    return retorno

def read_file(path):
    with open(path, "rb") as file:
        content = file.read()
    return content

def load_data():
    database = Database('banco')
    notes = database.get_all()
    return notes

# def load_template(nome):
#     with open("templates/" + nome, "r",encoding='UTF-8') as file:
#         content = file.read()
#     return str(content)

def load_template(filename):
    FULL_PATH = CUR_DIR / 'templates' / filename
    with open(FULL_PATH, 'r', encoding='UTF-8') as f:
        return f.read()
    

def add_dic(params):
    nota = Note(title=params['titulo'], content=params['detalhes'])
    database = Database('banco')
    database.add(nota)

    # notes_file = Path("notes.json")
    # if notes_file.exists():
    #     with open(notes_file, "r") as file:
    #         notes = json.load(file)
    # else:
    #     notes = []
    # notes.append(new_note)
    # with open(notes_file, "w") as file:
    #     json.dump(notes, file)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        return f'HTTP/1.1 {code} {reason}\n\n{body}'.encode()
    else:
        return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()