from unittest import TestCase
from horoscope import word_cache, word_data
import redis

redis_client = redis.Redis(
    host='localhost',
    port=6379)


class CacheTest(TestCase):

    def setUp(self):
        print

    def test_default_word_data(self):
        """Cache and retrieve the default data"""
        # Call function to cache word data
        word_cache.cache_words(word_data.words)

        # read data back from cache
        for key in word_data.words.keys():
            value = redis_client.get(key)
            # print "Cache got", key, value
            self.assertIsNotNone(value)

    def test_word_data(self):
        """Cache and retrieve some dummy data"""
        test_words = {
            "familiar people": [
                "your mother",
                "your father",
                "your closest friend",
                "a family member"
            ]
        }

        # Call function to cache word data
        word_cache.cache_words(test_words)

        # read data back from cache
        for key in test_words.keys():
            value = redis_client.get(key)
            # print "Cache got", key, value
            self.assertIsNotNone(value)

