from datetime import date, datetime
from typing import List
from Note.Note import Note
import json


# from Notebook.NoteIterator import NoteIterator


class Notebook:
    def __init__(self, notebook=None):
        if notebook is None:
            notebook = []
        self.notebook = notebook

    def get_notebook(self):
        return self.notebook

    # def __init__(self, notebook: List[Note] = []):
    #     self.notebook = notebook

    def __str__(self):
        res = ""
        for n in self.notebook:
            res += str(n)
        return res

    # def __iter__(self):
    #    return NoteIterator(self.notebook)

    def add_record(self, n: Note):
        self.notebook.append(n)

    def remove_record(self, title: str):
        for i, n in enumerate(self.notebook):
            if title == n.get_title():
                del self.notebook[i]
                break

    def get_note(self, title: str) -> Note:
        for n in self.notebook:
            if title == n.get_title():
                return n
        return None

    def contains_of(self, title: str) -> bool:
        return self.get_note(title) in self.notebook

    def show_notes_by_date(self, local_date: date) -> List[Note]:
        temp = []
        for n in self.notebook:
            if local_date == n.get_date().date():
                temp.append(n)
        return temp

    def save_data(self, file_name: str):
        data = {}
        data['notes'] = []
        for n in self.notebook:
            data['notes'].append({
                'id': n.get_id(),
                'datetime': n.get_date().isoformat(),
                'title': n.get_title(),
                'body': n.get_body()
            })
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile, default=str)

    def load_data(self, file_name: str):
        with open(file_name) as json_file:
            data = json.load(json_file)
            for p in data['notes']:
                date_time = datetime.strptime(p['datetime'], '%Y-%m-%dT%H:%M:%S.%f')
                note = Note(p['id'], date_time, p['title'], p['body'])
                self.notebook.append(note)




                #print('id: ' + str(p['id']))
                #print('datetime: ' + p['datetime'])
                #print('title: ' + p['title'])
                #print('body: ' + p['body'])
                #print('')


