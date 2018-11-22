import statistics
import pandas as pd

class HACandleDigester():

	# class variables:
	# candlesHistory:
	#	  it's a list with 3 candles with the format: 
        #      	  [0]lastCandle[1]secondLastCandle[2]tirdlastCandle
	candlesHistory = []
	# currentCandle: it's a list of 4 prices with the format:
	#		 [OPEN, HIGH, LOW, CLOSE]
	currentCandle = [] 
#################################################################################
	#constructor for Digester object:
	def __init__(self):
		print "Initiated Digester"
#################################################################################
	# set the currentCandle class variable with the prices   	
	def addHACandle(self, Open, high, low, close):
		self.currentCandle.append(Open)
		self.currentCandle.append(high)
		self.currentCandle.append(low)
		self.currentCandle.append(close)
#################################################################################
	# update the candlesHistory : every candle is shifted by one position 
	#			      the first candle is now the currentCandle
	#			      the candlesHistory is always 3 
	#			      the currentCandle is now empty 
	def updateHACandleDigester(self):
		if len(self.candlesHistory) < 3:
			self.candlesHistory.append(self.currentCandle)
		else:
			self.candlesHistory[2] = self.candlesHistory[1]
			self.candlesHistory[1] = self.candlesHistory[0]
			self.candlesHistory[0] = self.currentCandle
		self.currentCandle = []
#################################################################################
	# send one of the 3 possible signals: "BUY", "SELL","HOLD"
	# once de signal is send it calls the updateDigester method so make sure
	# to call the method addCandle before calling again this method 
	def sendHACandleSignal(self):
		if len(self.candlesHistory) == 3:
			if self.colorDigest(self.currentCandle,self.candlesHistory[0]) == 'RedGreen':
				self.updateHACandleDigester()
				return "BUY"
			elif self.colorDigest(self.currentCandle,self.candlesHistory[0]) == 'GreenRed':
				self.updateHACandleDigester() 
        			return "SELL"
			else:
				self.updateHACandleDigester()
				return "HOLD"
		else:
			self.updateHACandleDigester()	
			return "HOLD"		
#################################################################################
	def candleColor(self, Candle): 
		if Candle[0] < Candle[3]:
			return "green"
		else:
			return "red"
#################################################################################
	def colorDigest(self, newCandle, oldCandle):
		if self.candleColor(newCandle) == self.candleColor(oldCandle):
			return 'Same'
		elif self.candleColor(newCandle) == 'red' and self.candleColor(oldCandle) == 'green':
			return 'RedGreen'
		else:
			return 'GreenRed'


	








		
