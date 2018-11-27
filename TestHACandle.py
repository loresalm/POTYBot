
from Run import Run 
from HACandle import HACandles
from HACandleDigester import HACandleDigester
from Analyzer import Analyzer
import matplotlib.pyplot as plt



testRun = Run('ETHUSDT','1d','2018.09.17 00:00:00','2018.11.25 00:00:00')

#print testRun.getPriceList()

pricesList = testRun.getPriceList()
time = testRun.getTime()
fig = plt.figure()
fig.canvas.set_window_title('graph')
HACandleGraph = fig.add_subplot(211)
BUYSELLgraph = fig.add_subplot(212)

HACandles_ = HACandles(pricesList[0][0], pricesList[1][0], pricesList[2][0], pricesList[3][0], time[0]) 


HACandlesDigester_ = HACandleDigester()

analys = Analyzer(10000,100,1.001)

for i in range(1, len(time)):

	if i== len(time)-1:
    		print""
    		print"FINISH"
    		print""
   	else:
		HACandles_.CandleHA_Generator(pricesList[0][i], pricesList[1][i], pricesList[2][i], pricesList[3][i], time[i])
		HACandleList_ = HACandles_.getCandlesList()

		if(HACandleList_[0][i] > HACandleList_[3][i]):
			HACandles_.draw(HACandleGraph,'red',i)	
		else:
			HACandles_.draw(HACandleGraph,'green',i)

		HACandlesDigester_.addHACandle(HACandleList_[0][i], HACandleList_[1][i], HACandleList_[2][i], HACandleList_[3][i])
	
		analys.signalAnalyzer(HACandlesDigester_.sendHACandleSignal(),pricesList[0][i+1],time[i+1])
		
analys.finalRapport()
analys.drawAnalyzer(HACandleGraph)
plt.ylabel('PRICE')
plt.xlabel('TIME')
plt.legend()
plt.grid(True)
HACandleGraph.set_xlim(-0.5, len(time))
HACandleGraph.set_ylim(min(HACandleList_[2])-1,max(HACandleList_[1])+1)
plt.show()



