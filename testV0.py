import time, sys
from Run import Run 
from HACandle import HACandles
from HACandleDigester import HACandleDigester
from Analyzer import Analyzer
import matplotlib.pyplot as plt
from ClassicCandles import ClassicCandles
from MacdDigester import MacdDigester
from MacdLine import MacdLine
from DigesterV0 import DigesterV0

testRun = Run('ETHUSDT','30m','2018.11.01 00:00:00','2018.11.02 00:00:00')
#get api data 
pricesList = testRun.getPriceList()
time = testRun.getTime()
#graph specifications
fig = plt.figure()
fig.canvas.set_window_title('graph')
plt.legend()
plt.grid(True)
#graph subplots
HACandleGraph = fig.add_subplot(311)
HACandleGraph.grid(True)
BUYSELLgraph = fig.add_subplot(313)
BUYSELLgraph.grid(True)
macdGraph = fig.add_subplot(312)
#data elaboration
ClassicCandles_ = ClassicCandles()
HACandles_ = HACandles(pricesList[0][0], pricesList[1][0], pricesList[2][0], pricesList[3][0]) 
macdLine = MacdLine()
#data digesters
HACandlesDigester_ = HACandleDigester()
macdDigest= MacdDigester(12,26,9)
digester = DigesterV0()
#analyzer
analys = Analyzer(10000,100,1.001)
#lists for plots limits
NewClassicCandle = []
HACandleList_ = []
ClassicCandleList_ = []
#go over all the pricesselected 
for i in time:
	#update the macdwith the new price
	macdLine.line(macdDigest.getMACDline(),macdDigest.getSignalLine())
	#prevent out of range for the last signal 
	if i == len(time)-1:
    		print u"\u001b[42;1m                      \u001b[0m"
    		print u"\u001b[42;1m        FINISH        \u001b[0m"
    		print u"\u001b[42;1m                      \u001b[0m"
    	else:
		#update the HACandles adding the last HACandle 
		HACandles_.CandleHA_Generator(pricesList[0][i], pricesList[1][i], pricesList[2][i], pricesList[3][i])
		NewHACandle = HACandles_.getLastHACandle()
		#update the ClassicCandles adding the last ClassicCandle 
		ClassicCandles_.CandleClassic_Generator(pricesList[0][i], pricesList[1][i], pricesList[2][i], pricesList[3][i])
		NewClassicCandl = ClassicCandles_.getLastClassicCandle()
		#draw the HACandles
		if(NewHACandle[0] > NewHACandle[3]):

			HACandles_.draw(NewHACandle,HACandleGraph,'red',i)	
		else:
			HACandles_.draw(NewHACandle,HACandleGraph,'green',i)
		#draw the ClassicCandles
		if(NewClassicCandl[0] > NewClassicCandl[3]):
			ClassicCandles_.draw(NewClassicCandl,BUYSELLgraph,'red',i)	
		else:
			ClassicCandles_.draw(NewClassicCandl,BUYSELLgraph,'green',i)
		#add the last candle to the digester
		HACandlesDigester_.addHACandle(NewHACandle[0], NewHACandle[1], NewHACandle[2], NewHACandle[3])
		#send the signal
		analys.signalAnalyzer(digester.sendSignal(HACandlesDigester_.sendHACandleSignal(),macdDigest.macdSignal(pricesList[3][i])),pricesList[0]
[i+1],time[i+1])

#analysis data		
analys.finalRapport()
analys.drawAnalyzer(BUYSELLgraph)
#draw the macdgraph
macdLine.drawLine(macdGraph, time)
#fix size of HACandlesgraph
HACandleList_ = HACandles_.getCandlesList()
HACandleGraph.set_xlim(-0.5, len(time))
HACandleGraph.set_ylim(min(HACandleList_[2])-1,max(HACandleList_[1])+1)
#fix size of classicCandlesgraph
BUYSELLgraph.set_xlim(-0.5, len(time))
BUYSELLgraph.set_ylim(min(pricesList[2])-1,max(pricesList[1])+1)

plt.show()



