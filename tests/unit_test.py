from unittest import TestCase
from horoscope import horoscope


class NostraUnitTest(TestCase):

    def setUp(self):
        print

    def test_generate(self):
        results = horoscope.generate()
        print results
        self.assertTrue(results)

    def test_relationship(self):
        for mood in ['good', 'bad']:
            results = horoscope.relationship(mood)
            print results
            self.assertTrue(results)

    def test_encounter(self):
        for mood in ['good', 'bad']:
            results = horoscope.encounter(mood)
            print results
            self.assertTrue(results)

    def test_word_data(self):
        word_data = {
            "familiar people": [
                "your mother",
                "your father",
                "your closest friend",
                "a family member"
            ]
        }

        # Call function to insert data
        for val in word_data.keys():
            print val


