from UI.Commands.AddNote import AddNote
from UI.Commands.EditNote import EditNote
from UI.Commands.Finish import Finish
from UI.Commands.ReadNote import ReadNote
from UI.Commands.RemoveNote import RemoveNote
from UI.Commands.SaveChanges import SaveChanges
from UI.Commands.ShowList import ShowList
from UI.Commands.ShowNotesByDate import ShowNotesByDate
from UI.View import View


class Menu:
    def __init__(self, console: View):
        self.list = []
        self.list.append(ShowList(console))
        self.list.append(ShowNotesByDate(console))
        self.list.append(ReadNote(console))
        self.list.append(AddNote(console))
        self.list.append(EditNote(console))
        self.list.append(RemoveNote(console))
        self.list.append(SaveChanges(console))
        #self.list.append(LoadFile(console))
        self.list.append(Finish(console))

    def print(self):
        sb = ""
        for i in range(len(self.list)):
            sb += str(i + 1) + ". " + self.list[i].get_description() + "\n"
        return sb

    def get_size(self):
        return len(self.list)

    def execute(self, choice):
        self.list[choice - 1].execute()
