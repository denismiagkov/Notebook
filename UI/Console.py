import datetime
from Presenter import Presenter
from UI.Menu import Menu
from UI.View import View


class Console(View):
    def __init__(self):
        self.presenter = None
        self.scanner = input
        self.work = True
        self.menu = Menu(self)

    def print(self, text):
        print(text)

    def start(self):
        while self.work:
            print(self.menu.print())
            choice = self.scanner()
            if self.check(choice, self.menu.get_size()):
                self.menu.execute(int(choice))
            else:
                self.fail()

    def set_presenter(self, presenter):
        self.presenter = presenter

    def check(self, text, n):
        return text.isdigit() and n >= int(text) > 0

    def fail(self):
        print("Ошибка ввода!")

    def finish(self):
        print("Работа программы завершена")
        self.work = False

    def get_presenter(self):
        return self.presenter

    def set_scanner(self, scanner):
        self.scanner = scanner

    def show_list(self):
        print(self.presenter.show_list())

    def show_notes_by_date(self):
        print("Введите дату заметки в формате ГГГГ ММ ДД: ")
        date = self.scanner().split(" ")
        localDate = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        print(self.presenter.show_notes_by_date(localDate))

    def add_note(self):
        print("Введите название заметки: ")
        title = self.scanner()
        print("Введите заметку: ")
        body = self.scanner()
        self.presenter.add_note(title, body)


    def remove_note(self):
        print("Введите название заметки: ")
        title = input().upper()
        if self.presenter.contains_of(title):
            self.presenter.remove_note(title)
            print("Заметка удалена")
        else:
            print("Заметка с таким названием отсутствует!")

    def edit_note(self):
        print("Введите название заметки: ")
        title = input().upper()
        if self.presenter.contains_of(title):
            print("Введите текст заметки")
            body = input()
            self.presenter.set_date(title)
            self.presenter.set_body(title, body)
            print("Заметка изменена")
        else:
            print("Такой заметки не существует!")

    def read_note(self):
        print("Введите название заметки: ")
        title = input().upper()
        if self.presenter.contains_of(title):
            print(self.presenter.get_note(title))
        else:
            print("Заметка с таким названием отсутствует!")

    def save_data(self):
        print("Введите название и расширение файла: ")
        file_name = input()
        self.presenter.save_data(file_name)
