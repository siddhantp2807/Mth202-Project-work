import matplotlib.pyplot as plt
from math import dist, atan2, factorial
import numpy as np
from random import sample
import json
from scipy.optimize import curve_fit

x = [[np.cos(x), np.sin(x)] for x in np.linspace(0, 2*np.pi, 2000)]

y = sample(x, 500)
def initialDict(arr) :
    return [{ 'coor' : i, 'pointsConnected' : 0} for i in arr]

def Connect(arr, r) :
    for point in arr :
        if point['pointsConnected'] == 0 :
            for other in [i for i in arr if i != point] :
                if dist(point['coor'], other['coor']) <= r :
                    point['pointsConnected'] += 1
    return arr


def simulation(pts, N, r) :
    theta = np.linspace(0, 2*np.pi, pts)
    points = [(np.cos(i), np.sin(i)) for i in theta]

    plt.plot(np.cos(theta), np.sin(theta))
    randomPoints = sample(points, N)

    delta = Connect(initialDict(randomPoints), r) 

    # for i in range(N) :
    #     plt.plot(randomPoints[i][0], randomPoints[i][1], marker = 'o')


    # plt.scatter([j['coor'][0] for j in delta], [j['coor'][1] for j in delta])
    # plt.plot([j['coor'][0] for j in delta], [j['coor'][1] for j in delta])

    # plt.axis('equal')
    # plt.show()

    return delta


def simulateAlternateImages(N, r, pts = 5000) :
    theta = np.linspace(0, 2*np.pi, pts)
    points = [(np.cos(i), np.sin(i)) for i in theta]
    plt.title(f'Simulation for N={N}, r = {r}')
    plt.plot(np.cos(theta), np.sin(theta))
    randomPoints = sample(points, N)

    delta = Connect(initialDict(randomPoints), r) 
    plt.scatter([i['coor'][0] for i in delta], [i['coor'][1] for i in delta], marker = 'o')
    con = [i['coor'] for i in delta if i['pointsConnected'] != 0]

    for i in con :
        for j in [k for k in con if k != i] :
            if dist(i, j) <= r :
                plt.plot([i[0], j[0]], [i[1], j[1]], 'r-')
    plt.axis('equal')
    plt.savefig(f'AltSim/N,r={N},{r}.png')
    plt.clf()
    # plt.show()
    

def FreqDegrees(ds) :
    freq = {}
    for i in ds :
        freq[i] = freq.get(i, 0) + 1/5
    return freq

def addToJson(file, data) :
    with open(file, 'w') as fileOpen :
        json.dump(data, fileOpen)
    return 'Done!'


# rVal = [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3]
# NVal = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 2000]
# dataList = {}
# for j in NVal :
#     Val = []
#     for i in rVal :
#             sum = 0
#             temp = []
#             for _ in range(5) :
#                 u = simulation(5000, j, i)
#                 temp += u
#                 sum += len([k for k in u if k['pointsConnected'] == 0])
            
#             Val.append({'Parameter (r)' : i, 'No. of Isolated Vertices(X)' : int(sum/5), 'pointsConnected' : FreqDegrees([k['pointsConnected'] for k in temp])})
#             print(f'r:{i} and N:{j}')
#     dataList[j] = Val

# addToJson('newData.json', dataList)
# print('Done!')


# #Generate Simulation Images
# for N in [100, 250, 500, 1000] :
#     for r in [0.004, 0.01, 0.05, 0.1] :
#         simulationImages(N, r)

C = lambda n,k : factorial(n)/(factorial(k)*factorial(n-k))
def prob(k, n, p) :
    return C(n-1, k)*pow(p, k)*pow(1-p, n-k-1)


# for r in [0.005, 0.01, 0.05, 0.1] :
#     for N in [100, 500, 1000] :
#         simulateAlternateImages(N, r)




