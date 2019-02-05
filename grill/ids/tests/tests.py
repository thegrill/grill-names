import unittest
from grill import ids


class TestIDs(unittest.TestCase):

    def test_keys(self):
        for k in dir(ids):
            res = getattr(ids, k)
            with self.assertRaises(TypeError):
                res[k] = 'sorry'

    def test_mod(self):
        with self.assertRaises(AttributeError):
            ids.hello
