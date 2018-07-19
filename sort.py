import random


DATA_NUM = 50
DATA_MAX = 50


playback_list = []


def generate_dataset(num):
    assert num == DATA_NUM
    ds = []
    for i in range(num):
        ds.append(random.randint(1, DATA_MAX))
    return ds


def insertion_sort(ds):
    i = 1
    while i < len(ds):
        j = i
        while j > 0 and ds[j - 1] > ds[j]:
            ds[j], ds[j - 1] = ds[j - 1], ds[j]
            j -= 1
            playback_list.append(ds[:])
        i += 1
    return ds