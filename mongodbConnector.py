__author__ = 'Agile Developers'
import pymongo
from series import Series

databaseName = 'showguide'
mongoClient = pymongo.MongoClient("localhost", 27017)
database = mongoClient.showguide

def getAllSeries():
    seriesNames = []
    for document in database.overview.find():
        seriesName = document['name']
        seriesNames.append(seriesName)

    return seriesNames

def addNewShow(show):
    #series = {"name" : seriesname}
    #series = {"description" : description}
    #series_id = database.overview.insert(series)

    showObject = {"name" : show.name,
                  "description" : show.description
    }

    show._id = database.overview.insert(showObject)
    return show._id

def removeSeries(seriesname):

    series = {"name" : seriesname}
    database.overview.remove(series)

def createInfo(series):

    seriesObject = {"name" : series.name,
                    "identifier" : series.season + "x" + series.episodenumber,
                    "season" : series.season,
                    "episode_number" : series.episodenumber,
                    "general_episodenumber" : series.generalepisodenumber,
                    "episode_name_de" : series.episodename_de,
                    "episode_name_en" : series.episodename_en,
                    "dvd_number" : series.dvdnumber,
                    "dvd_episode_number" : series.dvdepisodenumber,
                    "content" : series.content,
                    "director" : series.director }

    # for saving the series as mongodb-collection it must be in lower cases without any spaces
    seriesname = series.name.lower()
    seriesname = seriesname.replace(" ", "")
    series_id = database[seriesname].insert(seriesObject)

def getEpisodeguide(series):

    seriesName = series.lower()
    seriesName = seriesName.replace(' ', '')
    documents = database[seriesName].find()
    return documents;

series = Series()
series.name = "TestSerie"
series.content = "Test content mit Umlauten ä, ü, ö, ß."
createInfo(series)