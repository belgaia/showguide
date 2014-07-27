import mongodbConnector

__author__ = 'Agile Developers'

from unittest import TestCase


class TestMongoDbConnector(TestCase):



    def test_getAllSeries(self):

        print("getAllSeries test")

        self.series = mongodbConnector.getAllSeries()
        #self.assertEquals(self.series, "Chicago Fire")

    def test_saveNewSeries(self):

        self.series = "Testserie"

        print("saveNewSeries test")

        mongodbConnector.addNewSeries(self.series)

        mongodbConnector.removeSeries(self.series)
