import pickle
import pandas as pd
import copy

def fileCombine():
    bigFile = []
    for x in range(1, 5):
        filename = 'sim_data' + str(x)
        file = open(filename, 'rb')
        data = pickle.load(file)
        file.close()
        bigFile += data
        print(f"Loaded: {filename}")
    return bigFile

def loadFile(file):
    filename = 'sim_data' + str(file)
    file = open(filename, 'rb')
    data = pickle.load(file)
    file.close()
    print(f"Loaded: {filename}")
    return data



def ChampCount(data):
    lewis = 0
    verst = 0
    other = 0
    valtteri = 0
    for x in range(len(data)):
        max_value = max(data[x][1])
        max_index = data[x][1].index(max_value)
        if max_index == 0:
            lewis += 1
        elif max_index == 1:
            valtteri += 1
        elif max_index == 2:
            verst += 1
        else:
            other += 1
            print(max_index)
            print(x)
    print(lewis)
    print(valtteri)
    print(verst)
    print(other)

def Test1():
    print(data[0][1])

def seasonCSV(data, output):
    column_names = ["Driver", "Avg_Pos", "Pos_SDV", "Ret"]
    temp_data = pd.read_csv("2020.csv", names=column_names)
    Driver = temp_data.Driver.to_list()
    season_raw = data[1]
    holder = []
    for i in range(len(season_raw)):
        holder += [[Driver[i]] + [season_raw[i]]]

    Sort(holder)

    points = []
    drivers = []
    for i in range(len(holder)):
        drivers.append(holder[i][0])
        points.append(holder[i][1])

    df = pd.DataFrame(data={"Driver": drivers})

    for i in range(17):
        race = data[0][i]
        A = [0] * 20
        for x in range(20):
            count = 0
            while True:
                if race[x][0] == holder[count][0]:
                    A[count] = x
                    if race[x][1] > 90:
                        A[count] = "RET"
                    if race[x][1] > 900:
                        A[count] = "DNS"
                    break
                count += 1

        for y in range(len(A)):
            if type(A[y]) == int:
                A[y] += 1
        df[str(i + 1)] = A
    df["points"] = points
    df.to_csv(output + ".csv", index=False)

def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1], reverse=True)
    return sub_li

def Sort3rd(sub_li):
    sub_li.sort(key=lambda x: x[2], reverse=True)
    return sub_li

def greatestRange(data):
    index = 0
    topResult = 0
    for x in range(len(data)):
        lowScore = min(data[x][1])
        highScore = max(data[x][1])
        gap = highScore - lowScore
        if gap > topResult:
            topResult = gap
            index = x
    print(f"Greatest Range: {topResult}, found at: {index}")

def smallestRange(data):
    index = 0
    topResult = 500
    for x in range(len(data)):
        lowScore = min(data[x][1])
        highScore = max(data[x][1])
        gap = highScore - lowScore
        if gap < topResult:
            topResult = gap
            index = x
    print(f"Smallest Range: {topResult}, found at: {index}")

def bestSeason(data):
    drivers = [['Hamilton', 0, 0], ['Bottas', 0, 0], ['Verstappen', 0, 0], ['Perez', 0, 0], ['Ricciardo', 0, 0], ['Sainz', 0, 0], ['Albon', 0, 0], ['Leclerc', 0, 0], ['Norris ', 0, 0], ['Gasly', 71, 0], ['Stroll', 0, 0], ['Ocon ', 0, 0], ['Vettel', 0, 0], ['Kvyat', 0, 0], ['Raikonnen', 0, 0], ['Giovinazzi', 0, 0], ['Russell', 0, 0], ['Grosjean ', 0, 0], ['Magnussen', 0, 0], ['Latifi', 0, 0]]
    for x in range(len(data)):
        for y in range(len(data[x][1])):
            if data[x][1][y] > drivers[y][1]:
                drivers[y][1] = data[x][1][y]
                drivers[y][2] = x
    return(drivers)

