def sort(arr, t):
    for i in range(1, len(arr)):
        tempVal = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > tempVal:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = tempVal
    return t