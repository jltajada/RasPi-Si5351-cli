import unittest
from src.Model import Model
from src.output.DefaultOutput import DefaultOutput

class TestDefaultOutput(unittest.TestCase):
    def test_update(self):
        m = Model(3500, 100)
        do = DefaultOutput()

        m.registerOutput(do)
        m.start()
        self.assertEqual(3500, do.lastFreq)

if __name__ == '__main__':
    unittest.main()
