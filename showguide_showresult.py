#!/Python34/python
import cgi

import helper
import mongodbConnector


print("Content-type: text/html; charset=utf8")
print()

form = cgi.FieldStorage()
series = form.getvalue("series_choice")
imageName = series.lower()
imageName = imageName.replace(" ", "")

print("<table width='50%'><tr><td>")
print("<img src='images/overview/" + imageName + ".jpg' alt='" + series + " Image'/></td>")
print("<td><h1>" + series + "</h1></td></tr></table>")

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









