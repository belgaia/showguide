__author__ = 'Agile Developers'

from unittest import TestCase

import mongoExporteur


class TestMongoExporteur(TestCase):

    def test_shouldExportOneCollection(self):

        print("Testing export of one collections.")

        mongoExporteur.exportCollection("prisonbreak", "C:/dev/mongodb/backups/")

    def test_shouldExportMultipleCollections(self):

        print("Testing export of multiple collections.")

        shows = [ "prisonbreak", "chicagofire" ]
        mongoExporteur.exportCollections(shows, "C:/dev/mongodb/backups/")


    def test_shouldExportAllCollections(self):

        print("Testing export of all collections.")

        mongoExporteur.exportAllCollections( "C:/dev/mongodb/backups/")