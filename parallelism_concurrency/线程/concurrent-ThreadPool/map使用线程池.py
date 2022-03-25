import concurrent.futures
import requests
import threading
import time


def download_one(url):
    print(url)
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites, sites2):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites, sites2)



def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
    ]
    sites2 = [1, 2, 3]
    start_time = time.perf_counter()
    download_all(sites, sites2)
    end_time = time.perf_counter()
    time.sleep(5)
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()

## 输出
# Read 151021 from https://en.wikipedia.org/wiki/Portal:Mathematics
# Read 129886 from https://en.wikipedia.org/wiki/Portal:Arts
# Read 107637 from https://en.wikipedia.org/wiki/Portal:Biography
# Read 224118 from https://en.wikipedia.org/wiki/Portal:Society
# Read 184343 from https://en.wikipedia.org/wiki/Portal:History
# Read 167923 from https://en.wikipedia.org/wiki/Portal:Geography
# Read 157811 from https://en.wikipedia.org/wiki/Portal:Technology
# Read 91533 from https://en.wikipedia.org/wiki/Portal:Science
# Read 321352 from https://en.wikipedia.org/wiki/Computer_science
# Read 391905 from https://en.wikipedia.org/wiki/Python_(programming_language)
# Read 180298 from https://en.wikipedia.org/wiki/Node.js
# Read 56765 from https://en.wikipedia.org/wiki/The_C_Programming_Language
# Read 468461 from https://en.wikipedia.org/wiki/PHP
# Read 321417 from https://en.wikipedia.org/wiki/Java_(programming_language)
# Read 324039 from https://en.wikipedia.org/wiki/Go_(programming_language)
# Download 15 sites in 0.19936635800002023 seconds
