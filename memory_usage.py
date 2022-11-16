import requests
import functools
import psutil


def func_memory(func):
    def get_process_memory():
        process = psutil.Process()
        return process.memory_info().rss

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        mem_before = get_process_memory()
        result = func(*args, **kwargs)
        mem_after = get_process_memory()
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
