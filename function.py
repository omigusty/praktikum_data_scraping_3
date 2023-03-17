import os


def createDirectory(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)


def createNewFile(path):
    f = open(path, "w")
    f.write("")
    f.close()


def writeToFile(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def doesFileExist(path):
    return os.path.isfile(path)
