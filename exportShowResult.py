#!/Python34/python
__author__ = 'Agile Developers'

import cgi

import persistence.mongoExporteur

print("Content-type: text/html; charset=utf8")
print()

form = cgi.FieldStorage()

showName = form.getvalue("series_choice")
targetDir = form.getvalue("targetDir")

usedTargetDir = persistence.mongoExporteur.exportCollection(showName, targetDir)

print("Serie " + showName + " was exported to " + usedTargetDir)
print()
print("<p>")
print("<a href='index.html'>Main Page</a><br>")
print("<a href='showguide_insert.py'>Insert Formular</a><br>")
print("<a href='showguide_addseries.py'>Add Series Formular</a><br>")
print("</p>")
