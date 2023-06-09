from UI.View import View
from UI.Commands.Command import Command


class LoadData(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return "Загрузить файл"

    def execute(self):
        self.get_console().load_data()
