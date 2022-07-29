from runTimeFunctions import *
from coordsManagement import *



#initial variables needed
# arr = [[5, 4, 3], 
#        [6, 2, 1], 
#        [1, 6, 3],
#        [1, 2, 3]]
arr = outputArray()


toBeVisited = []

#Node class for all datapoints
class Node():
    def __init__(self, height):
        self.longitude = 0.0
        self.latitude = 0.0
        self.height = height
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
    #start point
    arr[2][1].fullPathDistance=0

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


#finding all of the nodes that need to be visited
def __toBeVisited():
    for row in range(1, len(arr)-1):
        for column in range(1, len((arr[row])[1:len(arr[row])])):
            toBeVisited.append([row, column])


fillBox(arr)
__initRows()
__toBeVisited()

#just a thing that shows

checkSurrounding([2, 1], arr)

for row in range(1, len(arr)-1):
    for column in range(1, len((arr[row])[1:len(arr[row])])):
        if arr[row][column].fullPathDistance < 10:

            arr[row][column] = arr[row][column].fullPathDistance
        else: 
            arr[row][column] = 0
for i in arr:
    print(i)
