def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swap = False

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True

        if not swap:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)