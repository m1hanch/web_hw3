import time
from multiprocessing import Pool, cpu_count
def factors(n:int):
    res = [i for i in range(1, int(n / 2) + 1) if n % i == 0]
    res.append(n)
    return res

def factorize_synch(*numbers):
    return [factors(number) for number in numbers]

def factorize_processes(*numbers):
    with Pool(cpu_count()) as p:
        res = p.map_async(factors, numbers)
        p.close()
        p.join()
        return res.get()


if __name__ == '__main__':
    start = time.time()
    a, b, c, d = factorize_synch(128, 255, 99999, 10651060)
    end = time.time()
    print(f'Synchron execution took {end - start} seconds')
    start = time.time()
    e, f, g, h = factorize_processes(128, 255, 99999, 10651060)
    end = time.time()
    print(f'Processes execution took {end - start} seconds')
    assert a == e == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == f == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == g == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == h == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]