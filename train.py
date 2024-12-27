#!/usr/bin/env python3

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

nums = fibonacci()

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
coordinates = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 8:
            coordinates.append((i, j))

# print(coordinates)

class Plane:
    def fly(self):
        print(self.sound)

class Boeing(Plane):
    def __init__(self, sound):
        self.sound = sound

# plane = Plane()
# boeing = Boeing("Meeeeow")
# boeing.fly()

def sort_sample(arr):
    for i in range(0, len(arr) - 1):
        idx_min = i
        for j in range(i + 1, len(arr)):
            if arr[idx_min] > arr[j]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]

l = [1, 0, 3, 4, 2, 10, 7]
sort_sample(l)
print(l)
