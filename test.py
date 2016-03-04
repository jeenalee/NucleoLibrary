import unittest, sys
sys.path.append('/Users/Jeena/src')
from NucleoLibrary import dna

class DNAtest(unittest.TestCase):
    def test_complement(self):
        self.assertEqual(dna.complement("ACTGACTG"), "CAGTCAGT")
        self.assertRaises(ValueError, dna.complement, "hello")
        self.assertRaises(ValueError, dna.complement, "ACT ACTG ")
        
    def test_reverse(self):
        self.assertEqual(dna.reverse("ACTGACTG"), "GTCAGTCA")

    def test_converting_to_RNA(self):
        self.assertEqual(dna.convert_to_RNA("ACTGACTG"), "CAGUCAGU")
        self.assertRaises(ValueError, dna.convert_to_RNA, "ACUGUGU")

    def test_GCfraction(self):
        self.assertEqual(dna.GCfraction("TATATATATATA"), 0)
        self.assertEqual(dna.GCfraction("GCGCGCGCGC"), 1)
        self.assertEqual(dna.GCfraction("GCGCTATA"), 0.5)

    def test_is_present(self):
        self.assertTrue(dna.is_present("ACTGACTGACTG", "ACT"))
        self.assertFalse(dna.is_present("ACTGACTGACTG", "GTA"))

    def test_highlight(self):
        self.assertEqual(dna.highlight("ACACGTGTACAC", "GTGT"), "ACAC-GTGT-ACAC")
        self.assertEqual(dna.highlight("ACACGTGTACAC", "GTGT", highlighter="/"), \
                                       "ACAC/GTGT/ACAC")
        self.assertRaises(ValueError, dna.highlight, "ACTG AGAG", "AGAG")

if __name__ == '__main__':
    unittest.main()
