import csv
data = []

with open("PSCompPars_2021.08.10_02.55.27.csv","r") as f:
    csvReade = csv.reader(f)
    for row in csvReade:
        data.append(row)

headers = data[0]
planet_data = data[1:]

for data in planet_data:
    data[2] = data[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("DataSet_2_sorted.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)