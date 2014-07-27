__author__ = 'Agile Developers'

import persistence.mongoExporteur

from unittest import TestCase
from show import Show


class TestMongoExporteur(TestCase):

    def test_shouldExportOneCollection(self):

        print("Testing export of one collections.")

        persistence.mongoExporteur.exportCollection("prisonbreak", "C:/dev/mongodb/backups/")

    def test_shouldExportMultipleCollections(self):

        print("Testing export of multiple collections.")

        shows = [ "prisonbreak", "chicagofire" ]
        persistence.mongoExporteur.exportCollections(shows, "C:/dev/mongodb/backups/")


    def test_shouldExportAllCollections(self):

        print("Testing export of all collections.")

        persistence.mongoExporteur.exportAllCollections( "C:/dev/mongodb/backups/")