def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min = i

        for j in range(i+1, n):
            if (arr[j] < arr[min]):
                min = j
            
        if (min != i):
            arr[min], arr[i] = arr[i], arr[min]

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print(arr)