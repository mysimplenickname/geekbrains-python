class Stationery:
    title: str

    def __init__(self, user_title=""):
        self.title = user_title

    def draw(self):
        print("Drawing started.")


class Pen(Stationery):
    def draw(self):
        print("Pen drawing started.")


class Pencil(Stationery):
    def draw(self):
        print("Pencil drawing started.")


class Handle(Stationery):
    def draw(self):
        print("Handle drawing started.")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