def bestResults(data):
    drivers = [['Hamilton', 25, 0], ['Bottas', 25, 0], ['Verstappen', 25, 0], ['Perez', 25, 0], ['Ricciardo', 25, 0], ['Sainz', 25, 0], ['Albon', 25, 0], ['Leclerc', 25, 0], ['Norris ', 25, 0], ['Gasly', 25, 0], ['Stroll', 25, 0], ['Ocon ', 25, 0], ['Vettel', 25, 0], ['Kvyat', 25, 0], ['Raikonnen', 25, 0], ['Giovinazzi', 25, 0], ['Russell', 25, 0], ['Grosjean ', 25, 0], ['Magnussen', 25, 0], ['Latifi', 25, 0]]
    for x in range(len(data)):
        for y in range(len(data[x])):
            for z in range(len(data[x][0])):
                if z < drivers[data[x][0][y][z][2]][1]:
                    drivers[data[x][0][y][z][2]][1] = z
                    drivers[data[x][0][y][z][2]][2] = 0
                if z == drivers[data[x][0][y][z][2]][1]:
                    drivers[data[x][0][y][z][2]][2] += 1


    for i in range(len(drivers)):
        drivers[i][1] += 1
    export = pd.DataFrame(drivers)
    return(drivers)

def champ_Count(data):
    drivers = [['Hamilton', 0, 0], ['Bottas', 0, 0], ['Verstappen', 0, 0], ['Perez', 0, 0], ['Ricciardo', 0, 0], ['Sainz', 0, 0], ['Albon', 0, 0], ['Leclerc', 0, 0], ['Norris ', 0, 0], ['Gasly', 0, 0], ['Stroll', 0, 0], ['Ocon ', 0, 0], ['Vettel', 0, 0], ['Kvyat', 0, 0], ['Raikonnen', 0, 0], ['Giovinazzi', 0, 0], ['Russell', 0, 0], ['Grosjean ', 0, 0], ['Magnussen', 0, 0], ['Latifi', 0, 0]]
    for x in range(len(data)):
        max_value = max(data[x][1])
        max_index = data[x][1].index(max_value)
        drivers[max_index][1] += 1
        drivers[max_index][2] = x
    return(drivers)

def mostRetirements(data):
    SeasonBest = 0
    SeasonBestInd = 0
    SeasonFewest = 300
    SeasonFewInd = 0
    RaceBest = 0
    RaceBestInd = 0
    for x in range(len(data)):
        SeasonTotal = 0
        for y in range(len(data[x][0])):
            RaceTotal = 0
            for z in range(len(data[x][0][y])):
                #print(data[x][0][y][z])
                if data[x][0][y][z][1] > 50 and data[x][0][y][z][1] < 200:
                    RaceTotal += 1
                    SeasonTotal += 1
                if RaceTotal > RaceBest:
                    RaceBest = RaceTotal
                    RaceBestInd = x
        if SeasonTotal > SeasonBest:
                SeasonBest = SeasonTotal
                SeasonBestInd = x
        if SeasonTotal < SeasonFewest:
                SeasonFewest = SeasonTotal
                SeasonFewInd = x
    seasonCSV(data[RaceBestInd], f"MostRetsRace_{RaceBest}")
    seasonCSV(data[SeasonBestInd], f"MostRetsSeason_{SeasonBest}")
    seasonCSV(data[SeasonFewInd], f"FewRetsSeason_{SeasonFewest}")

def avgPoints(data):
    result = [0] * 20
    for x in range(len(data)):
        for y in range(len(data[x][1])):
            result[y] += data[x][1][y]
    for z in range(len(result)):
        result[z] /= len(data)
    return(result)

def other_wins(data):
    for x in range(len(data)):
        max_value = max(data[x][1])
        max_index = data[x][1].index(max_value)
        if max_index == 4 or max_index == 6 or max_index == 7:
            print(max_index)
            seasonCSV(data[x], f"{x}, {max_index}")

