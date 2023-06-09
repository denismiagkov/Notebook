from datetime import date
from typing import List
from Note.Note import Note
#from Notebook.NoteIterator import NoteIterator


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

    #def __iter__(self):
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
