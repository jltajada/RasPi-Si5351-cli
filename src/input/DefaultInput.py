from src.Model import Model

class DefaultInput(object):
    def __init__(self, model):
        if not isinstance(model, Model):
            raise TypeError("Passed wrong object to DefaultInput")
        self.model = model


    def up(self):
        self.model.stepUp()

    def down(self):
        self.model.stepDown()

    def start(self):
        pass
