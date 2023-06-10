from UI.View import View
from UI.Commands.Command import Command


class SaveData(Command):
    def __init__(self, console: View):
        super().__init__(console)

    def get_description(self):
        return "Сохранить изменения в файл"

    def execute(self):
        self.get_console().save_data()
