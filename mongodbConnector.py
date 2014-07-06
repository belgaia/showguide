__author__ = 'Agile Developers'
import pymongo

databaseName = 'showguide'
mongoClient = pymongo.MongoClient("localhost", 27017)
database = mongoClient.showguide

def getAllSeries():
    seriesNames = []
    for document in database.overview.find():
        series = document['name']
        seriesNames.append(series)

    return seriesNames

def addNewSeries(seriesname):
    series = {"name" : seriesname}
    series_id = database.overview.insert(series)

def removeSeries(seriesname):

    series = {"name" : seriesname}
    database.overview.remove(series)