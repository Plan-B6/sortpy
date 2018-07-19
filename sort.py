import random


DATA_NUM = 50
DATA_MAX = 50


playback_list = []


def generate_dataset(num, repeat=False):
    assert num == DATA_NUM
    ds = []
    if repeat:
        for i in range(num):
            ds.append(random.randint(1, DATA_MAX))
    else:
        ds = [i + 1 for i in range(num)]
        random.shuffle(ds)
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


def bubble_sort(ds):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(ds)):
            if ds[i - 1] > ds[i]:
                ds[i], ds[i - 1] = ds[i - 1], ds[i]
                swapped = True
                playback_list.append(ds[:])
    return ds


def selection_sort(ds):
    for i in range(len(ds) - 1):
        min_index = i
        for j in range(i + 1, len(ds)):
            if ds[j] < ds[min_index]:
                min_index = j
        if min_index != i:
            ds[i], ds[min_index] = ds[min_index], ds[i]
            playback_list.append(ds[:])