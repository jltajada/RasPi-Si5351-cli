import unittest
from src.output.CliOutput import CliOutput
from src.Model import Model

class TestCliOutput(unittest.TestCase):
    def test_something(self):
        m = Model(3500,100)
        c = CliOutput()
        m.registerOutput(c)
        m.start()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
