

def insertionSort(arr):
    for i in range(len(arr)):
        currentItem = arr[i]
        j = i - 1

        while j >= 0 and currentItem < arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = currentItem

    return arr

print(insertionSort([3, 5, 6, 1, 12, 120, 60]))