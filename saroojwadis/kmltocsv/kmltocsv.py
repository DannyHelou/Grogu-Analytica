"""
imporing all the files that will be read through and fed into a singular array output
"""
filesToProcess = [
"47.txt",
"46.txt",
"48.txt",
"49.txt",
"50.txt",
"52.txt",
"51.txt",
"53.txt",
"54.txt",
"55.txt",
"56.txt",
"58.txt",
"57.txt",
"59.txt",
"61.txt",
"60.txt",
"62.txt",
"63.txt",
"64.txt",
"65.txt",
"66.txt",
"67.txt",
"68.txt",
"69.txt",
"70.txt",
"71.txt",
"72.txt",
"73.txt",
"74.txt",
"75.txt",
"76.txt",
"77.txt",
"78.txt",
"79.txt",
"80.txt",
"81.txt",
"82.txt",
"83.txt",
"84.txt",
"85.txt",
"86.txt",
"6.txt",
"7.txt",
"8.txt",
"9.txt",
"10.txt",
"11.txt",
'12.txt',
"13.txt",
"14.txt",
"15.txt",
"16.txt",
"17.txt",
"18.txt",
"19.txt",
"20.txt",
"21.txt",
"22.txt",
"23.txt",
"24.txt",
"25.txt",
"26.txt",
"27.txt",
"28.txt",
"29.txt",
"30.txt",
"31.txt",
"32.txt",
"33.txt",
"34.txt",
"35.txt",
"36.txt",
"37.txt",
"38.txt",
"39.txt",
"40.txt",
"41.txt",
"42.txt",
"43.txt",
"44.txt",
"45.txt",
"87.txt"]

from bs4 import BeautifulSoup
import csv
import numpy as np

"""
Main function run when called on <-- outputs array with all coordinates that are inside a wadi
"""

def main():
    allWadiCoords = []

    for file in filesToProcess:
        txtfile = open("/Users/dhelou1/Desktop/Programming/groguAnalytica/coordinates/saroojwadis/kml/" + file)
        for counter, i in enumerate(txtfile):
            if counter == 32:
                #base operator array

                baseOperator = i.split(" ")

                #checking the first coord of the wadi
                val = list(map(float, baseOperator[0].split(",")[:2])) 

                #checking the last coord of the wadi
                try:
                    val2 = list(map(float, baseOperator[-1].split(",")[:2]))
                    allWadiCoords.append(val2)
                except:
                    pass

                #checking the middle-most coord of the wadi
                try:
                    middleCoord = int(round(len(baseOperator)/2))
                    val2 = list(map(float, baseOperator[middleCoord].split(",")[:2]))
                    allWadiCoords.append(val2)
                except:
                    pass

                allWadiCoords.append(val)
    return(allWadiCoords)
main()
