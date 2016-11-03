import urllib

htmlFile = urllib.request.urlopen("http://google.com")
htmlText = htmlFile.read()
print(htmlText)
