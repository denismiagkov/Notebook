from UI.View import View
from UI.Commands.Command import Command


class ReadNote(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return "Прочитать заметку"

    def execute(self):
        self.get_console().read_note()
