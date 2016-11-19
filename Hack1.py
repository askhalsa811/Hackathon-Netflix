import requests
from bs4 import BeautifulSoup

# ftp://ftp.fu-berlin.de/pub/misc/movies/database/ratings.list.gz
url_to_scrape = "ftp://ftp.fu-berlin.de/pub/misc/movies/database/ratings.list.gz"


# "http://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/rd_e_berdcostr2.tsv.gz&unzip=true"

r = requests.get(url_to_scrape)



print (r)