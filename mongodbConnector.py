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
