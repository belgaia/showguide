__author__ = 'Agile Developers'
import os
import subprocess

def exportCollection(collectionName, targetDir):

    os.chdir("C:/Program Files/mongodb/bin/")
    mongoexportCommand = "mongoexport --db showguide --collection " + collectionName + " --csv " \
                             "--fields _id,name,episode_name_de,episode_name_en,general_episode_number,dvd_number,season,dvd_episode_number,director,identifier,content " \
                             "--out " + targetDir + collectionName + ".csv"

    subprocess.call(mongoexportCommand)

