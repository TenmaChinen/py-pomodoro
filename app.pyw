from controller import Controller
from model import Model
from view import View

class App:

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model,self.view)
        self.view.set_controller(self.controller)

    def run(self):
        self.view.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()
