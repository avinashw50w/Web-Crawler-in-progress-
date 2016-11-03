from urllib.request import urlopen

urls = ["http://google.com", "http://ndtv.com", "http://quora.com"]
i=0
while i < len(urls):
    htmlFile = urlopen(urls[i])
    htmlText = htmlFile.read()
    print(htmlText)
    i += 1
