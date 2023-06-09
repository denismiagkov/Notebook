from UI.View import View
from UI.Commands.Command import Command


class ShowList(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return " Посмотреть список заметок"

    def execute(self):
        self.get_console().show_list()
