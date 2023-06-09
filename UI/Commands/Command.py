from abc import abstractmethod

from UI.Commands.Option import Option
from UI.View import View


class Command(Option):
    def __init__(self, console: View):
        self.console = console

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def get_console(self):
        return self.console
