import csv
from procmon_parser import ProcmonLogsReader
f = open("LogFile.PML", "rb")
pmlf = ProcmonLogsReader(f)
fsize = len(pmlf)
header = ['process', 'tid', 'stacktrace', 'date', 'category','duration','stacktrace','details']
with open('LogFile.csv', 'w', encoding='UTF8',newline='') as fcsv:
    writer = csv.writer(fcsv)
    writer.writerow(header)
    for x in range(fsize):
        event = next(pmlf)
        data = []
        data.append(event.process)
        data.append(event.tid)
        data.append(event.stacktrace)
        data.append(event.date)
        data.append(event.category)
        data.append(event.duration)
        data.append(event.stacktrace)
        data.append(event.details)
        writer.writerow(data)
    
