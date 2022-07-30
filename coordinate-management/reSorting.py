
from numpy import greater
from utmtodeg import *
import sys
import os
sys.path.append("/Users/dhelou1/desktop/programming/groguanalytica/coordinates/saroojwadis/kmltocsv")

import kmltocsv

"""
imporing all the files that will be read through and fed into a singular file
"""
filesToOpen = [
"A1-1.txt",
"A1-2.txt",
"A1-3.txt",
"A1-4.txt",
"A1-5.txt",
"A1-6.txt",
"A1-7.txt",
"A4-1.txt",
"A4-2.txt",
"A4-3.txt",
"B1-2.txt",
"C-END.txt",
"c1.txt"
]


"""
Initializing all variables that may be used
"""
newFile = open("completeCoords.txt", "w")
wadiCoords = kmltocsv.main()

greaterData = []
data = []

"""
Append all data to greater data for later use, checking if coordinates are wadi coords
"""

for file in filesToOpen:
    data = []
    for count, i in enumerate(open( "/Users/dhelou1/Desktop/Programming/groguAnalytica/coordinates/points/" +file, "r")):
        coords = i.split(",")
        longlatcoords = unproject(40, "R", coords[1], coords[2])
    
        wadiAppendVal  = "0"
        
        #run through all of the wadi coords and check if close or not
        for wadi in wadiCoords: 
            if (((wadi[0] - longlatcoords[0])**2 + (wadi[1] - longlatcoords[1])**2)**0.5 < 0.000314921):
                print("HERE", count)
                wadiAppendVal = " 1"
                continue
        data.append([str(count), str(longlatcoords[1]),str(longlatcoords[0]),str(coords[3]), wadiAppendVal])
    greaterData.append(data)

"""
Write everything to completeCoords.txt
"""

for i, smallerData in enumerate(greaterData):
    for x in smallerData:

        newFile.write(",".join(x) + "\n")
