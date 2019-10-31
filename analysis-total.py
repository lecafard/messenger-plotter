import csv
import matplotlib.pyplot as plt
#from matplotlib.dates import YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange
import sys
from datetime import datetime, timedelta

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

fig = plt.figure(figsize=(30, 30))

for fn in sys.argv[1:]:
    fin = open(fn)

    reader = csv.reader(fin, delimiter='\t')

    datum = {}

    for row in reader:
        ts = datetime.fromtimestamp(int(row[0])//1000)
        dt = ts.replace(hour=0, minute=0, second=0, microsecond=0)
        if dt not in datum:
            datum[dt] = [0, 0, 0]

        datum[dt][0] += 1
        if row[1] == '1':
            datum[dt][1] += 1
        else:
            datum[dt][2] += 1

    x = []
    y1 = []

    for date in sorted(datum):
        x.append(date)
        if len(y1) == 0:
            y1.append(datum[date][0])
        else:
            y1.append(datum[date][0] + y1[-1])

    #plt.stackplot(x,y1,y2,labels=['me','not'])
    fn = fn[:-4]
    plt.plot(x,y1,label=fn)

plt.legend()
fig.savefig('image.png')
