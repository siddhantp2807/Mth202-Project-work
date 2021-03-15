from scipy.stats import binom
# from scipy.optimize import curve_fit
from math import comb
import numpy as np
import json
import matplotlib.pyplot as plt

jsonData = json.load(open('newData.json'))



def prob(k, p) :

    return comb(100-1, k)*pow(p, k)*pow(1-p, 100-k-1)



def degreeDist(finalDict, r, N) :
    plt.style.use('ggplot')
    for el in finalDict :
        if el == str(N) :
            data = [k['pointsConnected'] for k in finalDict[el] if k['Parameter (r)'] == r][0]

            plt.bar(list(map(int, data.keys())), [i for i in data.values()])
    # print(popt)
    plt.show()
    return [i for i in data.values()]

def binDegDist(finalDict, r, N) :
    plt.style.use('ggplot')
    for el in finalDict :
        if el == str(N) :
            data = [k['pointsConnected'] for k in finalDict[el] if k['Parameter (r)'] == r][0]
           
            plt.plot(list(map(int, data.keys())), [i/100 for i in data.values()])
            plt.scatter(sorted(list(map(int, data.keys()))), binom.pmf(sorted(list(map(int, data.keys()))), N-1, r/2))
    plt.xlabel('K')
    plt.ylabel('P(x = k)')
    # plt.legend()
    plt.show()

# degreeDist(jsonData, 0.05, 100)
binDegDist(jsonData, 0.1, 1000)
