import os
import sys
sys.path += [os.path.join(sys.path[0], '..')]
import buttifier
import unittest

class ButtifierTest(unittest.TestCase):
    def test_camelcase(self):
        self.assertEqual("-".join(buttifier.word("test")), "test")
        self.assertEqual("-".join(buttifier.word("tesT")), "tes-T")
        self.assertEqual("-".join(buttifier.word("teSt")), "te-St")
        self.assertEqual("-".join(buttifier.word("teST")), "te-ST")

        self.assertEqual("-".join(buttifier.word("tEst")), "t-Est")
        self.assertEqual("-".join(buttifier.word("tEsT")), "t-Es-T")
        self.assertEqual("-".join(buttifier.word("tESt")), "t-ESt")
        self.assertEqual("-".join(buttifier.word("tEST")), "t-EST")

        self.assertEqual("-".join(buttifier.word("Test")), "Test")
        self.assertEqual("-".join(buttifier.word("TesT")), "Tes-T")
        self.assertEqual("-".join(buttifier.word("TeSt")), "Te-St")
        self.assertEqual("-".join(buttifier.word("TeST")), "Te-ST")

        self.assertEqual("-".join(buttifier.word("TEst")), "TEst")
        self.assertEqual("-".join(buttifier.word("TEsT")), "TEs-T")
        self.assertEqual("-".join(buttifier.word("TESt")), "TESt")
        self.assertEqual("-".join(buttifier.word("TEST")), "TEST")

    def test_runs(self):
        self.assertEqual("-".join(buttifier.word("whaaaaat")), "whaaaaat")

    def test_url(self):
        sent = buttifier.sentence("a url: http://www.example.com/")
        self.assertEqual(str(sent[0]), "a")
        self.assertEqual(str(sent[1]), "url")
        self.assertEqual(str(sent[2]), "http://www.example.com/")

if __name__ == '__main__':
    unittest.main()
