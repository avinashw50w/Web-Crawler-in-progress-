from urllib.request import urlopen
import re

urls = ["http://github.com", "http://ndtv.com", "http://hackerrank.com", "http://quora.com"]

regex = '<title>(.+?)</title>'
pattern = re.compile(regex)
i=0
while i < len(urls):
    htmlFile = urlopen(urls[i])
    htmlText = htmlFile.read()
    htmlText = htmlText.decode("utf-8")
    titles = re.findall(pattern,htmlText)
    print(titles)
    i += 1
