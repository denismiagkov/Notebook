from UI.View import View
from UI.Commands.Command import Command


class Finish(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return "Завершить работу"

    def execute(self):
        self.get_console().finish()
