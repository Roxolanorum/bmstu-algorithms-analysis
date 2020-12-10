def lsearch(arr, key):
    for i in arr:
        if i == key:
            return True
    return False


def bsearch_wrap(arr, key):
    arr.sort()
    return bsearch(arr, key, 0, len(arr))


def bsearch(arr, key, l, r):
    left = l
    right = r

    mid = (left+right) // 2
    while left < right:
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left+right) // 2
    return arr[mid] == key


def fsearch_wrap(arr, key):
    freq = [0] * 34
    for s in arr:
        freq[ord(s[0]) - ord('А')] += 1

    arr.sort()
    l = sum(freq[:ord(key[0]) - ord('А')])
    r = l + freq[ord(key[0]) - ord('А')]

    return bsearch(arr, key, l, r)
