import functools
import requests
from collections import OrderedDict


def cache(max_limit=5):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                if cache_key in counter:
                    counter[cache_key] += 1
                return deco._cache[cache_key]

            result = f(*args, **kwargs)

            if len(deco._cache) >= max_limit:
                min_key = min(counter, key=counter.get)
                deco._cache.pop(min_key)
                counter.pop(min_key)

            deco._cache[cache_key] = result
            counter[cache_key] = 1
            return result

        deco._cache = OrderedDict()
        counter = {}
        return deco

    return internal


@cache(3)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


if __name__ == '__main__':
    print(fetch_url('https://google.com'))
    print(fetch_url('https://ithillel.ua'))
    print(fetch_url('https://google.com'))
    print(fetch_url('https://google.com'))
    print(fetch_url('https://ithillel.ua'))
    print(fetch_url('https://lms.ithillel.ua'))
    print(fetch_url('https://github.com'))
    print(fetch_url('https://github.com'))
    print(fetch_url('https://github.com'))
    print(fetch_url('https://github.com'))
    print(fetch_url('https://lms.ithillel.ua'))
