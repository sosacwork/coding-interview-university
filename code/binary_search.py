def binary_search(array, target):
    low = 0
    high = len(array)

    while low < high:
        mid = low + (high - low) // 2
        print(mid)
        if array[mid] > target:
            high = mid
        else:
            low = mid + 1
    return low - 1


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(a, 2))
