import mongodbConnector

__author__ = 'Agile Developers'

from unittest import TestCase
from show import Show


class TestMongoDbConnector(TestCase):



    def test_getAllSeries(self):

        print("getAllSeries test")

        self.series = mongodbConnector.getAllSeries()
        #self.assertEquals(self.series, "Chicago Fire")

    def test_saveNewSeries(self):

        self.show = Show()
        self.show.name = "Testserie"
        self.show.description = "Description of the Testserie"

        mongodbConnector.addNewShow(self.show)