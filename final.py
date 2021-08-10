import csv
dataSet1 = []
dataSet2 = []

with open("dataset_1.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataSet1.append(row)

with open("DataSet_2_sorted.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataSet2.append(row)

headers1 = dataSet1[0]
headers2 = dataSet2[0]

data1 = dataSet1[1:]
data2 = dataSet2[1:]

headers = headers1 + headers2
finalData = []

for index,data in enumerate(data1):
    finalData.append(data1[index]+data2[index])

with open("FinalScrappedData.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(finalData)
