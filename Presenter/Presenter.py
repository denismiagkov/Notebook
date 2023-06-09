
from typing import List
from datetime import date
from Note.Note import Note
from Service.Service import Service
from UI.View import View


class Presenter:
    def __init__(self, service: Service, view: View):
        self.service = service
        self.view = view
        view.set_presenter(self)

    def show_list(self) -> List[str]:
        titles = []
        for n in self.service.get_notebook():
            titles.append(n.get_title())
        return titles

    def show_notes_by_date(self, local_date: date) -> List[Note]:
        return self.service.show_notes_by_date(local_date)

    def get_note(self, title: str) -> str:
        return str(self.service.get_note(title))

    def add_note(self, title: str, body: str):
        self.service.add_note(title, body)

    def remove_note(self, title: str):
        self.service.remove_note(title)

    def contains_of(self, title: str) -> bool:
        return self.service.contains_of(title)

    def set_body(self, title: str, body: str):
        self.service.set_body(title, body)

    def set_date(self, title: str):
        self.service.set_date(title)

    def save_data(self, file_name: str):
        self.service.save_data(file_name)

    def load_data(self, file_name: str):
        self.service.load_data(file_name)