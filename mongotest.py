#!/Python34/python
from persistence import mongodbConnector

series = mongodbConnector.getAllSeries()

print("Content-type: text/html")
print()
print("<html><head>")
print()
print("</head><body>")
for showname in series:
	print("Series: " + showname)
print()
print("</body></html>")