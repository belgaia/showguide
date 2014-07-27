__author__ = 'Agile Developers'

import persistence.mongoExporteur

from unittest import TestCase
from show import Show


class TestMongoExporteur(TestCase):

    def test_shouldExportOneCollection(self):

        persistence.mongoExporteur.exportCollection("prisonbreak", "C:/dev/mongodb/backups/")