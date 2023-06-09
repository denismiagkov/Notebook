from UI.View import View
from UI.Commands.Command import Command


class RemoveNote(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return "Удалить заметку"

    def execute(self):
        self.get_console().remove_note()
