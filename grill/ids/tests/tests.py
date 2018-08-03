import unittest
from grill import ids

class TestIDs(unittest.TestCase):

    def test_keys(self):
        for k in ids.cgasset.IDS:
            res = getattr(ids.cgasset, k)
            with self.assertRaises(TypeError):
                res[k] = 'sorry'

    def test_mod(self):
        with self.assertRaises(AttributeError):
            ids.cgasset.hello
