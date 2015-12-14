import redis

redis_client = redis.Redis(
    host='localhost',
    port=6379)


def cache_words(word_dict):

    for key in word_dict.keys():
        # print "Caching", key, word_dict[key]
        redis_client.set(key, word_dict[key])