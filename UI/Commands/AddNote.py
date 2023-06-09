from UI.Commands.Command import Command
from UI.View import View


class AddNote(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return "Добавить заметку"

    def execute(self):
        self.get_console().add_note()
