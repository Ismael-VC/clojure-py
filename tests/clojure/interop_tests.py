from clojure.lang.rt import *
import unittest


class TestTupleInterop(unittest.TestCase):
    def test_tuple_seq(self):
        data = (1, 2, 3, 4, 5, 6,)
        s = seq(data)
        i = 0
        while s is not None:
            self.assertEqual(data[i], first(s))
            i += 1
            s = next(s)

        self.assertEqual(i, len(data))

        self.assertEqual(hash(data), hash(data))

        self.assertEqual(hash(data), hash(seq(data)))

        self.assertEqual(seq(data), seq(data))

    def equiv_tests(self):
        self.assertEqual(equiv(1, 1), True)

    def reducing_tests(self):
        data = (1, 2, 3, 4, 5, 6,)

        result = reduce(lambda x, y: x + y, 0, seq(data))

        self.assertEqual(result, 21)

