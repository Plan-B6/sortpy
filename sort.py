import random


DATA_NUM = 50
DATA_MAX = 50


playback_list = []


def generate_dataset(num, repeat=False):
    assert num == DATA_NUM
    if repeat:
        ds = [random.randint(1, DATA_MAX) for i in range(num)]
    else:
        ds = [i + 1 for i in range(num)]
        random.shuffle(ds)
    return ds


def swap(left, right, plist, ds):
    if ds[left] > ds[right]:
        ds[left], ds[right] = ds[right], ds[left]
        plist.append(ds[:])
        return True
    return False


def bubble_sort(ds):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(ds)):
            if swap(i - 1, i, playback_list, ds):
                swapped = True
    return ds


def cocktail_sort_up(ds):
    swapped = False
    for i in range(len(ds) - 1):
        if swap(i, i + 1, playback_list, ds):
            swapped = True
    return swapped


def cocktail_sort_down(ds):
    swapped = False
    for i in range(len(ds) - 2, -1, -1):
        if swap(i, i + 1, playback_list, ds):
            swapped = True
    return swapped


def cocktail_sort(ds):
    swapped = cocktail_sort_up(ds)
    first_swap = True
    while swapped:
        if not first_swap:
            swapped = cocktail_sort_up(ds)
        first_swap = False
        swapped = cocktail_sort_down(ds)
    return ds


def comb_sort(ds):
    gap = len(ds)
    shrink = 1.3
    swapped = True
    while swapped:
        gap = int(gap // shrink)
        if gap <= 1:
            swapped = False
        else:
            swapped = True
        i = 0
        while i + gap < len(ds):
            if swap(i, i + gap, playback_list, ds):
                swapped = True
            i += 1
    return ds


def odd_even_sort(ds):
    swapped = True
    while swapped:
        swapped = False
        # Swap odd indexes
        for i in range(1, len(ds) - 1, 2):
            if swap(i, i + 1, playback_list, ds):
                swapped = True
        # Swap even indexes
        for i in range(0, len(ds) - 1, 2):
            if swap(i, i + 1, playback_list, ds):
                swapped = True
    return ds


def insertion_sort(ds):
    i = 1
    while i < len(ds):
        j = i
        while j > 0 and ds[j - 1] > ds[j]:
            swap(j - 1, j, playback_list, ds)
            j -= 1
        i += 1
    return ds


def shell_sort(ds):
    # Ciura's gap sequence
    gaps = [301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        if gap >= DATA_NUM:
            continue
        for i in range(gap, len(ds)):
            dummy = ds[i]
            j = i
            # Sort with gap
            while j >= gap and ds[j - gap] > dummy:
                ds[j] = ds[j - gap]
                playback_list.append(ds[:])
                j -= gap
            ds[j] = dummy
            playback_list.append(ds[:])
    return ds


def gnome_sort(ds):
    i = 0
    while i < len(ds):
        if i == 0 or ds[i] >= ds[i - 1]:
            i += 1
        else:
            ds[i], ds[i - 1] = ds[i - 1], ds[i]
            playback_list.append(ds[:])
            i -= 1
    return ds


def merge_list(ds, left, mid, right):
    l_num = mid - left + 1
    r_num = right - mid

    temp_left = [0] * l_num
    temp_right = [0] * r_num

    for i in range(l_num):
        temp_left[i] = ds[left + i]
    for i in range(r_num):
        temp_right[i] = ds[mid + 1 + i]

    # Place elements back into base list
    i, j, k = 0, 0, left
    while i < l_num and j < r_num:
        if temp_left[i] <= temp_right[j]:
            ds[k] = temp_left[i]
            i += 1
        else:
            ds[k] = temp_right[j]
            j += 1
        k += 1
        playback_list.append(ds[:])

    # Add outstanding elements
    while i < l_num:
        ds[k] = temp_left[i]
        playback_list.append(ds[:])
        i += 1
        k += 1
    while j < r_num:
        ds[k] = temp_right[j]
        playback_list.append(ds[:])
        j += 1
        k += 1


def merge_sort(ds, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(ds, left, mid)
        merge_sort(ds, mid + 1, right)
        merge_list(ds, left, mid, right)
    return ds


def quick_partition(ds, low, high):
    pivot = ds[high]
    i = low - 1
    for j in range(low, high):
        if ds[j] < pivot:
            i += 1
            ds[i], ds[j] = ds[j], ds[i]
            playback_list.append(ds[:])
    ds[i + 1], ds[high] = ds[high], ds[i + 1]
    playback_list.append(ds[:])
    return i + 1


def quick_sort(ds, low, high):
    if low < high:
        p = quick_partition(ds, low, high)
        quick_sort(ds, low, p - 1)
        quick_sort(ds, p + 1, high)
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
    return ds


def stooge_sort(ds, left, right):
    swap(left, right, playback_list, ds)
    if right - left + 1 > 2:
        partition = (right - left + 1) // 3
        stooge_sort(ds, left, right - partition)
        stooge_sort(ds, left + partition, right)
        stooge_sort(ds, left, right - partition)
    return ds
