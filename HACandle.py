from binance.client import Client
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from Candles import Candles

class HACandles(Candles):
	# class variables:
	newCandle = []
	previousCandle = []
	candles_list = []
#################################################################################
	# constructor for the class Candles
	# the first candle is initialized with the Open, high, low, close prices 			 
	def __init__(self, Open, high, low, close):
		# Call the constructor of the Superclass
		# initializing the list format for the first candle
		# candles_list list composition: 
		# [[all the 'OPEN'],[all the 'HIGH'],[all the 'LOW'],[all the 'CLOSE']] 
		openList = [0]
		highList = [0]
		lowList = [0]
		closeList = [0]
		self.candles_list.append(openList)
		self.candles_list.append(highList)
		self.candles_list.append(lowList)
		self.candles_list.append(closeList)			 
		Candles.__init__(self)
		print "initializing the HACandles"		
		# initializing the first candle
		self.newCandle.append(Open)
		self.newCandle.append(high)
		self.newCandle.append(low)
		self.newCandle.append(close)

		# Heikin-Ashi Candle Calculations for the rest of time
		self.newCandle[0] = (Open + close) / 2
		self.newCandle[1] = high
		self.newCandle[2] = low
		self.newCandle[3] = (Open + high + low + close) / 4
		# store the first candle in order to build the next one
		self.previousCandle = self.newCandle
		# store the first candle in order to build and print the graphic
		self.candles_list[0][0] = self.newCandle[0]
		self.candles_list[1][0] = self.newCandle[1]
		self.candles_list[2][0] = self.newCandle[2]
		self.candles_list[3][0] = self.newCandle[3]
#################################################################################
	def CandleHA_Generator(self, Open, high, low, close):
		
		# generating the newCandle using the privous candle
		self.newCandle[0] = (self.previousCandle[0] + self.previousCandle[3]) / 2
		self.newCandle[3] = (Open + high + low + close) / 4
		self.newCandle[1] = max(high, self.newCandle[0], self.newCandle[3])
		self.newCandle[2] = min(low, self.newCandle[0], self.newCandle[3])
		# store the candle in order to build and print the graphic
		self.addCandleToCandleList(self.newCandle) 
		#store the candle in order to build the next one
		self.previousCandle.append(self.newCandle)	
#################################################################################
	def getLastHACandle(self):
		return self.newCandle
#################################################################################
	def getCandlesList(self):
		return self.candles_list









