import unittest
import clojure.lang.rt as RT

class TestHashing(unittest.TestCase):
    def test_int_hashing(self):
        self.assertEqual(RT.hash(42), RT.hash(42))

    def test_hashing_things(self):
        self.assertEqual(RT.hash(u"42"), RT.hash(u"42"))
        self.assertEqual(RT.hash(True), RT.hash(True))
        self.assertEqual(RT.hash(None), RT.hash(None))
        self.assertEqual(RT.hash(42.0), RT.hash(42.0))
