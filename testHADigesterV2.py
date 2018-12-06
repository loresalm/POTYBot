
from Run import Run 
from HACandle import HACandles
from HACandleDigesterV2 import HACandleDigesterV2
from Analyzer import Analyzer
import matplotlib.pyplot as plt
from ClassicCandles import ClassicCandles
from MacdDigester import MacdDigester
from MacdLine import MacdLine




testRun = Run('ETHUSDT','30m','2018.11.21 00:00:00','2018.11.25 00:00:00')

#print testRun.getPriceList()

pricesList = testRun.getPriceList()
time = testRun.getTime()
fig = plt.figure()
fig.canvas.set_window_title('graph')

HACandleGraph = fig.add_subplot(311)
BUYSELLgraph = fig.add_subplot(313)
macdGraph = fig.add_subplot(312)

#plt.ylabel('PRICE')
#plt.xlabel('TIME')
plt.legend()

HACandleGraph.grid(True)
BUYSELLgraph.grid(True)
macdGraph

ClassicCandles_ = ClassicCandles()
HACandles_ = HACandles(pricesList[0][0], pricesList[1][0], pricesList[2][0], pricesList[3][0]) 
macdLine = MacdLine()

HACandlesDigester_ = HACandleDigesterV2()
macdDigest= MacdDigester(12,26,9)

analys = Analyzer(10000,100,1.001)

NewClassicCandle = []
HACandleList_ = []
ClassicCandleList_ = []

for i in time:
	print ("time step ", time[i])

	macdLine.line(macdDigest.getMACDline(),macdDigest.getSignalLine())

	if i == len(time)-1:
    		print""
    		print"FINISH"
    		print""

    	else:
		HACandles_.CandleHA_Generator(pricesList[0][i], pricesList[1][i], pricesList[2][i], pricesList[3][i])
		NewHACandle = HACandles_.getLastHACandle()
		

		ClassicCandles_.CandleClassic_Generator(pricesList[0][i], pricesList[1][i], pricesList[2][i], pricesList[3][i])
		NewClassicCandl = ClassicCandles_.getLastClassicCandle()

		if(NewHACandle[0] > NewHACandle[3]):

			HACandles_.draw(NewHACandle,HACandleGraph,'red',i)	
		else:
			HACandles_.draw(NewHACandle,HACandleGraph,'green',i)

		if(NewClassicCandl[0] > NewClassicCandl[3]):
			ClassicCandles_.draw(BUYSELLgraph,'red',i)	
		else:
			ClassicCandles_.draw(BUYSELLgraph,'green',i)
		signal = macdDigest.macdSignal(pricesList[3][i])		

		HACandlesDigester_.addHACandle(NewHACandle[0], NewHACandle[1], NewHACandle[2], NewHACandle[3])
	
		analys.signalAnalyzer(HACandlesDigester_.sendHACandleSignal(),pricesList[0][i+1],time[i+1])
plt.grid(True)
		
analys.finalRapport()
analys.drawAnalyzer(BUYSELLgraph)

macdLine.drawLine(macdGraph, time)

plt.legend()

HACandleList_ = HACandles_.getCandlesList()
HACandleGraph.set_xlim(-0.5, len(time))
HACandleGraph.set_ylim(min(HACandleList_[2])-1,max(HACandleList_[1])+1)

BUYSELLgraph.set_xlim(-0.5, len(time))

BUYSELLgraph.set_ylim(min(pricesList[2])-1,max(pricesList[1])+1)
plt.show()



