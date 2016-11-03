from urllib.request import urlopen
import re

htmlFile = urlopen('http://finance.yahoo.com/q?s=AAPL')
htmlText = htmlFile.read()
htmlText = htmlText.decode("utf-8")
regex = '<span id="yfs_l84_aapl">(.+?)</span>'
pattern = re.compile(regex)
price = re.findall(pattern,htmlText)
print(price)
