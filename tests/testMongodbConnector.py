import mongodbConnector

__author__ = 'Agile Developers'

from unittest import TestCase
from show import Show
from series import Series


class TestMongoDbConnector(TestCase):

    def test_getAllSeries(self):

        print("getAllSeries test")

        self.series = mongodbConnector.getAllSeries()
        #self.assertEquals(self.series, "Chicago Fire")

    def test_saveNewShow(self):

        self.show = Show()
        self.show.name = "Testserie"
        self.show.description = "Description of the Testserie"

        mongodbConnector.addNewShow(self.show)

    def test_saveSeries(self):

        self.series = Series()
        self.series.name = "Testserie"
        self.series.season = 1
        self.series.generalepisodenumber = 1
        self.series.episodenumber = 1
        self.series.episodename_de = "Erste Folge"
        self.series.episodename_en = "First series"
        self.series.dvdnumber = 1
        self.series.dvdepisodenumber = 1
        self.series.actors = "TestActor 1"
        self.series.director = "Director 1"
        self.series.content = "Content"

        self.seriesId = mongodbConnector.createInfo(self.series)

        self.assertIsNotNone(self.seriesId)




