import json
from math import factorial, comb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from scipy.sparse import data

dataDict = json.load(open('newData.json'))

def plotIt(finalDict, style) :
    
    plt.style.use(style)
    i = 0
    for element in finalDict.keys() :
        plt.ylabel('No. of Isolated Vertices(X)')
        plt.xlabel('Parameter (r)')
        plt.title(f'X vs r with N = {element}')
        
        plt.plot([i['Parameter (r)'] for i in finalDict[element]], [j['No. of Isolated Vertices(X)'] for j in finalDict[element]], linestyle = '-', marker = 'o', markersize = 1.0, label = f'N = {element}')
        # plt.legend()
        
        if element == "2000" :
            
            plt.savefig(f'all/all.png', dpi = 600)
            plt.clf()
        i += 1

    return "Done"

def g(x, a, b) :
    return a*np.exp(-b*x)

def f(x, a, b) :
    return a*pow(x, -b)



def fitPlotExp(finalDict, style, N) :
    parsed = finalDict
    r = [i['Parameter (r)'] for i in parsed[N]]
    X = [j['No. of Isolated Vertices(X)'] for j in parsed[N]]
    popt, pcov = curve_fit(g, r, X)
    
    plt.style.use(style)
    plt.ylabel('No. of Isolated Vertices(X)')
    plt.xlabel('Parameter (r)')
    plt.title(f'X vs r for N = {N}')
    
    plt.plot([i['Parameter (r)'] for i in parsed[N]], [j['No. of Isolated Vertices(X)'] for j in parsed[N]], '#471323', marker = 'o', label = 'Points', linestyle = '')
    x = np.linspace(0, 0.3, 500)
    plt.plot(x, g(x, popt[0], popt[1]), '#585563',label = f'Curve Fit: {round(popt[0], 2)}*exp({-round(popt[1], 2)}*x)')
    plt.legend()
    plt.savefig(f'agnExpCurveFit/expCurveFitN={N}.png', dpi = 600)
    plt.clf()

# for N in [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 2000] :
#     fitPlotExp(dataDict, 'seaborn', str(N))



def degDistribution(finalDict, style, r, N) :
    plt.style.use(style)
    for i in finalDict :
        if i == str(N) :
            plt.ylabel('P(X = k)')
            plt.xlabel('No. of Points Connected (k)')
            for j in finalDict[i] :
                if j["Parameter (r)"] == r :
                    plt.title(f'Degree Distribution for N = {i}, r = {j["Parameter (r)"]}.')
                    
                    elements = [element for element in sorted([int(el) for el in j['pointsConnected'].keys()])]
                    plt.plot(elements, [j['pointsConnected'][str(i)]/N for i in elements], color='#C46D5E', label = 'Probability vs Degree Curve')
                    # popt, pcov = curve_fit(f, elements, [j['pointsConnected'][str(i)]/N for i in elements])

                    
                    pts = np.linspace(min(elements), max(elements)+1, 500)
                    # plt.plot(pts, f(pts, popt[0], popt[1]), label = f'Power curve: y = {round(popt[0], 2)}*x^{-round(popt[1], 2)}', color="#6320ee")
                    plt.plot(pts, [pow(i, -1.5) for i in pts], label = 'Power curve: y = x^-1.5', color="#6320ee")

                    plt.legend()
                    plt.xlim(-0.5, max(elements)+1)
                    plt.ylim(0, 1)
                    
                    
                    plt.savefig(f'newDist/N,r={N},{r}.png', dpi=600)
                    plt.clf()





for r in [0.001, 0.007, 0.05, 0.1] :
    for N in [100, 500, 700, 1000, 2000] :
        degDistribution(dataDict, 'seaborn', r, N)




