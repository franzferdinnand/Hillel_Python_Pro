import requests
import functools
import tracemalloc
from pprint import pp


def func_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        mem_size, mem_peak = tracemalloc.get_traced_memory()
        tracemalloc.reset_peak()

        pp(f'memory usage is size={mem_size} peak={mem_peak}')

        return result

    return wrapper


@func_memory
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


if __name__ == '__main__':
    print(fetch_url('https://google.com'))
