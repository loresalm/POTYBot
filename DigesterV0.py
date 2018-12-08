import statistics
import pandas as pd
from HACandleDigester import HACandleDigester
from MacdDigester import MacdDigester
 

class DigesterV0():
	signals = []
#################################################################################
	#constructor for Digester object:
	def __init__(self):
		print "Initiated HADigester"	
#################################################################################
	def sendSignal(HASignal, MacdSignal, ParabolicSarSignal):
		if(self,HASignal==MacdSignal or HASignal==ParabolicSarSignal):
			return HASignal
		elif(ParabolicSarSignal==MacdSignal):
			return ParabolicSarSignal
		else:
			return 'HOLD'
#################################################################################
	def sendSignal(self,MacdSignal):
		for i in range (0,len(self.signals)):
			if self.signals[i] == MacdSignal and MacdSignal!='HOLD':
				return self.signals[i]
		return 'HOLD'
#################################################################################
	def addSignals(self,HASignal):
		if len(self.signals)<5:
			self.signals.append(HASignal)
		else:
			del self.signals[0]
			self.signals.append(HASignal)			
		



	








		
