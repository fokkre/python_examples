import os
import random

FOLDER = "data/"
Filename = os.listdir(FOLDER)

patientData = {}

"""
The hospital sends over a list of patients and their results as a single csv file. There are 569 unique records indicating:
1) ID number
2) Diagnosis (M = malignant, B = benign)
3) Mean Results
4) SE Results
5) Worst Results

Results each of the following values
a) radius (mean of distances from center to points on the perimeter)
b) texture (standard deviation of gray-scale values)
c) perimeter
d) area
e) smoothness (local variation in radius lengths)
f) compactness (perimeter^2 / area - 1.0)
g) concavity (severity of concave portions of the contour)
h) concave points (number of concave portions of the contour)
i) symmetry
j) fractal dimension ("coastline approximation" - 1)
"""

def get_results_by_id(request):

    for file in Filename:
        data = []
        with open (FOLDER + file) as csvfile:
            data = csvfile.readlines()
            column_titles = data[0]

            for line in range(1, len(data)):
                results = data[line].strip().split(',')
                id = results[0]
                results.pop(0)
                if id not in patientData:
                    patientData[id] = [results]
                patientData[id].append(results)

    return(column_titles, (patientData[request]))

def get_random_ids(record_request_count):

    for file in Filename:
        data = []
        with open (FOLDER + file) as csvfile:
            data = csvfile.readlines()

            for line in range(1, len(data)):
                results = data[line].strip().split(',')
                id = results[0]
                results.pop(0)
                if id not in patientData:
                    patientData[id] = [results]
                patientData[id].append(results)

    random_index = []
    random_records = []
    i = 0

    while i < record_request_count:
        random_index.append(random.randrange(1,570))
        i+=1

    for index in random_index:
        random_records.append(list(patientData.keys())[index])
    
    return(random_records)