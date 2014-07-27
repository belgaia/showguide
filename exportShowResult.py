#!/Python34/python
__author__ = 'Agile Developers'

import cgi

import persistence.mongoExporteur

print("Content-type: text/html; charset=utf8")
print()

form = cgi.FieldStorage()

targetDir = form.getvalue("targetDir")

if form.getvalue("series_choice") == "Alle":
    persistence.mongoExporteur.exportAllCollections(targetDir)
else:
    showNames = []
    for choice in form.getvalue("series_choice"):
        showNames.append(choice)

    persistence.mongoExporteur.exportCollections(showNames, targetDir)

print("Serie(n) " + " exportiert nach " + targetDir)
print()
print("<p>")
print("<a href='index.html'>Main Page</a><br>")
print("<a href='showguide_insert.py'>Insert Formular</a><br>")
print("<a href='showguide_addseries.py'>Add Series Formular</a><br>")
print("</p>")
