import random

def binary_search(l, target, min = 0, max = None):
    if max == None: max = len(l) - 1
    if min > max: return -1
    mid = (min + max) // 2

    if l[mid] == target: return mid
    if l[mid] > target: return binary_search(l, target, min, mid-1)
    if l[mid] < target: return binary_search(l, target, mid+1, max)

sorted_list = [i for i in range(100)]
target = random.choice(sorted_list)
result = binary_search(sorted_list, target)
print(result) # some number other than -1
result = binary_search(sorted_list, 101)
print(result) # -1