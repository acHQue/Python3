#
#   The Web Scraper Project
#

import datetime

x = datetime.datetime.now()
#y = x.year

#xml = urlopen("https://www.lottery.co.uk/lotto/results/past").read()

import urllib.request

#urllib.request.urlretrieve("https://www.lottery.co.uk/lotto/results/past", "test.txt")

year = x.year
#int(year -1)
#print(int(year - 1 ))

for year in range(1994, year):
    #print('https://www.lottery.co.uk/lotto/results/archive-' + str(year -1 ))
    #if year == 1994: continue

    print(year)

#1994

#urllib.request.url



