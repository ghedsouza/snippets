import csv
f = open("dbs3.prod.polarmobile.com.neo201811-20 AM.csv", "rb")
r = csv.reader(f)
lines = list(r)

import terminaltables
table = terminaltables.AsciiTable(lines)


print table.table
