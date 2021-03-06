import statistics
import pandas as pd
from termcolor import colored

class HACandleDigester():

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
		print "Initiated HADigester"
#################################################################################
#|1|	
	# set the currentCandle class variable with the prices   	
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
################################################################################# print colored('curr', 'red'),
#|2|
	# send one of the 3 possible signals: "BUY", "SELL","HOLD"
	# once de signal is send it calls the updateDigester method so make sure
	# to call the method addCandle before calling again this method 
	def sendHACandleSignal(self):
		# check if the hisoty is ready and if the current candle is not too small:
		if len(self.candlesHistory) == 3:
			if self.currentSize > min(self.sizes):
				# check if the we are in a green green or red red situation
				if self.colorDigest(self.candlesHistory[0], self.candlesHistory[1]) == "stationary":
					# check if the price is changing and going down green green->red
					if self.colorDigest(self.currentCandle, self.candlesHistory[0]) == "bearish":
						self.candleColor(self.candlesHistory[1]),					
						self.updateHACandleDigester() 	
        					return "SELL"
					# check if the price is changing and going up red red->green
					elif self.colorDigest(self.currentCandle, self.candlesHistory[0]) == "bullish":
						self.updateHACandleDigester()
						return "BUY"
					else:
						#the price is constant 
						self.updateHACandleDigester()
						return "HOLD"
				else:
					# we have not green green or red red 
					self.updateHACandleDigester()	
					return "HOLD"
			else:
				self.updateHACandleDigester()	
				return "HOLD"

		else:
			self.updateHACandleDigester()	
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
		self.currentState = []		
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


	








		
