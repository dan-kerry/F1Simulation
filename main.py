import pandas as pd
import numpy as np
import random
import pickle

column_names = ["Driver", "Avg_Pos", "Pos_SDV", "Ret"]
data = pd.read_csv("2020.csv", names=column_names)
Driver = data.Driver.to_list()
Avg_Pos = data.Avg_Pos.to_list()
Pos_SDV = data.Pos_SDV.to_list()
Ret = data.Ret.to_list()
fullData = [Driver] + [Avg_Pos] + [Pos_SDV] + [Ret]

points = {0: 25, 1: 18, 2: 15, 3: 12, 4: 10, 5: 8, 6: 6, 7: 4, 8: 2, 9: 1}

def retirementTest(avg_ret):
        x = random.random()
        if avg_ret > x:
            return True

def covidTest():
    x = random.random()
    if 0.01167 > x:
        return True

def Race(data):
    result = ["None"] * 20
    ranking = []

    for i in range(len(result)):
        pos = np.random.normal(data[1][i], data[2][i])
        if covidTest():
            pos += 1000
        if retirementTest(data[3][i]):
            pos += 100
        ranking += [[data[0][i], pos, i]]
    raceRank = (Sort(ranking))
    for j in range(10):
        raceRank[j].append(points[j])
    for k in range(10, 20):
        raceRank[k].append(0)
    return raceRank


def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    sub_li.sort(key=lambda x: x[1])
    return sub_li

def Season():
    standings = [0] * 20
    seasonData = []
    for i in range(17):
        raceResult = (Race(fullData))
        seasonData += [raceResult]
        for j in range(len(raceResult)):
            standings[raceResult[j][2]] += raceResult[j][3]
    return([seasonData] + [standings])


output = []
iterations = 100
for x in range(iterations):
    output += [Season()]
    print(Season())
    if x % 10000 == 0:
        print(x)
file = open('sim_data4', 'wb')
pickle.dump(output, file, protocol=pickle.HIGHEST_PROTOCOL)
file.close()


















