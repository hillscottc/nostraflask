from unittest import TestCase

from webapp import nostra


class NostraTest(TestCase):

    def setUp(self):
        print

    def test_generate(self):
        results = nostra.generate()
        print results
        self.assertTrue(results)

    def test_relationship(self):
        for mood in ['good', 'bad']:
            results = nostra.relationship(mood)
            print results
            self.assertTrue(results)

    def test_encounter(self):
        for mood in ['good', 'bad']:
            results = nostra.encounter(mood)
            print results
            self.assertTrue(results)

