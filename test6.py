from urllib.request import urlopen
import re

words = ["youtube", "Salman", "codechef"]
i=0
while i < len(words) :
    url = "https://www.google.co.in/search?q=" + words[i]
    htmlFile = urlopen(url)
    htmlText = htmlFile.read()
    htmlText = htmlText.decode("utf=8")
    regex = '<div id="resultStats">(.+?)<nobr>'
    pattern  = re.compile(regex)
    result = re.findall(pattern,htmlFile)
    print("Your query",word[i],"contains",result)
    i += 1
    
