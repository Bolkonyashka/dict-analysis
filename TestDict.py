import unittest
from dict import BFDict, BSDict, BTDict, BBTDict, HDict


class TestDicts(unittest.TestCase):

    def test_BFDict_get(self):
        dct = BFDict()
        dct.add(("Roma", 1), ("Fofo", 2), ("ffdf", 3), ("fdfsfg", 5), ("fhgrfhrh", 6), ("gjhjrh", 7), ("hlkh", 8),
                ("fhjkrh", 9), ("yjyj", 10))
        self.assertEqual(dct.get("Roma"), 1)
        self.assertEqual(dct.get("gjhjrh"), 7)
        self.assertEqual(dct.get("Fofo"), 2)

    def test_BFDict_items_keys_values(self):
        dct = BFDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        self.assertTrue(("ковер", 8) in dct.items())
        self.assertTrue(("раковина", 12) in dct.items())
        self.assertTrue("Сковородка" in dct.keys())
        self.assertTrue("диван" in dct.keys())
        self.assertTrue(3 in dct.values())
        self.assertTrue(7 in dct.values())

    def test_BFDict_pop(self):
        dct = BFDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        dct.pop("пол")
        dct.pop("стол")
        self.assertFalse(("пол", 3) in dct.items())
        self.assertFalse("пол" in dct.keys())
        self.assertFalse(3 in dct.values())
        self.assertFalse(("стол", 7) in dct.items())
        self.assertFalse("стол" in dct.keys())
        self.assertFalse(7 in dct.values())

    def test_BSDict_get(self):
        dct = BSDict()
        dct.add(("Roma", 1), ("Fofo", 2), ("ffdf", 3), ("fdfsfg", 5), ("fhgrfhrh", 6), ("gjhjrh", 7), ("hlkh", 8),
                ("fhjkrh", 9), ("yjyj", 10))
        self.assertEqual(dct.get("Roma"), 1)
        self.assertEqual(dct.get("gjhjrh"), 7)
        self.assertEqual(dct.get("Fofo"), 2)

    def test_BSDict_items_keys_values(self):
        dct = BSDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        self.assertTrue(("ковер", 8) in dct.items())
        self.assertTrue(("раковина", 12) in dct.items())
        self.assertTrue("Сковородка" in dct.keys())
        self.assertTrue("диван" in dct.keys())
        self.assertTrue(3 in dct.values())
        self.assertTrue(7 in dct.values())

    def test_BSDict_pop(self):
        dct = BSDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        dct.pop("пол")
        dct.pop("стол")
        self.assertFalse(("пол", 3) in dct.items())
        self.assertFalse("пол" in dct.keys())
        self.assertFalse(3 in dct.values())
        self.assertFalse(("стол", 7) in dct.items())
        self.assertFalse("стол" in dct.keys())
        self.assertFalse(7 in dct.values())

    def test_BTDict_get(self):
        dct = BTDict()
        dct.add(("Roma", 1), ("Fofo", 2), ("ffdf", 3), ("fdfsfg", 5), ("fhgrfhrh", 6), ("gjhjrh", 7), ("hlkh", 8),
                ("fhjkrh", 9), ("yjyj", 10))
        self.assertEqual(dct.get("Roma"), 1)
        self.assertEqual(dct.get("gjhjrh"), 7)
        self.assertEqual(dct.get("Fofo"), 2)

    def test_BTDict_items_keys_values(self):
        dct = BTDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        self.assertTrue(("ковер", 8) in dct.items())
        self.assertTrue(("раковина", 12) in dct.items())
        self.assertTrue("Сковородка" in dct.keys())
        self.assertTrue("диван" in dct.keys())
        self.assertTrue(3 in dct.values())
        self.assertTrue(7 in dct.values())

    def test_BTDict_pop(self):
        dct = BTDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        dct.pop("пол")
        dct.pop("стол")
        self.assertFalse(("пол", 3) in dct.items())
        self.assertFalse("пол" in dct.keys())
        self.assertFalse(3 in dct.values())
        self.assertFalse(("стол", 7) in dct.items())
        self.assertFalse("стол" in dct.keys())
        self.assertFalse(7 in dct.values())

    def test_BBTDict_get(self):
        dct = BBTDict()
        dct.add(("Roma", 1), ("Fofo", 2), ("ffdf", 3), ("fdfsfg", 5), ("fhgrfhrh", 6), ("gjhjrh", 7), ("hlkh", 8),
                ("fhjkrh", 9), ("yjyj", 10))
        self.assertEqual(dct.get("Roma"), 1)
        self.assertEqual(dct.get("gjhjrh"), 7)
        self.assertEqual(dct.get("Fofo"), 2)

    def test_BBTDict_items_keys_values(self):
        dct = BBTDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        self.assertTrue(("ковер", 8) in dct.items())
        self.assertTrue(("раковина", 12) in dct.items())
        self.assertTrue("Сковородка" in dct.keys())
        self.assertTrue("диван" in dct.keys())
        self.assertTrue(3 in dct.values())
        self.assertTrue(7 in dct.values())

    def test_BBTDict_pop(self):
        dct = BBTDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        dct.pop("пол")
        dct.pop("стол")
        self.assertFalse(("пол", 3) in dct.items())
        self.assertFalse("пол" in dct.keys())
        self.assertFalse(3 in dct.values())
        self.assertFalse(("стол", 7) in dct.items())
        self.assertFalse("стол" in dct.keys())
        self.assertFalse(7 in dct.values())

    def test_HDict_get(self):
        dct = HDict()
        dct.add(("Roma", 1), ("Fofo", 2), ("ffdf", 3), ("fdfsfg", 5), ("fhgrfhrh", 6), ("gjhjrh", 7), ("hlkh", 8),
                ("fhjkrh", 9), ("yjyj", 10))
        self.assertEqual(dct.get("Roma"), 1)
        self.assertEqual(dct.get("gjhjrh"), 7)
        self.assertEqual(dct.get("Fofo"), 2)

    def test_HDict_items_keys_values(self):
        dct = HDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        self.assertTrue(("ковер", 8) in dct.items())
        self.assertTrue(("раковина", 12) in dct.items())
        self.assertTrue("Сковородка" in dct.keys())
        self.assertTrue("диван" in dct.keys())
        self.assertTrue(3 in dct.values())
        self.assertTrue(7 in dct.values())

    def test_HDict_pop(self):
        dct = HDict()
        dct.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10),
                ("Сковородка", 11), ("раковина", 12))
        dct.pop("пол")
        dct.pop("стол")
        self.assertFalse(("пол", 3) in dct.items())
        self.assertFalse("пол" in dct.keys())
        self.assertFalse(3 in dct.values())
        self.assertFalse(("стол", 7) in dct.items())
        self.assertFalse("стол" in dct.keys())
        self.assertFalse(7 in dct.values())



if __name__ == '__main__':
    unittest.main()
