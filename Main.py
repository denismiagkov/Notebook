from Notebook.Notebook import Notebook
from Presenter.Presenter import Presenter
from Service.Service import Service
from UI.Console import Console
from UI.Menu import Menu

notebook = Notebook()
service = Service(notebook)
console = Console()
presenter = Presenter(service, console)
menu = Menu(console)
console.start()
