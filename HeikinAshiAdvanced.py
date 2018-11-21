#bullish = crescente 
#bearish = decrescente 
from binance.client import Client
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
	########################################################################
def Heikin_Ashi_Candle(price,time):
	#priceHA list composition: [[all the 'OPEN'],[all the 'HIGH'],[all the 'LOW'],[all the 'CLOSE']]
	priceHA=[price[0],price[1],price[2],price[3]]
 	#Heikin-Ashi Candle Calculations on First Run
	priceHA[0][0]= (price[0][0] + price[3][0]) / 2
	priceHA[1][0]= price[1][0]
	priceHA[2][0]= price[2][0]
	priceHA[3][0]= (price[0][0] + price[1][0] + price[2][0] + price[3][0]) / 4
	#Heikin-Ashi Candle Calculations for the rest of time
	for i in range(1, len(time)):
		priceHA[0][i]= (priceHA[0][i-1] + priceHA[3][i-1]) / 2
		priceHA[3][i]= (price[0][i] + price[1][i] + price[2][i] + price[3][i]) / 4
		priceHA[1][i]= max(price[1][i],priceHA[0][i],priceHA[3][i])
		priceHA[2][i]= min(price[2][i],priceHA[0][i],priceHA[3][i])
	return priceHA
########################################################################
def vertsCreator(priceHA,dt):
	verts = [
		(time[dt],priceHA[3][dt]),
		(time[dt]-0.1,priceHA[3][dt]), 			
		(time[dt]-0.1,priceHA[1][dt]),  
		(time[dt]-0.105,priceHA[1][dt]),
		(time[dt]-0.105,priceHA[3][dt]),
		(time[dt]-0.2,priceHA[3][dt]),
		(time[dt]-0.2,priceHA[0][dt]),
		(time[dt]-0.105,priceHA[0][dt]),
		(time[dt]-0.105,priceHA[2][dt]),
		(time[dt]-0.1,priceHA[2][dt]),
		(time[dt]-0.1,priceHA[0][dt]),
		(time[dt],priceHA[0][dt]),
		(time[dt],priceHA[3][dt]),
		]
	return verts
########################################################################
def codesCreator():
	codes = [
		Path.MOVETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.CLOSEPOLY,
		]
	return codes
########################################################################
def drow(HACandleGraph, color, dt):
		verts = vertsCreator(priceHA,dt)
		codes = codesCreator()

		path = Path(verts, codes)
		patch = patches.PathPatch(path, facecolor= color, lw=0.2)
		HACandleGraph.add_patch(patch)
########################################################################
client= Client("", "")

coin= client.get_historical_klines(symbol= 'ETHUSDT', interval= '15m', start_str= '2018.11.17 00:00:00')
coin_tb= pd.DataFrame(coin, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
time_tb= pd.to_datetime(coin_tb['Open time'], unit='ms')
#price list format 
price = [['Open'],['High'],['Low'],['Close']]
#fills the price list according to the format described above
for i in range(0,4): 
	price[i]= coin_tb[price[i][0]].astype(float)
#fills the list with all the time steps
time= []
for i in range(0,len(time_tb)):
	time.append(i)

buyTime= []
buyPrice= []
sellTime= [] 
sellPrice= []
priceHA = Heikin_Ashi_Candle(price,time) 

fig = plt.figure()
fig.canvas.set_window_title('Heikin-Ashi Candles')
HACandleGraph = fig.add_subplot(211)
#config for the start of the simulation
wallet=1000
crypto=0
bullish= False
bearish= False

minEarn= 10000000
maxEarn= 0
#start the simulation i = step of time 
for i in range(1,len(time)):
	#test the color of the candle is green 
	if priceHA[0][i]< priceHA[3][i]: 
		drow(HACandleGraph, 'green', i)
		#test the phase
		if (priceHA[0][i-1]<priceHA[3][i-1]) and (priceHA[0][i]-priceHA[3][i]>0.002) and (priceHA[0][i-1]-priceHA[3][i-1]>0.002):

			bullish= True
			if bearish==True:
				wallet-=500*1.001
				crypto+=500/price[0][i+1]
				print "buy","{",time[i+1],"}", wallet
				buyTime.append(time[i+1])
				buyPrice.append(price[0][i+1])
				bearish=False
	#the color of the candle must be red
	else:
		drow(HACandleGraph, 'red', i)
		#test the phase
		if (priceHA[0][i-1]>priceHA[3][i-1]) and (priceHA[0][i]-priceHA[3][i]>0.002) and (priceHA[0][i-1]-priceHA[3][i-1]>0.002):

			bearish=True
			if bullish==True:
				if crypto*price[3][i]- ((price[3][i]* crypto)* 0.001)< minEarn:
					minEarn= crypto*price[3][i]- ((price[3][i]* crypto)* 0.001)
					timeMin= time[i]


				if crypto*price[3][i]- ((price[3][i]* crypto)* 0.001)> maxEarn:
					maxEarn= crypto*price[3][i]- ((price[3][i]* crypto)* 0.001)
					timeMax= time[i]
						

				wallet+=crypto*price[0][i+1]- ((price[0][i+1]* crypto)* 0.001)
				crypto-=crypto
				print "sell","{",time[i],"}", wallet
				sellTime.append(time[i+1])
				sellPrice.append(price[0][i+1])
				bullish=False

if wallet<500:
	wallet+=500

earn= wallet-1000

print "wallet str:",1000, "wallet end:",wallet,"investimento:", 500
print "earn:",earn 
#print "max earn", maxEarn -500, timeMax 
#print "min earn", minEarn -500, timeMin
					
				



plt.plot(buyTime,buyPrice,'d',label= 'Buy')
plt.plot(sellTime, sellPrice,'d',label= 'Sell')
plt.ylabel('PRICE')
plt.xlabel('TIME')
plt.legend()
plt.grid(True)

HACandleGraph.set_xlim(-0.5, len(time))
HACandleGraph.set_ylim(min(price[2])-1,max(price[1])+1)
plt.show()






