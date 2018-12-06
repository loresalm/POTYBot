import statistics
import pandas as pd
from termcolor import colored

class HACandleDigesterV2():

	# class variables:
	# candlesHistory:
	#	  it's a list with the last 3 candles with the format: 
        #      	  [0]lastCandle[1]secondLastCandle[2]tirdlastCandle
	candlesHistory = []
	# currentCandle: it's a list of the last 4 prices with the format:
	#		 [OPEN, HIGH, LOW, CLOSE]
	currentCandle = []

	currentSize = 0
	#list of the tree last candle size:
	#	[0]currentsize [1]lastsize[2]secondlastsize 
	sizes = []
#################################################################################
	#constructor for HADigester object:
	def __init__(self):
		print "Initiated HADigesterV2"
#################################################################################
#|1|	
	# set the currentCandle class variable with the prices and the currentSize  	
	def addHACandle(self, Open, high, low, close):
		self.currentCandle.append(Open)
		self.currentCandle.append(high)
		self.currentCandle.append(low)
		self.currentCandle.append(close)
		# set the current size of the current candle 
		self.currentSize = abs(self.currentCandle[0]-self.currentCandle[3])  
		# for the first three candles 
		if len(self.candlesHistory) < 3:
			self.candlesHistory.append(self.currentCandle)
			# generate sizes list 
			self.sizes.append(self.currentSize)
#################################################################################
#|2|
	# send one of the 3 possible signals: "BUY", "SELL","HOLD"
	# once de signal is send it calls the updateDigester method so make sure
	# to call the method addCandle before calling again this method 
	def sendHACandleSignal(self):
		if len(self.candlesHistory) == 3 and len(self.sizes) == 3:
			if self.candleColor(self.currentCandle) == "red" and self.candleColor(self.candlesHistory[0]) == "red" and self.currentSize>self.sizes[0] and self.currentCandle[0] == self.currentCandle[1]:
				self.updateHACandleDigester() 	
        			return "SELL"
			elif self.candleColor(self.currentCandle) == "green" and self.candleColor(self.candlesHistory[0]) == "green" and self.currentSize > self.sizes[0] and self.currentCandle[0] == self.currentCandle[2]:
				self.updateHACandleDigester() 	
        			return "BUY"
			else:
				self.updateHACandleDigester()
				print "Holds"
				return "HOLD"
#################################################################################
#|3|
	# update the candlesHistory : every candle is shifted by one position 
	#			      the first candle is now the currentCandle
	#			      the candlesHistory is always 3 
	#			      the currentCandle is now empty 
	def updateHACandleDigester(self):
		# check if the hisoty is ready and if the current candle is not too small:
		if len(self.candlesHistory) >= 3 and len(self.sizes) >=3:
			# update the candle history 
			self.candlesHistory[2] = self.candlesHistory[1]
			self.candlesHistory[1] = self.candlesHistory[0]
			self.candlesHistory[0] = self.currentCandle	
			# update the state history 
			self.sizes[2] = self.sizes[1]
			self.sizes[1] = self.sizes[0]
			self.sizes[0] = self.currentSize
		# make a reset 
		self.currentCandle = []	
#################################################################################
	def candleColor(self, Candle): 
		if Candle[0] < Candle[3]:
			return "green"
		else:
			return "red"
#################################################################################
	def colorDigest(self, newCandle, oldCandle):
		if self.candleColor(newCandle) == self.candleColor(oldCandle):
			return "stationary"
		elif self.candleColor(newCandle) == "red" and self.candleColor(oldCandle) == "green":
			return "bearish"
		else:
			return "bullish"


	








		