def biggestWin(data):
    Big = 0
    BigIndex = 0
    Small = 500
    SmallIndex = 0
    for x in range(len(data)):
        temp = data[x][1]
        temp2 = temp.sort(reverse=True)
        diff = temp[0] - temp[1]
        if diff > Big:
            Big = diff
            BigIndex = x
        if diff < Small:
            Small = diff
            SmallIndex = x
    seasonCSV(data[BigIndex], f"Big_{Big}_{BigIndex}")
    seasonCSV(data[SmallIndex], f"Small_{Small}_{SmallIndex}")

def draws(data):
    draw_count = 0
    for x in range(len(data)):
        temp = data[x][1]

        temp2 = sorted(temp, reverse=True)
        if temp2[0] == temp2[1]:
            draw_count += 1
        if temp2[0] == temp2[1] and temp2[1] == temp2[2]:
            print("Shit...")
            seasonCSV(data[x], f"ThreeWayDraw_{x}")
    print(draw_count)

def teamResult(data):
    BiggestGap = 0
    BigGapIndex = 0
    teamTally= [["Mercedes", 0], ["Red Bull", 0], ["McLaren", 0], ["Ferrari", 0], ["Renault", 0], ["Racing Point", 0], ["Alpha Tauri", 0], ["Alfa Romeo", 0], ["Haas", 0], ["Williams", 0]]
    for x in range(len(data)):
        team = [[0, "Mercedes", 0], [1, "Red Bull", 0], [2, "McLaren", 0], [3, "Ferrari", 0], [4, "Renault", 0],
                     [5, "Racing Point", 0], [6, "Alpha Tauri", 0], [7, "Alfa Romeo", 0], [8, "Haas", 0], [9, "Williams", 0]]
        for y in range(len(data[x][0])):
            ordered = copy.copy(data[x][0][y])
            ordered = Sort3rd(ordered)
            team[9][2] += (ordered[0][3] + ordered[3][3]) #Williams
            team[8][2] += (ordered[1][3] + ordered[2][3])  # Haas
            team[7][2] += (ordered[4][3] + ordered[5][3]) #Alfa Romeo
            team[6][2] += (ordered[6][3] + ordered[10][3])  # Alpha Tauri
            team[5][2] += (ordered[9][3] + ordered[16][3])  # Racing Point
            team[4][2] += (ordered[8][3] + ordered[15][3])  # Renault
            team[3][2] += (ordered[7][3] + ordered[12][3])  # Ferrari
            team[2][2] += (ordered[11][3] + ordered[14][3])  # Mclaren
            team[1][2] += (ordered[13][3] + ordered[17][3])  # Red Bull
            team[0][2] += (ordered[19][3] + ordered[18][3])  # Alfa Romeo
        seasonResult = Sort3rd(team)
        gap = seasonResult[0][2] - seasonResult[1][2]
        if gap > BiggestGap:
            BiggestGap = gap
            BigGapIndex = x
        if seasonResult[0][0] != 0:
            if seasonResult[0][0] != 1:
                seasonCSV(data[x], f"NonMercRB_{x}")
        teamTally[seasonResult[0][0]][1] += 1
    print(teamTally)
    seasonCSV(data[BigGapIndex], f"BigTeamGap_{BiggestGap}_{BigGapIndex}")

