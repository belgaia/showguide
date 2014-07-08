#!/Python34/python
import cgi
import mongodbConnector
import helper

print("Content-type: text/html; charset=utf8")
print()

form = cgi.FieldStorage()
series = form.getvalue("series_choice")
print("<h1>" + series + "</h1>")

print("<h2>Allgemeine Infos</h2>")
print()

print("<h2>Episodeguide</h2>")
print()

documents = mongodbConnector.getEpisodeguide(series)
for doc in documents:
    print("<p>")
    print("<b>DVD " + doc["dvd_number"]
          + " - " + doc["identifier"]
          + " - Episode " + doc["episode_number"]
          + " - " + helper.replaceUmlaute(doc["episode_name_de"]) + "</b><br>")
    content = helper.replaceUmlaute(doc["content"])
    print(content)
    print("</p>")
    print()









