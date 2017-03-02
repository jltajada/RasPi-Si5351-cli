import unittest

from src.Model import Model, FrequencyUnit

class TestModel(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(TypeError):
            m = Model('foo', 'bar')

        with self.assertRaises(ValueError):
            m = Model(-1, -2)

    def test_normal_use(self):
        m = Model(3500, 100000)
        m.stepUp()
        self.assertEqual(m.getFrequency(), 3600)
        m.stepDown()
        self.assertEqual(m.getFrequency(), 3500)

        self.assertEqual(m.getFrequency(FrequencyUnit.HZ), 3500000)
        self.assertEqual(m.getFrequency(FrequencyUnit.MHZ), 3.5)

if __name__ == '__main__':
    unittest.main()
