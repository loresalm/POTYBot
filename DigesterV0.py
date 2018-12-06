import statistics
import pandas as pd
from HACandleDigester import HACandleDigester
from MacdDigester import MacdDigester
 

class DigesterV0():
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
	def sendSignal(self,HASignal, MacdSignal):
		if HASignal == MacdSignal:
			return HASignal
		else:
			return 'HOLD'



	








		
