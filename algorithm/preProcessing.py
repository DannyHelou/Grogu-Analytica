from turtle import clear
from runTimeFunctions import *
import initializingInput as initin
import coordsManagement



#initial variables needed
# arr = [[5, 4, 3], 
#        [6, 2, 1], 
#        [1, 7, 3],
#        [2, 2, 3]]
txtFile = open("testerCoords.txt", "r")
arr = initin.initializeArray(*coordsManagement.rawData(txtFile))


toBeVisited = []

#Node class for all datapoints
class Node():
    def __init__(self, dataInput):
        #should be input parameters
        if isInt(dataInput):
            self.height = dataInput
        else:
            self.longitude = dataInput[1]
            self.latitude = dataInput[0]
            self.height = float(dataInput[2])
        
        self.fullPathDistance = 9999999999
        self.prevNode = None
        self.UP = None
        self.DOWN = None
        self.LEFT = None
        self.RIGHT = None
        self.LEFTUP = None
        self.RIGHTUP = None
        self.LEFTDOWN = None
        self.RIGHTDOWN = None

#inits all the nodes that need to be visited 
def __initRows():
    for row in range(1, len(arr)-1):
        for column in range(1, len((arr[row])[1:len(arr[row])])):
            arr[row][column] = Node(arr[row][column])
    
    

    for row in range(1, len(arr)-1):
        for column in range(1, len((arr[row])[1:len(arr[row])])):
            arr[row][column].UP = arr[row-1][column]
            arr[row][column].DOWN = arr[row+1][column]
            arr[row][column].LEFT = arr[row][column-1]
            arr[row][column].RIGHT = arr[row][column+1]
            arr[row][column].LEFTUP = arr[row-1][column-1]
            arr[row][column].RIGHTUP = arr[row-1][column+1]
            arr[row][column].LEFTDOWN = arr[row+1][column-1]
            arr[row][column].RIGHTDOWN = arr[row+1][column+1]
            arr[row][column].longitude = 0
            arr[row][column].latitude = 0


#finding all of the nodes that need to be visited(REDUNDANT, DONT NEED) 
def __toBeVisited():
    for row in range(1, len(arr)-1):
        for column in range(1, len((arr[row])[1:len(arr[row])])):
            toBeVisited.append([row, column])



if __name__ == '__main__':
    #setting up all prereqs
    fillBox(arr)
    __initRows()
    __toBeVisited() #<- dont really need this was just for testing purposes
    
    #initializing and running the algorithm for our start point
    arr[1][2].fullPathDistance = 0
    checkSurrounding([1, 2], arr)


    #Printing the visuals for the output
    for row in range(1, len(arr)-1):
        for column in range(1, len((arr[row])[1:len(arr[row])])):
            arr[row][column] = arr[row][column].fullPathDistance
    for i in arr:
        print(i)

