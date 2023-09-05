import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(f'{name}.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);')

    def add(self, note):
        self.conn.execute(f'INSERT INTO note (title, content) VALUES ("{note.title}", "{note.content}");')
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute('SELECT id, title, content FROM note;')
        notas = []
        for linha in cursor:
            identificador = linha[0]
            titulo = linha[1]
            conteudo = linha[2]
            nota = Note(identificador, titulo, conteudo)
            notas.append(nota)

        return notas
    
    def update(self, entry):
        self.conn.execute('UPDATE note SET title = ?, content = ? WHERE id = ?;', (entry.title, entry.content, entry.id))
        self.conn.commit()


    def delete(self, note_id):
        self.conn.execute(f'DELETE FROM note WHERE id = {note_id};')
        self.conn.commit()


    

