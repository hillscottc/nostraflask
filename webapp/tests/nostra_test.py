from unittest import TestCase

from .. import nostra


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
            # print results
            self.assertTrue(results)

    def test_encounter(self):
        for mood in ['good', 'bad']:
            results = nostra.encounter(mood)
            # print results
            self.assertTrue(results)

    def test_feeling_statement_s(self):
        for mood in ['good', 'bad']:
            results = nostra.feeling_statement_s(mood)
            # print results
            self.assertTrue(results)

    def test_warning_s(self):
        for mood in ['good', 'bad']:
            results = nostra.warning_s(mood)
            # print results
            self.assertTrue(results)