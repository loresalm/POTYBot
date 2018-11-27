from binance.client import Client
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from Candles import Candles

class ClassicCandles(Candles):
	# class variables:
	newCandle = []
	candles_list = []
#################################################################################
	# constructor for the class Candles
	# the first candle is initialized with the Open, high, low, close prices 			 
	def __init__(self):
		# Call the constructor of the Superclas			 
		Candles.__init__(self)
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
		print "initializing the ClassicCandles"	
		self.newCandle = [0]*4
#################################################################################
	def CandleClassic_Generator(self, Open, high, low, close):
		self.newCandle[0] = Open
		self.newCandle[1] = high
		self.newCandle[2] = low
		self.newCandle[3] = close
		self.addCandleToCandleList(self.newCandle)
#################################################################################
	def getLastClassicCandle(self):
		return self.newCandle
#################################################################################
	def getCandlesList(self):
		return self.candles_list






	
