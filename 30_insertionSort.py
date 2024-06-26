def insertionSort(arr,n):
    for i in range(1, n):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

arr = [22,11,3,65,1]

n = len(arr)

insertionSort(arr,n)

print(arr)

# First element is always sorted