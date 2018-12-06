from binance.client import Client
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
#from Candles import Candles

class ClassicCandles():
	# class variables:
	newCandle = []
	candles_list = []
#################################################################################
	# constructor for the class Candles
	# the first candle is initialized with the Open, high, low, close prices 			 
	def __init__(self):
		# Call the constructor of the Superclas			 
		#Candles.__init__(self)
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
		print  "before",self.candles_list[0][0]
		if self.candles_list[0][0]==0:
			del self.candles_list[0][0]
			del self.candles_list[1][0]
			del self.candles_list[2][0]
			del self.candles_list[3][0]
		return self.candles_list
#################################################################################
	def vertsCreator(self,dt):
		verts = [
			(dt,self.candles_list[3][dt]),
			(dt-0.1,self.candles_list[3][dt]), 			
			(dt-0.1,self.candles_list[1][dt]),  
			(dt-0.105,self.candles_list[1][dt]),
			(dt-0.105,self.candles_list[3][dt]),
			(dt-0.2,self.candles_list[3][dt]),
			(dt-0.2,self.candles_list[0][dt]),
			(dt-0.105,self.candles_list[0][dt]),
			(dt-0.105,self.candles_list[2][dt]),
			(dt-0.1,self.candles_list[2][dt]),
			(dt-0.1,self.candles_list[0][dt]),
			(dt,self.candles_list[0][dt]),
			(dt,self.candles_list[3][dt]),
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
	def draw(self,HACandleGraph, color, dt):
		verts = self.vertsCreator(dt)
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






	
