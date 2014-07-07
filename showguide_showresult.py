#!/Python34/python
import cgi
import mongodbConnector

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
    print("<b>" + doc["dvd_number"]
          + " - " + doc["episode_number"]
          + " - " + doc["episode_name_de"] + "</b><br>")
    print(doc["content"])
    print("</p>")
    print()



