
from typing import List
from datetime import datetime

from Note.Note import Note
from Notebook import Notebook


class Service:
    def __init__(self, notebook: Notebook):
        #self.id = 0
        #self.date = None
        self.notebook = notebook

    def add_note(self, title: str, body: str):
        if not hasattr(self, 'id'):
            self.id = 1
        date = datetime.now()
        self.notebook.add_record(Note(self.id, date, title.upper(), body))
        self.id += 1

    def remove_note(self, title: str):
        self.notebook.remove_record(title)

    def get_notebook(self) -> List[Note]:
        return self.notebook.get_notebook()

    def get_note(self, title: str) -> Note:
        return self.notebook.get_note(title)

    def contains_of(self, title: str) -> bool:
        return self.notebook.contains_of(title)

    def set_body(self, title: str, body: str):
        self.notebook.get_note(title).set_body(body)

    def set_date(self, title: str):
        self.notebook.get_note(title).set_date(datetime.now())

    def show_notes_by_date(self, datetime: datetime) -> List[Note]:
        return self.notebook.show_notes_by_date(datetime)

    def save_data(self, file_name: str):
        self.notebook.save_data(file_name)

    def load_data(self, file_name: str):
        self.notebook.load_data(file_name)