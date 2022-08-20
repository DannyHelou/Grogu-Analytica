"""
    TODO:
    
"""    

import numpy as np
import coordsManagement

PATH = ""

txtFile = open("testerCoords.txt", "r")

#intializing the array that is inputted into the preProcessing file
def initializeArray(numLat, numLong, data, minLat, minLong, maxLat, maxLong):
    
    incrementLat, incrementLong = findIncrements(data)
    formatArr = []

    #creating the initial format array
    for i in range(numLat):
        currArr = []
        for x in range(numLong):
            currArr.append(-1)
        formatArr.append(currArr)
        
    #inputting all of the coordinates into the formatarr
    for node in data:
        x, y, height = findingPos(node, minLat, minLong, incrementLong, incrementLat)
        formatArr[int(x)][int(y)] = [node[0], node[1], node[2]]

    #outputting the formatarr to the algorithm file to then find optimal pathing
    return(formatArr)

#finding the increment in each change in the longitude and latitude
def findIncrements(data):
    #calculating the increment diffrence
    incrementLong = 0
    incrementLat = 0
    currLat = data[0][0]
    currLong = data[0][1]
    for i in data:
        if currLat != i[0]:
            incrementLat = abs(float(currLat) - float(i[0]))
        currLat = i[0]
    for i in data:
        if currLong != i[1]:
            incrementLong = abs(float(currLong) - float(i[1]))
        currLong = i[1]
    return(incrementLat, incrementLong)

#finding the index in the formatArr of a given coordinate
def findingPos(data, minLat, minLong, incrementLong, incrementLat):
    height = data[2]
    lat = float(data[0])
    long = float(data[1])
    if incrementLat != 0:
        row = (lat - minLat)//incrementLat
    else:
        row = 0
    
    if incrementLong != 0:
        column = (long - minLong)//incrementLong
    else:
        column = 0
    return(row, column, height)




"""
Assumptions Made:
1. Data given is ordered, x2-x1 = x3-x2 etc
2. All of the coordinates are connected by some way, ie there are no gaps in space between points

"""
