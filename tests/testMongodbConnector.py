import mongodbConnector

__author__ = 'Agile Developers'

from unittest import TestCase
from show import Show
from series import Series


class TestMongoDbConnector(TestCase):

    def setUp(self):

        mongodbConnector.setupDatabase("testShowGuidePersistence")

    def test_getAllShows(self):

        print("getAllShows test")

        self.shows = mongodbConnector.getAllSeries()
        self.assertIsNotNone(self.shows)

    def test_getSeries(self):

        print("getSeries test")

        self.show = "Testserie"
        self.identifier = "1x1"

        self.documents = mongodbConnector.getSeries(self.show, self.identifier)
        self.assertIsNotNone(self.documents)

        for document in self.documents:
            print("Document: " + document["name"])
            self.assertEquals(document["name"], self.show)
            self.assertEquals(document["identifier"], self.identifier)

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

def test_updateSeries(self):

        self.series = Series()
        self.series.name = "Testserie"
        self.series.identifier = "1x1"
        self.series.content = "Neuer Content nach Update"

        self.updatedSeries = mongodbConnector.updateSeries(self.series)
        self.assertIsNotNone(self.updatedSeries)


