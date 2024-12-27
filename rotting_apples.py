from pprint import pprint as pp

def rotting(box, days):
    coordinates = []
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            if box[i][j] == "X":
                coordinates.append((i + 1, j + 1))

    for row, col in coordinates:
        for i in range(row - 1 - 1, row + 1):
            if i < 0:
                i = 0
            if i > len(box) - 1:
                i = len(box) - 1
            for j in range(col - 1 - 1, col + 1):
                if j < 0:
                    j = 0
                if j > len(box[0]) - 1:
                    j = len(box[0]) - 1
                box[i][j] = "X"

def rotting_apples():
    box_size = input("Enter the size of the box: ")
    rows = int(box_size.split("x")[0])
    cols = int(box_size.split("x")[1])
    coordinates = input("Еnter the coordinates of the rotten apples: ")
    rotten_apples = eval(coordinates)
    days = int(input("After how many days will you come back: "))

    box = [["O" for _ in range(cols)] for _ in range(rows)]
    for col, row in rotten_apples:
        box[col - 1][row - 1] = "X"

    for i in range(days // 3):
        rotting(box, days)
        
    for i in range(len(box)):
        print(box[i])

rotting_apples()