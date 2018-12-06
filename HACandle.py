from binance.client import Client
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
#from Candles import Candles

class HACandles():
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
		#Candles.__init__(self)
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
		#print 'BEFORE', self.previousCandle
		# generating the newCandle using the privous candle
		self.newCandle[0] = (self.previousCandle[0] + self.previousCandle[3]) / 2
		self.newCandle[3] = (Open + high + low + close) / 4
		self.newCandle[1] = max(high, self.newCandle[0], self.newCandle[3])
		self.newCandle[2] = min(low, self.newCandle[0], self.newCandle[3])
		# store the candle in order to build and print the graphic
		self.addCandleToCandleList(self.newCandle) 
		#store the candle in order to build the next one
		self.previousCandle = []
		self.previousCandle = self.newCandle
		#print 'SIZE', (self.newCandle[0]-self.newCandle[3])
		#print 'AFTER', self.previousCandle	
#################################################################################
	def getLastHACandle(self):
		return self.newCandle
#################################################################################
	def getCandlesList(self):
		return self.candles_list
#################################################################################
	def vertsCreator(self,candle,dt):

		if candle[3]> candle[0]:
			verts = [
				(dt,candle[3]),
				(dt-0.4,candle[3]), 			
				(dt-0.4,candle[1]),  
				(dt-0.405,candle[1]),
				(dt-0.405,candle[3]),
				(dt-0.8,candle[3]),
				(dt-0.8,candle[0]),
				(dt-0.405,candle[0]),
				(dt-0.405,candle[2]),
				(dt-0.4,candle[2]),
				(dt-0.4,candle[0]),
				(dt,candle[0]),
				(dt,candle[3]),
				]
			return verts
		else:
			verts = [
				(dt,candle[3]),
				(dt-0.4,candle[3]), 			
				(dt-0.4,candle[2]),  
				(dt-0.405,candle[2]),
				(dt-0.405,candle[3]),
				(dt-0.8,candle[3]),
				(dt-0.8,candle[0]),
				(dt-0.405,candle[0]),
				(dt-0.405,candle[1]),
				(dt-0.4,candle[1]),
				(dt-0.4,candle[0]),
				(dt,candle[0]),
				(dt,candle[3]),
				]
			return verts

#################################################################################
	def codesCreator(self):
		codes = [
			Path.MOVETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.LINETO,
			Path.CLOSEPOLY,
			]
		return codes
#################################################################################
	def draw(self,candle,HACandleGraph, color, dt):
		verts = self.vertsCreator(candle,dt)
		codes = self.codesCreator()
		path = Path(verts, codes)
		patch = patches.PathPatch(path, facecolor= color, lw=0.2)
		HACandleGraph.add_patch(patch)
#################################################################################
	def addCandleToCandleList(self,candle):
		self.candles_list[0].append(candle[0])
		self.candles_list[1].append(candle[1])
		self.candles_list[2].append(candle[2])
		self.candles_list[3].append(candle[3])
		










