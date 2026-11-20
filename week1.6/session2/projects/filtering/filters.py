import image

def blur(img):
    total = 0
    photo = Image.create(img.width, img.height, 0, img.max_value)
    for row in range(1, img.height - 1):
        for col in range(1, img.width - 1):
            region = [img.get(row - 1, col - 1), img.get(row - 1, col), img.get(row - 1, col + 1),
                      img.get(row, col - 1), img.get(row, col), img.get(row, col + 1),
                      img.get(row + 1, col - 1), img.get(row + 1, col), img.get(row - 1, col + 1)]
            for i in range(0, len(region)):
                total =+ region[i]
            avrg = total / 9
            photo.set(row, col, avrg)