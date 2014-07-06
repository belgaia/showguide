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

def addNewSeries(seriesname):
    series = {"name" : seriesname}
    series_id = database.overview.insert(series)

def removeSeries(seriesname):

    series = {"name" : seriesname}
    database.overview.remove(series)

def createInfo(series):

    seriesname = series.name
    series_id = database.seriesname.insert(series)

entry = Series()
entry.name = "TestSerie"
entry.season = "1"

#createInfo(entry)