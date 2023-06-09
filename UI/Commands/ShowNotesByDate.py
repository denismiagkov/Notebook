from UI.View import View
from UI.Commands.Command import Command


class ShowNotesByDate(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return "Показать список заметок по дате"

    def execute(self):
        self.get_console().show_notes_by_date()
