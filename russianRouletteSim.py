import random
import math
from statistics import mean
import statistics
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats as stats
import pylab as pl

## Creates our gun
def spinRevolver():
    spin = random.randint(1,6)
    if spin == 6:
        #print(spin,'Loss')
        return False
    else:
        #print(spin, 'Win')
        return True
    
   

# creates the russian roulette game
def russianRoulette(gameLength):
    currentRound = 0
    x = []
    y = []
    live = 0
    #wager = initialWager
    while (currentRound <= gameLength) and (live >= 0):
        if spinRevolver():
            live = 1
            #funds += wager
        else:
            live = -1
            #funds = 0
        x.append(currentRound)
        #y.append(funds)
        currentRound += 1
    #plt.plot(x,y)
    return (currentRound)

# creates our simulator, visualizations, and statistics
def simRussianRoulette(playerCount,gameLength):
    x = 0
    lifeSpan = []
    while x < playerCount:
        lifeSpan.append(russianRoulette(gameLength))
        x+=1
    df = pd.DataFrame(lifeSpan)
    #plt.ylabel('Funds')
    #plt.xlabel('Game Length')
    #plt.show()
    ls = sorted(lifeSpan)
    fit = stats.norm.pdf(ls, np.mean(ls), np.std(ls))
    #mn = mean(lifeSpan)
    #std = statistics.stdev(lifeSpan)
    # Mean = 0, SD = 2.
    pl.plot(ls,fit,'-o')

    pl.hist(ls,normed=True) 
    #plt.plot(lifeSpan, norm.pdf(lifeSpan,mn,std))
    #plt.savefig('RRSim.png',dpi=800)
    pl.savefig('RRSim.png',dpi=800)
    print(df.describe())
    #print(df.describe())
    
playerCount = input("How many players? (int)")
gameLength = input("Maximum number of rounds? (int)")
playerCount = int(playerCount)
gameLength = int(gameLength)
simRussianRoulette(playerCount,gameLength)
