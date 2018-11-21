#from binance.client import Client
#import pandas as pd
from Run import Run 
from Candle import Candles
import matplotlib.pyplot as plt



testRun = Run('ETHUSDT','15m','2018.11.17 00:00:00','2018.11.20 00:00:00')

#print testRun.getPriceList()

pricesList = testRun.getPriceList()
time = testRun.getTime()
heikinAshiCandleList = Candles(pricesList,time)

fig = plt.figure()
fig.canvas.set_window_title('Heikin-Ashi Candles')
HACandleGraph = fig.add_subplot(211)
priceHA = heikinAshiCandleList.getCandlesList()


for i in range(1,len(time)):
	#test the color of the candle is green 
	if priceHA[0][i]< priceHA[3][i]: 
		heikinAshiCandleList.drow(HACandleGraph, 'green', i)
	else:
		heikinAshiCandleList.drow(HACandleGraph, 'red', i)
plt.ylabel('PRICE')
plt.xlabel('TIME')
plt.legend()
plt.grid(True)
HACandleGraph.set_xlim(-0.5, len(time))
HACandleGraph.set_ylim(min(priceHA[2])-1,max(priceHA[1])+1)
plt.show()



