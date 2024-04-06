import csv
import matplotlib.pyplot as plt 
from math import log, sqrt
import os


# load all the data from a csv file
def loadDataMoreInputs(fileName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    return dataNames, data

# extract a particular feature (column)
def extractFeature(allData, names, featureName):
    pos = names.index(featureName)
    return [float(data[pos]) for data in allData]

# plot a histogram for some data x
def plotDataHistogram(x, variableName):
    n, bins, patches = plt.hist(x, 20)
    plt.title('Histogram of ' + variableName)
    plt.show()


#pb1


crtDir =  os.getcwd()
filePath = os.path.join(crtDir, 'data', 'employees.csv')

names, allData = loadDataMoreInputs(filePath)

#Salary
prices = extractFeature(allData, names, 'Salary')
pricesScaled01 = [(p - min(prices)) / (max(prices) - min(prices)) for p in prices]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
ax1.hist(prices, 20)
ax1.set_title('Salary histo')
ax2.hist(pricesScaled01, 20)
ax2.set_title('[0,1] scaled Salary histo')
plt.show()

#Bonus
bonusuri=extractFeature(allData, names, 'Bonus %')
bonusLog = [log(p) for p in bonusuri]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
ax1.hist(bonusuri, 20)
ax1.set_title('Bonus histo')
ax2.hist(bonusLog, 20)
ax2.set_title('log Bonus histo')
plt.show()
