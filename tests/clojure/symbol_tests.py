import unittest
import clojure.lang.rt as RT

class SymbolTests(unittest.TestCase):
    def test_creation(self):
        self.assertEqual(RT.symbol(u"foo"), RT.symbol(u"foo"))
        self.assertNotEqual(RT.symbol(u"foo"), RT.symbol(u"bar"))

    def test_hashing(self):
        self.assertEqual(RT.hash(RT.symbol(u"foo")), RT.hash(RT.symbol(u"foo")))

    def test_meta(self):
        self.assertIsNone(RT.meta(RT.symbol(u"foo")))
        self.assertEqual(RT.meta(RT.with_meta(RT.symbol(u"foo"), 42)), 42)

    def test_str(self):
        self.assertEqual(str(RT.symbol(u"foo", u"bar")), "foo/bar")
        self.assertEqual(repr(RT.symbol(u"foo", u"bar")), "foo/bar")

    def test_named(self):
        self.assertEqual(RT.name(RT.symbol(u"foo")), u"foo")
        self.assertEqual(RT.namespace(RT.symbol(u"foo", u"bar")), u"foo")
