import random

# get file path for file that needs
# to be read
def getPath():
    return input("Input Path. Make sure file has underscores where you would like spaces.\
    e.g: TITLE RaNDoM_LetTErS\n")

# read the file and read all of
# the lines
def readFile(path):
    fileFinal = ""
    fileRead = open(path)
    filePrint = fileRead.readlines()

# combine lines into one string
# to be parsed
    return fileFinal.join(filePrint)

# separate file into objects from 
# left column and colors / details
# from the right column
def separateFile(readableFile):
    splitList = readableFile.split()
    objects = []
    parameters = []
    i = 0;

# split file into left and right columns
    for x in splitList:
        if(i % 2 == 0):
            objects.append(x)
        else:
            parameters.append(x)
        i+=1
    
    return objects, parameters

def organizeColors(leftColumn):
# expected contents of file
    sortRef = ["body_background", "cell_background1", "cell_background2", "table_border_color"
    , "table_border_px", "authors", "title", "letters", "images"]

# turn everything in file lowercase in order
# to make sure there is no issue with any difference
# in case
    for x in range(len(leftColumn)):
        leftColumn[x] = leftColumn[x].lower()

    print(leftColumn)
# go through the eight expected attributes and sort them
# in a certain order so the program can generate the page
# no matter what order the user inputs
    for x in range(len(leftColumn)):
        if(x <= 7):
            if(leftColumn.index(sortRef[x]) + 1):
                print("found " + str(leftColumn[x]))
            else:
                print("could not find " + str(leftColumn[x]))
        else:
            print("There are more parameters than can be generated")
            break

def getIndex(input):
    print(input)

def main():
    fullFile = readFile(getPath())
    leftColumn, rightColumn = separateFile(fullFile)
    organizeColors(leftColumn)

main()