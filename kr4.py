def bin_search(li, element):
    low = 0
    high = len(li) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if li[mid] == element:
            return mid
        elif li[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1