def HamBotVer(data, HBVcount, pods, i, HBPcount, PVBcount):
    iter = i - 1
    race_count = 0

    for x in range(len(data)):
        for y in range(len(data[x][0])):
            race_count += 1
            if ((data[x][0][y][0][2] == 0) or (data[x][0][y][0][2] == 1) or (data[x][0][y][0][2] == 2)) and ((data[x][0][y][1][2] == 0) or (data[x][0][y][1][2] == 1) or (data[x][0][y][1][2] == 2)) and ((data[x][0][y][2][2] == 0) or (data[x][0][y][2][2] == 1) or (data[x][0][y][2][2] == 2)):
                HBVcount += 1
            if ((data[x][0][y][0][2] == 0) or (data[x][0][y][0][2] == 1) or (data[x][0][y][0][2] == 3)) and ((data[x][0][y][1][2] == 0) or (data[x][0][y][1][2] == 1) or (data[x][0][y][1][2] == 3)) and ((data[x][0][y][2][2] == 0) or (data[x][0][y][2][2] == 1) or (data[x][0][y][2][2] == 3)):
                HBPcount += 1
            if ((data[x][0][y][0][2] == 3) or (data[x][0][y][0][2] == 1) or (data[x][0][y][0][2] == 2)) and ((data[x][0][y][1][2] == 3) or (data[x][0][y][1][2] == 1) or (data[x][0][y][1][2] == 2)) and ((data[x][0][y][2][2] == 3) or (data[x][0][y][2][2] == 1) or (data[x][0][y][2][2] == 2)):
                PVBcount += 1
            if race_count % 250 == 0:
                place = race_count + (iter * (len(data)*17))
                pods.append([place, HBVcount, HBPcount, PVBcount])

def BadLuck(data):
    hs = 0
    hs_ind = 0
    for x in range(len(data)):
        drivers = [['Hamilton', 0, 0], ['Bottas', 0, 0], ['Verstappen', 0, 0], ['Perez', 0, 0], ['Ricciardo', 0, 0],
                   ['Sainz', 0, 0], ['Albon', 0, 0], ['Leclerc', 0, 0], ['Norris ', 0, 0], ['Gasly', 0, 0],
                   ['Stroll', 0, 0], ['Ocon ', 0, 0], ['Vettel', 0, 0], ['Kvyat', 0, 0], ['Raikonnen', 0, 0],
                   ['Giovinazzi', 0, 0], ['Russell', 0, 0], ['Grosjean ', 0, 0], ['Magnussen', 0, 0], ['Latifi', 0, 0]]
        for y in range(len(data[x][0])):
            for z in range(len(data[x][0][y])):
                if data[x][0][y][z][1] > 50 and data[x][0][y][z][1] < 200:
                    drivers[data[x][0][y][z][2]][1] += 1
        sorted_drivers = Sort(drivers)
        if sorted_drivers[0][1] > hs:
            hs = sorted_drivers[0][1]
            hs_ind = x

    seasonCSV(data[hs_ind], f"MostDriverRets_{hs}")

def VizCount(data, drivers):
    for x in range(len(data)):
        for y in range(len(data[x][0])):
            for z in range(len(data[x][0][y])):
                if data[x][0][y][z][1] < 90:
                    drivers[data[x][0][y][z][2]][z + 1] += 1
                elif data[x][0][y][z][1] > 91 and data[x][0][y][z][1] < 200:
                    drivers[data[x][0][y][z][2]][21] += 1
                elif data[x][0][y][z][1] > 300:
                    drivers[data[x][0][y][z][2]][22] += 1


drivers = [['Hamilton'] + [0] * 22, ['Bottas'] + [0] * 22, ['Verstappen'] + [0] * 22, ['Perez'] + [0] * 22, ['Ricciardo'] + [0] * 22,
           ['Sainz'] + [0] * 22, ['Albon'] + [0] * 22, ['Leclerc'] + [0] * 22, ['Norris'] + [0] * 22, ['Gasly'] + [0] * 22,
           ['Stroll'] + [0] * 22, ['Ocon'] + [0] * 22, ['Vettel'] + [0] * 22, ['Kvyat'] + [0] * 22, ['Raikonnen'] + [0] * 22,
           ['Giovinazzi'] + [0] * 22, ['Russell'] + [0] * 22, ['Grosjean'] + [0] * 22, ['Magnussen'] + [0] * 22, ['Latifi'] + [0] * 22]

for i in range(1, 5):
    simData = loadFile(i)
    VizCount(simData, drivers)
    del simData

export = pd.DataFrame(drivers)
export.to_csv("AllPositions.csv", index=False)








