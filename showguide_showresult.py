#!/Python34/python
import cgi
import mongodbConnector
import os

print("Content-type: text/html; charset=utf8")
print()

form = cgi.FieldStorage()
series = form.getvalue("series_choice")
print("<h1>" + series + "</h1>")

print("<h2>Allgemeine Infos</h2>")
print()

print("<h2>Episodeguide</h2>")
print()

# this is just a workaround -- fix problems with encoding
def replaceUmlaute(content):
    fixedContent = content.replace('ü', 'ue')
    fixedContent = fixedContent.replace('ö', 'oe')
    fixedContent = fixedContent.replace('ä', 'ae')
    fixedContent = fixedContent.replace('ß', 'ss')

    return fixedContent

documents = mongodbConnector.getEpisodeguide(series)
for doc in documents:
    print("<p>")
    print("<b>" + doc["dvd_number"]
          + " - " + doc["episode_number"]
          + " - " + doc["episode_name_de"] + "</b><br>")
    content = replaceUmlaute(doc["content"])
    print(content)
    print("</p>")
    print()









