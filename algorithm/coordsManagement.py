
#Initializing the data that file initializingInput uses to conduct their fiel experiments
def rawData(txtFile):
    
    seenLat = {}
    seenLong = {}
    completeData = []
    longChange = 0
    latChange = 0
    minLong = 99999999999999999999999999999999999999999999999999999
    minLat = 9999999999999999999999999999999999999999999999999
    maxLong = 0
    maxLat = 0
    currLat = 0
    currLong = 0

    for line in txtFile:
        currLine = line.split(",")
        if seenLat.get(currLine[1]) == None:
            seenLat[currLine[1]] = seenLat.get(currLine[1], 0)
            latChange += 1
        if seenLong.get(currLine[2]) == None:
            seenLong[currLine[2]] = seenLong.get(currLine[2], 0)
            longChange += 1

        currLat = currLine[1]
        currLong = currLine[2]
        minLong = min(float(minLong), float(currLong))
        minLat = min(float(minLat), float(currLat))
        maxLong = max(float(maxLong), float(currLong))
        maxLat = max(float(maxLat), float(currLat))
        completeData.append([currLat, currLong, currLine[3]])
    return(latChange, longChange, completeData, minLat, minLong, maxLat, maxLong)

    
def outputData():
    #take the final path data of the file, convert into into a string of (longitude, latitude, height) and output the file with comma deliteted format/txt  
    pass
