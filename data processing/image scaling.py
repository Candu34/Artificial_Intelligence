import numpy as np

# Datele sunt prelucrate si pastrate in fisier txt,
# lipsite de antetul setului de date original,
# matrici de 32x32 urmata de valoarea in zecimal al
# cifrei afisate de matrice

myList = []
list_of_values = []
index_of_image = 3  # incepand cu 0 - pana la numarul de matrici din data set

f = open(r"C:\Users\ionca\OneDrive\Desktop\digit data set.txt")
for line in f:
    row = line.split(',')
    if len(row[0]) > 3:
        for i in range(32):
            myList.append(int(row[0][i]))
    else:
        list_of_values.append(int(row[0]))

np_image = np.array(myList)
np_image = np_image.reshape(-1, 32)

print(list_of_values)


def scaling(img):
    new_img = np.array([])

    for i in range(0, 32, 2):
        for j in range(0, 32, 2):
            new_img = np.append(new_img, int(get_pixel(img[i: i + 2, j: j + 2])))

    new_img = new_img.reshape(16, 16)
    return new_img


def get_pixel(arr):
    # arr = 2x2
    n = np.sum(arr == 1)
    if n > 2:
        return 1
    return 0


n = index_of_image * 32
m = index_of_image * 32

array = scaling(np_image[0 + n:32 + m][0:32])
print(array)
