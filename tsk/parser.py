import csv
from tsk.models import Metrics

def parse():
    f = open(r'C:\Users\User\PycharmProjects\tskapi\tsk\dataset.csv', 'r')
    reader = csv.reader(f)
    for row in reader:
        if str(row[5]).isdigit():
            obj = Metrics(date=row[0], channel=row[1], country=row[2],
                          os=row[3], impressions=row[4], clicks=row[5],
                          installs=row[6], spend=row[7], revenue=row[8])
            obj.save()
    f.close()