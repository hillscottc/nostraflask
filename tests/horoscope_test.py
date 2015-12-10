from unittest import TestCase
from horoscope import horoscope, word_cache
import redis

redis_client = redis.Redis(
    host='localhost',
    port=6379)


class HoroscopeTest(TestCase):

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

