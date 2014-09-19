from clojure.lang.rt import *
import unittest


class TestPersistentVector(unittest.TestCase):

    def test_conj_and_nth(self):
        acc = vector()
        for x in range(80):
            acc = conj(acc, x)

            for y in range(x):
                self.assertEqual(y, nth(acc, y))


