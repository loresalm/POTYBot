
from Run import Run 
from MacdDigester import MacdDigester
from Analyzer import Analyzer
from MacdLine import MacdLine
import matplotlib.pyplot as plt

testRun = Run('ETHUSDT','15m','2018.10.01 00:00:00','2018.10.02 00:00:00')

pricesList = testRun.getPriceList()
time = testRun.getTime()

fig = plt.figure()
fig.canvas.set_window_title('Graph')
priceGraph= fig.add_subplot(211)
priceGraph.plot(time, pricesList[0],'r')
macdGraph= fig.add_subplot(212)

macdDigest= MacdDigester(12,26,9)
analys= Analyzer(10000,500,1.001)
macdLine= MacdLine()

for i in time:

	macdLine.line(macdDigest.getMACDline(),macdDigest.getSignalLine())

	if i== len(time)-1:
		print""
		print"FINISH"
		print""

	else:
		
		analys.signalAnalyzer(macdDigest.macdSignal(pricesList[3][i]),pricesList[0][i+1],time[i+1])


analys.finalRapport()

analys.drawAnalyzer(priceGraph)

macdLine.drawLine(macdGraph, time)

priceGraph.grid(True)
priceGraph.legend()
priceGraph.set_xlim(-0.5, len(time))
priceGraph.set_ylim(min(pricesList[2])-1,max(pricesList[1])+1)
plt.show()



