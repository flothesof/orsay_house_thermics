###############################################################################
# fetch data

import requests

url = "https://data.enedis.fr/explore/dataset/donnees-de-temperature-et-de-pseudo-rayonnement/download/?format=xls&sort=horodate&use_labels_for_header=true&timezone=Europe%2FParis"

r = requests.get(url)

###############################################################################
# save to file, which is a rare xml kind of Excel file
# (see https://stackoverflow.com/questions/7416105/warning-when-opening-generated-xls-file-in-excel-2007 for details)
# this needs to be converted to another format by hand

with open("data.xls", "wb") as f:
    f.write(r.content)
