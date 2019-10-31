import csv
import matplotlib.pyplot as plt
#from matplotlib.dates import YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange
import sys
from datetime import datetime, timedelta

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

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
    culm = []

    for date in sorted(datum):
        x.append(date)
        if len(culm) == 0:
            culm.append(datum[date][0])
        else:
            culm.append(datum[date][0] + culm[-1])

    y1 = [culm[i]/(i+1) for i in range(len(culm))]
    #plt.stackplot(x,y1,y2,labels=['me','not'])
    fn = fn[:-4]
    plt.plot(x,y1,label=fn)

plt.legend()

plt.show()
