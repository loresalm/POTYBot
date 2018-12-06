from binance.client import Client
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

class Candles():
#################################################################################
	def __init__(self):
		print "initializing the Candles"
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
	def addCandleToCandleList(self,candle):
		self.candles_list[0].append(candle[0])
		self.candles_list[1].append(candle[1])
		self.candles_list[2].append(candle[2])
		self.candles_list[3].append(candle[3])
#################################################################################
	def draw(self,HACandleGraph, color, dt):
		verts = self.vertsCreator(dt)
		codes = self.codesCreator()
		path = Path(verts, codes)
		patch = patches.PathPatch(path, facecolor= color, lw=0.2)
		HACandleGraph.add_patch(patch)
		










	
