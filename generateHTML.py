from os import read
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

# combine lines into one string
# to be parsed
    return filePrint

# separate file into objects from 
# left column and colors / details
# from the right colum
def separateFile(readableFile):
    objects = []
    parameters = []

    for x in range(len(readableFile)):
        objects.append(readableFile[x].upper().split())
        parameters.append(objects[x][1])
        objects[x].remove(objects[x][1])
        
    return objects, parameters

def generateHTML(objects, parameters):
    
    for x in objects:
        if x == ['TITLE']:
            print("title")
        elif x == ['AUTHORS']:
            print("authors")
        elif x == ['BODY_BACKGROUND']:
            print("body background")
        elif x == ['CELL_BACKGROUND1']:
            print("cell background 1")
        elif x == ['CELL_BACKGROUND2']:
            print("cell background 2")
        elif x == ['TABLE_BORDER_COLOR']:
            print("table border color")
        elif x == ['TABLE_BORDER_PX']:
            print("table border pixels")
        elif x == ['LETTERS']:
            print("letters")
        else:
            print("Unable to find " + str(x))

def writeFile():
    

def main():
    fullFile = readFile(getPath())
    leftColumn, rightColumn = separateFile(fullFile)
    #print(leftColumn)
    generateHTML(leftColumn, rightColumn)

main()