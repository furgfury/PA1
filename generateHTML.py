from os import read, write
import random

# get file path for file that needs
# to be read
def getPath():
    return input("Input Path. Make sure file has underscores where you would like spaces.\
    e.g: TITLE RaNDoM_LetTErS\n")

# read the file and get all of
# the lines
def readFile(path):
    fileRead = open(path)
    filePrint = fileRead.read().splitlines()
    return filePrint

# separate file into objects from 
# left column and colors / details
# from the right colum
def separateFile(readableFile):
    objects = []
    parameters = []

    for x in range(len(readableFile)):
        objects.append(readableFile[x].split())
        objects[x][0] = objects[x][0].upper()
        parameters.append(objects[x][1])
        objects[x].remove(objects[x][1])
        
    return objects, parameters

def generateHTML(objects, parameters):
    sortedObjects = []

    sortedObjects = fillArray(sortedObjects)

    for x in objects:
        if x == ['TITLE']:
            sortedObjects[0] = parameters[objects.index(x)]
        elif x == ['AUTHORS']:
            sortedObjects[1] = parameters[objects.index(x)]
        elif x == ['BODY_BACKGROUND']:
            sortedObjects[2] = parameters[objects.index(x)]
        elif x == ['CELL_BACKGROUND1']:
            sortedObjects[3] = parameters[objects.index(x)]
        elif x == ['CELL_BACKGROUND2']:
            sortedObjects[4] = parameters[objects.index(x)]
        elif x == ['TABLE_BORDER_COLOR']:
            sortedObjects[5] = parameters[objects.index(x)]
        elif x == ['TABLE_BORDER_PX']:
            sortedObjects[6] = parameters[objects.index(x)]
        elif x == ['LETTERS']:
            sortedObjects[7] = parameters[objects.index(x)]
        elif x == ['IMAGES']:
            sortedObjects[7] = ""
        else:
            sortedObjects[8] += (" " + str(objects[objects.index(x)]).lower())
            sortedObjects[8] += (" " + str(parameters[objects.index(x)]).lower())
        print(sortedObjects[8])

    return sortedObjects

def fillArray(array):
    for x in range(9):
        array.append("")
    return array

def createFile(name):
    return open(name, "x")

def writeFile(file, element):
    file = open(file.name, "a")
    file.write(element)
    file.flush()

def wrap(tag, element):
    #TODO check if tag is image bc they don't have closing tag
    line = str(tag + element + tag[0:1] + "/" + tag[1:len(tag.split(">", 2))] + ">")
    return line

def fillHeader(file, elements):
    headRef = "<!DOCTYPE html><html><head><style>*{padding:0px;margin:0px;}body{height:100vh;width:100vw;display:flex;align-items:center;justify-content:center;background-color:"\
     + str(elements[2]) + ";}table{width:60vw;height:60vh;}\ntd{text-align:center;border:" + str(elements[6]) + "px solid " + str(elements[5]) +\
    ";}tr td{background-color:" + str(elements[3]) + ";}tr:nth-child(even)td:nth-child(odd),tr:nth-child(odd)td:nth-child(even){background-color:\\"\
     + str(elements[4]) + ";}</style><head><body>"
    file = open(file.name, "a")
    file.write(headRef)

def fillFile(file, elementList):
    cleanList = elementList[8].replace("'", " ").split(" ")
    print(str(cleanList) + "\n\n")
    i = 0;
    file = open(file.name, "a")
    for x in range(int(len(cleanList))):
        if(i < x):
            print(cleanList[i])
            i+=2;

def main():
    fullFile = readFile(getPath())
    leftColumn, rightColumn = separateFile(fullFile)
    outputFile = createFile("pa1.txt")
    sortedList = generateHTML(leftColumn, rightColumn)
    #fillHeader(outputFile, sortedList)
    fillFile(outputFile, sortedList)
    #outputFile.write(wrap("<h6>", "title"))

main()