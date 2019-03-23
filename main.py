#  The Web Scraper Project
#
import urllib.request
import datetime

x = -1
startYear = 1994
year = datetime.datetime.now()
y = (int(year.strftime("%Y")))
rng = y - startYear
print("The National Lottery started in", startYear)
print("Loop starts at",startYear)

for i in range(startYear, y):           # So i is the itorates the range, and since the range is specified to be 1994, hardcoded, the sytem time specifies the stop date y.
                                        #We get output 1994 (start of range to 20**).

    #downloading data
    print(i)
    stringYear = str(i)
    u = urllib.request.urlretrieve("https://www.lottery.co.uk/lotto/results/archive-" + stringYear, stringYear + ".txt")





#urllib.request.url
# year = x.year
# print('https://www.lottery.co.uk/lotto/results/archive-' + str(year -1 ))
# if year == 1994: continue



# 1994


