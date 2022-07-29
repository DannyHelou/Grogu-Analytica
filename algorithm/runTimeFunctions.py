#functions

#fill the numbers in a 2d array with -1 values
def fillBox(arr):
    for i in arr:
        i.append(-1)
        i.insert(0, -1)
    arr.append([-1] * len(arr[0]))
    arr.insert(0, ([-1] * len(arr[0])))

#checking the surround possible coordinates
def checkSurrounding(coords, arr):
    currentSeen = coords
    #LEFT
    if(isInt(arr[currentSeen[0]][currentSeen[1]].LEFT) == False):
        if((arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].LEFT.height)) < arr[currentSeen[0]][currentSeen[1]].LEFT.fullPathDistance):
            arr[currentSeen[0]][currentSeen[1]].LEFT.prevNode = arr[currentSeen[0]][currentSeen[1]]
            arr[currentSeen[0]][currentSeen[1]].LEFT.fullPathDistance = arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].LEFT.height)
            checkSurrounding([currentSeen[0], currentSeen[1]-1], arr)
    #RIGHT
    if(isInt(arr[currentSeen[0]][currentSeen[1]].RIGHT) == False):
        if((arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].RIGHT.height)) < arr[currentSeen[0]][currentSeen[1]].RIGHT.fullPathDistance):
            arr[currentSeen[0]][currentSeen[1]].RIGHT.prevNode = arr[currentSeen[0]][currentSeen[1]]
            arr[currentSeen[0]][currentSeen[1]].RIGHT.fullPathDistance = arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height -arr[currentSeen[0]][currentSeen[1]].RIGHT.height)
            checkSurrounding([currentSeen[0], currentSeen[1]+1], arr)
    #UP
    if(isInt(arr[currentSeen[0]][currentSeen[1]].UP) == False):
        if((arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].UP.height)) < arr[currentSeen[0]][currentSeen[1]].UP.fullPathDistance):
            arr[currentSeen[0]][currentSeen[1]].UP.prevNode = arr[currentSeen[0]][currentSeen[1]]
            arr[currentSeen[0]][currentSeen[1]].UP.fullPathDistance = arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].UP.height)
            checkSurrounding([currentSeen[0]-1, currentSeen[1]], arr)
    #DOWN
    if(isInt(arr[currentSeen[0]][currentSeen[1]].DOWN) == False):
        if((arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].DOWN.height)) < arr[currentSeen[0]][currentSeen[1]].DOWN.fullPathDistance):
            arr[currentSeen[0]][currentSeen[1]].DOWN.prevNode = arr[currentSeen[0]][currentSeen[1]]
            arr[currentSeen[0]][currentSeen[1]].DOWN.fullPathDistance = arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height -arr[currentSeen[0]][currentSeen[1]].DOWN.height)
            checkSurrounding([currentSeen[0]+1, currentSeen[1]], arr)

    #LEFTUP
    if(isInt(arr[currentSeen[0]][currentSeen[1]].LEFTUP) == False):
        if((arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].LEFTUP.height)) < arr[currentSeen[0]][currentSeen[1]].LEFTUP.fullPathDistance):
            arr[currentSeen[0]][currentSeen[1]].LEFTUP.prevNode = arr[currentSeen[0]][currentSeen[1]]
            arr[currentSeen[0]][currentSeen[1]].LEFTUP.fullPathDistance = arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].LEFTUP.height)
            checkSurrounding([currentSeen[0]-1, currentSeen[1]-1], arr)
    #RIGHTUP
    if(isInt(arr[currentSeen[0]][currentSeen[1]].RIGHTUP) == False):
        if((arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].RIGHTUP.height)) < arr[currentSeen[0]][currentSeen[1]].RIGHTUP.fullPathDistance):
            arr[currentSeen[0]][currentSeen[1]].RIGHTUP.prevNode = arr[currentSeen[0]][currentSeen[1]]
            arr[currentSeen[0]][currentSeen[1]].RIGHTUP.fullPathDistance = arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height -arr[currentSeen[0]][currentSeen[1]].RIGHTUP.height)
            checkSurrounding([currentSeen[0]-1, currentSeen[1]+1], arr)
    #LEFTDOWN
    if(isInt(arr[currentSeen[0]][currentSeen[1]].LEFTDOWN) == False):
        if((arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].LEFTDOWN.height)) < arr[currentSeen[0]][currentSeen[1]].LEFTDOWN.fullPathDistance):
            arr[currentSeen[0]][currentSeen[1]].LEFTDOWN.prevNode = arr[currentSeen[0]][currentSeen[1]]
            arr[currentSeen[0]][currentSeen[1]].LEFTDOWN.fullPathDistance = arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].LEFTDOWN.height)
            checkSurrounding([currentSeen[0]+1, currentSeen[1]-1], arr)
    #RIGHTDOWN
    if(isInt(arr[currentSeen[0]][currentSeen[1]].RIGHTDOWN) == False):
        if((arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height - arr[currentSeen[0]][currentSeen[1]].RIGHTDOWN.height)) < arr[currentSeen[0]][currentSeen[1]].RIGHTDOWN.fullPathDistance):
            arr[currentSeen[0]][currentSeen[1]].RIGHTDOWN.prevNode = arr[currentSeen[0]][currentSeen[1]]
            arr[currentSeen[0]][currentSeen[1]].RIGHTDOWN.fullPathDistance = arr[currentSeen[0]][currentSeen[1]].fullPathDistance + abs(arr[currentSeen[0]][currentSeen[1]].height -arr[currentSeen[0]][currentSeen[1]].RIGHTDOWN.height)
            checkSurrounding([currentSeen[0]+1, currentSeen[1]+1], arr)
    
    
    
#checking if a value is an interger or not
def isInt(val):
    try:
        int(val)
        return(True)
    except:
        return(False)
currentCoords = [1, 1]

