# From http://codereview.stackexchange.com/questions/20938/the-observer-design-pattern-in-python-in-a-more-pythonic-way-plus-unit-testing

class Signal(object):
    def __init__(self):
        self._handlers = []

    def connect(self, handler):
        self._handlers.append(handler)

    def fire(self, *args):
        for handler in self._handlers:
            handler(*args)