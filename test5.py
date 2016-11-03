from urllib.request import urlopen
import re

symbolList = ["aapl","goog","spy","nflx"]

i = 0;
while i < len(symbolList):
    url = "http://finance.yahoo.com/q?s="+ symbolList[i] +"&fr=uh3_finance_web&uhb=uhb2"
    htmlFile = urlopen(url)
    htmlText = htmlFile.read()
    htmlText = htmlText.decode("utf-8")
    regex = '<span id="yfs_l84_'+ symbolList[i] +'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmlText)
    print("The Stock price of",symbolList[i],"is",price)
    i += 1
