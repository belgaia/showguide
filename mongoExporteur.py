__author__ = 'Agile Developers'
import os
import subprocess
import mongodbConnector

def exportCollection(showName, targetDir):

    # export file will be named after the show (with lower cases, without any spaces)
    # naming convention also for collections
    collectionName = createCollectionNameFromShowName(showName)

    filePath = targetDir + "/" + collectionName + ".csv"

    os.chdir("C:/Program Files/mongodb/bin/")
    mongoexportCommand = "mongoexport --db showguide --collection " + collectionName + " --csv " \
                             "--fields _id,name,episode_name_de,episode_name_en,general_episode_number,dvd_number,season,dvd_episode_number,director,identifier,content " \
                             "--out " + filePath

    subprocess.call(mongoexportCommand)

    return filePath


def exportCollections(showNames, targetDir):

    for show in showNames:
        exportCollection(show, targetDir)

def exportAllCollections(targetDir):

    # get all collections from the overview
    showList = mongodbConnector.getAllSeries()

    exportList = []

    for showName in showList:

        print("Show: " + showName)
        collectionName = createCollectionNameFromShowName(showName)
        exportList.append(showName)

    exportCollections(exportList, targetDir)


def createCollectionNameFromShowName(showName) :

    collectionName = showName.lower()
    collectionName = collectionName.replace(" ", "")

    return collectionName

