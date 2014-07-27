__author__ = 'Agile Developers'
import os
import subprocess

def exportCollection(showName, targetDir):

    # export file will be named after the show (with lower cases, without any spaces)
    # naming convention also for collections
    collectionName = showName.lower()
    collectionName = collectionName.replace(" ", "")

    filePath = targetDir + "/" + collectionName + ".csv"

    os.chdir("C:/Program Files/mongodb/bin/")
    mongoexportCommand = "mongoexport --db showguide --collection " + collectionName + " --csv " \
                             "--fields _id,name,episode_name_de,episode_name_en,general_episode_number,dvd_number,season,dvd_episode_number,director,identifier,content " \
                             "--out " + filePath

    subprocess.call(mongoexportCommand)

    return filePath

