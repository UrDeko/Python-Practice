image = [
   [0, 0, 0, 1, 0, 0, 0],
   [0, 0, 1, 1, 1, 0, 0],
   [0, 1, 1, 1, 1, 1, 0],
   [1, 1, 1, 1, 1, 1, 1],
   [0, 0, 0, 1, 0, 0, 0],
   [0, 0, 0, 1, 0, 0, 0]
]

def display_image(image):
    result = []

    for row in image:
        row_content = []

        for pixel in row:
            if pixel == 0:
                row_content.append(" ")
            elif pixel == 1:
                row_content.append("*")
            
        result.append("".join(row_content))

    return "\n".join(result)

print(display_image(image=image))