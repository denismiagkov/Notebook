from UI.View import View
from UI.Commands.Command import Command


class EditNote(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return "Редактировать заметку"

    def execute(self):
        self.get_console().edit_note()
