#!/usr/bin/python


emails = ['lNlffBWyo@gmail.com', 'uUNnFWr@gmail.com',
                  'CVOucdfTZfdqwlUDVJ@gmail.com', 'KhAezXwAZUUpOZdlhn@gmail.com',
                  'rYqKKheScZpG@gmail.com', 'kPHHmbQliojUrMy@gmail.com',
                  'hDHiHCeYboJgoed@gmail.com', 'DpiKdMYPcYxnyGFE@gmail.com',
                  'QEEAlDCQvlzAxuaK@gmail.com', 'AHzVwlzfHTuB@gmail.com',
                  'nhhmCVXHs@gmail.com', 'eDcPQUJLsXpKCHehw@gmail.com',
                  'IzexPV@gmail.com', 'SCSRoAX@gmail.com', 'JeamuDBywLOx@gmail.com',
                  'dhzdsKuwvQqLICwrgBuA@gmail.com', 'FDVUsYKjKCgWlMcKFvV@gmail.com',
                  'CFiNVgHeFyudJvHmlChQ@gmail.com', 'FOHgDgM@gmail.com', 'YFIXvXBA@gmail.com']

substr = "Dg"
found = [s for s in emails if substr in s]
print("Emails which contain 'Dg' substring : ")
print(found)
print()

i = 4
x = [s[i] for s in emails]
print("Every " + str(i) + "th symbol in emails list")
print(x)
print()

tuples = [(18, 11), (14, 12), (20, 7), (18, 8), (5, 19),
          (9, 5), (11, 14), (5, 13), (13, 17), (16, 15),
          (8, 8), (14, 6), (8, 6), (8, 19), (15, 13),
          (9, 5), (20, 15), (5, 19), (15, 18), (13, 8)]

from operator import itemgetter
tuples_sorted = sorted(tuples, key=itemgetter(1))
print("Sorted tuples list")
print(tuples_sorted)


def func(*params) :
    return sum(params)

print("Function that gets any number of integer arguments")
print(func(1, 2, 3))
print(func(5, 4))
print(func(1000, 1000, 1000, 1000, 1000))
print(func(15))

from numpy.random import randn
from pandas import DataFrame

print("Create random pandas.DataFrame from random numbers (10 by 4), change columns names to any other : ")
randDf = DataFrame(randn(10, 4), columns=["data1", "data2", "data3", "data4"])
print(randDf)

from pandas import read_csv
print("Import pandas.DataFrame from df.csv")
df = read_csv('df.csv', sep=';')

X = list(df.groupby(by='country_code'))

countsG = []
countsH = []
for it in X :
    countsG.append(sum(1 for s in it[1]['email'] if "@gmail.com" in s))
    countsH.append(sum(1 for s in it[1]['email'] if "@hotmail.com" in s))
countries = [s[0] for s in X]
counts = [countsH[i]/(countsG[i]+countsH[i])*100 for i in range(0, len(countries))]

import matplotlib.pyplot as plt
w = 0.8
B = plt.bar(countries, [100]*len(countries), color='#006699', width=w)
A = plt.bar(countries, counts, color='#ff6666', width=w)
plt.legend((A[0], B[0]), ('@hotmail.com', '@gmail.com'))
plt.show()
