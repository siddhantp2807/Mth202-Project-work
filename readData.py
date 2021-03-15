import json
from math import factorial
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def getFromJson(file) :
    with open(file, 'r') as fileRead :
        x = fileRead.read()
    
    return json.loads(x)

dataDict = getFromJson('newData.json')

def plotIt(finalDict, style) :
    
    plt.style.use(style)

    for element in finalDict.keys() :
        plt.ylabel('No. of Isolated Vertices(X)')
        plt.xlabel('Parameter (r)')
        plt.title(f'X vs r with N = {element}')
        
        plt.plot([i['Parameter (r)'] for i in finalDict[element]], [j['No. of Isolated Vertices(X)'] for j in finalDict[element]], linestyle = '-', marker = 'o', markersize = 1.5)
        plt.savefig(f'curves/N={element}.png')
        plt.clf()
    return "Done"



def g(x, a, b) :
    return a*np.exp(-b*x)

def f(x, a, b) :
    return a*pow(x, b)


def fitPlotPower(finalDict, style, N) :
    parsed = finalDict
    r = [i['Parameter (r)'] for i in parsed[N]]
    X = [j['No. of Isolated Vertices(X)'] for j in parsed[N]]
    popt, pcov = curve_fit(f, r, X)
    
    plt.style.use(style)
    plt.ylabel('No. of Isolated Vertices(X)')
    plt.xlabel('Parameter (r)')
    plt.title(f'X vs r for N = {N}')
    
    plt.scatter([i['Parameter (r)'] for i in parsed[N]], [j['No. of Isolated Vertices(X)'] for j in parsed[N]], marker = 'o', label = 'Points')
    x = np.array([i['Parameter (r)'] for i in parsed[N]])
    plt.plot(x, f(x, popt[0], popt[1]), 'r--', label = f'Curve Fit: {round(popt[0], 2)}*x^({round(popt[1], 2)})')
    plt.legend()
    plt.savefig(f'powerCurve/powerCurveFitN={N}.png')
    plt.clf()


def fitPlotExp(finalDict, style, N) :
    parsed = finalDict
    r = [i['Parameter (r)'] for i in parsed[N]]
    X = [j['No. of Isolated Vertices(X)'] for j in parsed[N]]
    popt, pcov = curve_fit(g, r, X)
    
    plt.style.use(style)
    plt.ylabel('No. of Isolated Vertices(X)')
    plt.xlabel('Parameter (r)')
    plt.title(f'X vs r for N = {N}')
    
    plt.scatter([i['Parameter (r)'] for i in parsed[N]], [j['No. of Isolated Vertices(X)'] for j in parsed[N]], marker = 'o', label = 'Points')
    x = np.array([i['Parameter (r)'] for i in parsed[N]])
    plt.plot(x, g(x, popt[0], popt[1]), 'r--', label = f'Curve Fit: {round(popt[0], 2)}*exp({-round(popt[1], 2)}*x)')
    plt.legend()
    plt.savefig(f'expCurveFit/expCurveFitN={N}.png')
    plt.clf()


def fitPlotlog(finalDict, style, N) :
    r = [i['Parameter (r)'] for i in finalDict[N]]
    X = [j['No. of Isolated Vertices(X)'] for j in finalDict[N]]

    plt.style.use(style)
    plt.ylabel('log(X)')
    plt.title(f'log(X) vs log(r) for N = {N}')
    plt.xlabel('log(r)')
    plt.scatter([np.log(i['Parameter (r)']) for i in finalDict[N] if i['No. of Isolated Vertices(X)']], [np.log(j['No. of Isolated Vertices(X)']) for j in finalDict[N] if j['No. of Isolated Vertices(X)']], marker = 'o', label = 'Points')
    m, c = np.polyfit([np.log(i['Parameter (r)']) for i in finalDict[N] if i['No. of Isolated Vertices(X)']], [np.log(j['No. of Isolated Vertices(X)']) for j in finalDict[N] if j['No. of Isolated Vertices(X)']], 1)
    x = [np.log(i['Parameter (r)']) for i in finalDict[N]]
    y = [m*j + c for j in x]
    plt.plot(x, y, label = f'Best Fit: y = {round(m, 3)}*x + {round(c, 3)}')
    plt.legend()

    plt.savefig(f'logPlot/logPlotN={N}.png')
    plt.clf()

# N = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 2000]
# for i in N :
#     fitPlotlog(dataDict, 'ggplot', str(i))


C = lambda n,k : factorial(n)/(factorial(k)*factorial(n-k))
def prob(k, p) :
    return C(100-1, k)*pow(p, k)*pow(1-p, 100-k-1)


def degDistribution(finalDict, style, r, N) :
    plt.style.use(style)
    for i in finalDict :
        if i == str(N) :
            plt.ylabel('Frequency')
            plt.xlabel('No. of Points Connected')
            for j in finalDict[i] :
                if j["Parameter (r)"] == r :
                    plt.title(f'Degree Distribution for N = {i}, r = {j["Parameter (r)"]}.')

                    plt.bar([int(element) for element in j['pointsConnected'].keys()], [i for i in j['pointsConnected'].values()])
                    
                    plt.savefig(f'ProbDistribution/DegDisN,r={i},{j["Parameter (r)"]}.png')
                    plt.clf()



for N in [100, 500] :
    for r in [0.005, 0.05, 0.03] :
        degDistribution(dataDict, 'ggplot', r, N)





