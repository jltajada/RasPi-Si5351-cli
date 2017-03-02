from enum import Enum
from src.Signal import Signal
from src.output.DefaultOutput import DefaultOutput
class FrequencyUnit(Enum):
    HZ  = 0
    KHZ = 1
    MHZ = 2


class Model(object):
    def __init__(self, freq, step):
        if not isinstance(freq, int) or not isinstance(step, int):
            raise TypeError('Invalid type in Model constructor.'
                            'freq:', type(freq), ', step:', type(step))
        if freq <= 0 or step <= 0:
            raise ValueError('Invalid values in Model constructor - '
                             'not positive numbers.')

        self.freq = freq*1000
        self.step = step
        self.changed = Signal()

    def start(self):
        self.changed.fire(self)

    def registerOutput(self, output):
        if not issubclass(output.__class__ , DefaultOutput):
            raise TypeError("Tried to register object that isn't output(", type(output),")")

        self.changed.connect(getattr(output, "update"))


    def stepUp(self):
        self.freq += self.step
        self.changed.fire(self)

    def stepDown(self):
        self.freq -= self.step
        self.changed.fire(self)

    def getFrequency(self, unit=FrequencyUnit.KHZ):
        return self.freq / 10 ** (unit.value*3)
