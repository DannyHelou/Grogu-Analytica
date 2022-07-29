import numpy as np

coordinates = open("testerCoords.txt", "r")

#finding the minimum latitude and longitude
mininmumLat = 99999999999999
minimumLong = 999999999999999

#creating a counter to count the number of rows and column we use to initialize our variable
latCounter = 0
longCounter = 0
repeatLat = ""
repeatLong = ""

#looping through the database of coordinates to find the number of the base instances
def loopCoords():
    for count, row in enumerate(coordinates):
        currentRowData = row.split(",")
        minimumLat = min(currentRowData[1], minimumLat)
        minimumLong = min(currentRowData[2], minimumLong)
        if count == 0:
            repeatLat = float(currentRowData[1])
            repeatLong = float(currentRowData[2])
            latCounter += 1
            longCounter += 1
        if repeatLat == float(currentRowData[1]):
            latCounter += 1
        if repeatLong == float(currentRowData[2]):
            longCounter += 1
    return(latCounter, longCounter)

#creating np array filled with 0s of shape equivelent to our outpetted values here
def instatiateArr(latSize, longSize):
    blueprintArr = np.zeros([latSize, longSize])
    print(blueprintArr)

#TODO: start filling in the blueprintArr with the desired coordinates
