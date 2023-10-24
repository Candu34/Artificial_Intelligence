import numpy as np
import csv

myList = []

with open(r"C:\Users\ionca\Inteligenta artificiala\Data\iris.data") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if len(row) == 5:
            myList.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])

npArray = np.array(myList)
columns = npArray.shape[1]
rows = npArray.shape[0]
col_min = np.array([])
col_max = np.array([])
col_med = np.array([])
col_avg = np.array([])
norm_array = np.array([])

########################### calculul minimului per coloane ###########################
for i in range(columns):
    col_min = np.append(col_min, np.min(npArray[:, i]))

print("minimul per coloana: ", col_min)

########################### calculul maximului per coloane ###########################
for i in range(columns):
    col_max = np.append(col_max, np.max(npArray[:, i]))

print("maximul per coloana: ", col_max)

########################### calculul medianei per coloane ############################
for i in range(columns):
    col_med = np.append(col_med, np.median(npArray[:, i]))

print("mediana per coloana: ", col_med)

########################### calculul mediei per coloane #############################
for i in range(columns):
    col_avg = np.append(col_avg, np.average(npArray[:, i]))

print("media per coloana: ", col_avg)

########################### normalizarea datelor ####################################
for i in range(columns):
    norm_array = np.append(norm_array, npArray[:, i] - min(npArray[:, i])) / (max(npArray[:, i]) -
                                                                              min(npArray[:, i]))

norm_array = norm_array.reshape(-1, 4)


########################## calculul datelor ponderate ###############################
pond_array = np.add(np.add(np.add(norm_array[:, 0] * 0.2, norm_array[:, 1] * 1.1), norm_array[:, 2] * -0.9),
                    norm_array[:, 3] * 1)
pond_array = pond_array.reshape(-1, 1)

########################## adaugarea ca coloana a datelor ponderate ##################
norm_array = np.append(norm_array, pond_array, 1)
