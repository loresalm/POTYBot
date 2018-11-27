from Run import Run 
from ParabolicSAR import ParabolicSAR
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches



testRun = Run('ETHUSDT','1d','2018.06.15 00:00:00','2018.11.01 00:00:00')

pricesList = testRun.getPriceList()
time = testRun.getTime()

SAR= ParabolicSAR(pricesList[0][0], pricesList[1][0],pricesList[2][0],pricesList[3][0]) 

fig, ax = plt.subplots()

for i in range(0,len(time)):

	if pricesList[3][i]< pricesList[0][i]: 

		verts = [
		(time[i],pricesList[3][i]),
		(time[i]-0.1,pricesList[3][i]), 			
		(time[i]-0.1,pricesList[1][i]),  
		(time[i]-0.105,pricesList[1][i]),

		(time[i]-0.105,pricesList[3][i]),
		(time[i]-0.2,pricesList[3][i]),
		(time[i]-0.2,pricesList[0][i]),
		(time[i]-0.105,pricesList[0][i]),
		(time[i]-0.105,pricesList[2][i]),
		(time[i]-0.1,pricesList[2][i]),
		(time[i]-0.1,pricesList[0][i]),
		(time[i],pricesList[0][i]),
		(time[i],pricesList[3][i]),
		]
		
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

		path = Path(verts, codes)
		patch = patches.PathPatch(path, facecolor='red', lw=0.2)
		ax.add_patch(patch)

	else:
		verts = [
		(time[i],pricesList[3][i]),
		(time[i]-0.1,pricesList[3][i]), 			
		(time[i]-0.1,pricesList[2][i]),  
		(time[i]-0.105,pricesList[2][i]),
		(time[i]-0.105,pricesList[3][i]),
		(time[i]-0.2,pricesList[3][i]),
		(time[i]-0.2,pricesList[0][i]),
		(time[i]-0.105,pricesList[0][i]),
		(time[i]-0.105,pricesList[1][i]),
		(time[i]-0.1,pricesList[1][i]),
		(time[i]-0.1,pricesList[0][i]),
		(time[i],pricesList[0][i]),
		(time[i],pricesList[3][i]),
		]

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

		path = Path(verts, codes)
		patch = patches.PathPatch(path, facecolor='green', lw=0.2)
		ax.add_patch(patch)


for i in range(1,len(time)):

	SAR.parabolicSAR(pricesList[1][i], pricesList[2][i])




plt.plot(time, SAR.getParabolicSAR(),'4')
plt.grid(True)
ax.set_xlim(-0.5, len(time))
ax.set_ylim(min(pricesList[2])-1,max(pricesList[1])+1)
plt.show()



