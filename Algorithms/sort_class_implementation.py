class Sort():
    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            pivot = arr[i]

            j = i - 1
            while j >= 0 and pivot < arr[j]:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = pivot

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr) - 1):
            pivot = i

            for j in range(i + 1, len(arr)):
                if arr[j] < arr[pivot]:
                    pivot = j

            if pivot != i:
                arr[pivot], arr[i] = arr[i], arr[pivot]

    @staticmethod
    def bubble_sort(arr):
        for i in range(len(arr) - 1):
            swap = False

            for j in range(len(arr) - i - 1):
                if arr[j+1] < arr[j]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    swap = True

            if not swap:
                break

    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            middle = len(arr) // 2
            L = arr[:middle]
            R = arr[middle:]

            Sort.merge_sort(L)
            Sort.merge_sort(R)

            i, j, k = 0, 0, 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1

            while i < len(L):
                arr[k] = L[i]
                i+=1
                k+=1

            while j < len(R):
                arr[k] = R[j]
                j+=1
                k+=1

    @staticmethod
    def _partition(arr, low, high):
        i = low
        for j in range(low, high):
            if arr[j] < arr[high]:
                arr[j], arr[i] = arr[i], arr[j]
                i+=1

        arr[i], arr[high] = arr[high], arr[i]
        return i

    @staticmethod
    def quick_sort(arr, low, high):
        if low < high:
            pivot = Sort._partition(arr, low, high)

            Sort.quick_sort(arr, low, pivot - 1)
            Sort.quick_sort(arr, pivot + 1, high)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    # Sort.insertion_sort(arr)
    # Sort.selection_sort(arr)
    # Sort.bubble_sort(arr)
    # Sort.merge_sort(arr)
    Sort.quick_sort(arr, 0, len(arr) - 1)
    print(arr)