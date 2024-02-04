"""
so the first person would want to go to the smallest node to avoid collision
and the second person would want to go to the next smallest node to avoid collision and so on
but we want to count these collisions, so we will get the input and check how many swaps do we need to sort the input and output the answer as the collision count
we will use merge sort as it has nlog(n) order
"""


def calculate_swaps(inp, temp, left, right):
    inv_count = 0
    mid = (left + right) // 2
    if left < right:
        inv_count += calculate_swaps(inp, temp, mid + 1, right)
        inv_count += calculate_swaps(inp, temp, left, mid)
        inv_count += merge(inp, temp, left, mid, right)
    return inv_count


def merge(arr, temp, left, mid, right):
    i, j, k, count = left, mid + 1, left, 0
    while j <= right and i <= mid:
        # merge two parts and count inversion if a[i] >= a[j]
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            temp[k] = arr[j]
            count += (mid - i + 1)
            j, k = j + 1, k + 1
    # one part is finished , finish the other part
    while j <= right:
        temp[k] = arr[j]
        j, k = j + 1, k + 1
    while i <= mid:
        temp[k] = arr[i]
        i, k = i + 1, k + 1
    # store the results
    for i in range(left, right + 1): arr[i] = temp[i]
    return count


n = int(input())
temp = [0] * n
inp = [int(x) for x in input().split()]
print(calculate_swaps(inp, temp, 0, n - 1))
