class Note:
    def __init__(self, id, date, title, body):
        self.id = id
        self.date = date
        self.title = title
        self.body = body

    def __str__(self):
        return f"\n{self.id}\n{self.date:%d %B %Y года}\n{self.date:%H:%M:%S}\n{self.title}\n{self.body}\n"

    def __eq__(self, other):
        return self.title == other.title and self.body == other.body

    def __hash__(self):
        return hash((self.title, self.date, self.body))

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def get_body(self):
        return self.body

    def get_category(self):
        return self.category

    def set_id(self, id):
        self.id = id

    def set_title(self, title):
        self.title = title

    def set_date(self, date):
        self.date = date

    def set_body(self, body):
        self.body = body

    def set_category(self, category):
        self.category = category
