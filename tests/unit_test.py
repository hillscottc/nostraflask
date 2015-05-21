from unittest import TestCase
from horoscope.horoscope import generate

class NostraUnitTest(TestCase):

    def test_generate(self):
        results = generate()
        print "helloo"
        print results
        # self.assertEqual(1, 2)

