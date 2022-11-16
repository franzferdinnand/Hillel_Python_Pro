import requests
import functools
import psutil


def func_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        mem_before = process.memory_info().rss
        result = func(*args, **kwargs)
        mem_after = process.memory_info().rss
        print(f'memory usage is {format((mem_after - mem_before)/1024/1024, ".2f")} MB')

        return result

    return wrapper


@func_memory
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


if __name__ == '__main__':
    print(fetch_url('https://google.com'))
