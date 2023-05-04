'''
Implement a function to perform a binary search on a sorted array of integers to find the index of a given integer.
'''

l = [4,7,32,45,67,68,72,75,88,92]


def binary_search(l, target):
    start = 0
    end = len(l)

    while start < end:
        mid = (start+end)//2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            start = mid + 1
        else:
            end = mid
    return -1


print(binary_search(l, 69))
