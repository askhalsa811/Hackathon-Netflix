import requests
from bs4 import BeautifulSoup

# url_to_scrape = "ftp://ftp.fu-berlin.de/pub/misc/movies/database/ratings.list.gz"
# opendata
# "http://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/rd_e_berdcostr2.tsv.gz&unzip=true"
#r = requests.get("http://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/rd_e_berdcostr2.tsv.gz&unzip=true")
#print(r.text)


f = open("ratings.list", encoding="iso-8859-1")
data = f.read()
f.close()

blocks = data.split("\n\n")
block = blocks[15]
lines = block.split("\n")

table = [line.split() for line in lines if len(line) > 0] #list comprehension
print(table[0:10])
print("delka souboru " + str(len(table)))



#line1 = list(filter(lambda x: len(x) > 0, data.readlines()[297].split(" ")))
#print(l)

