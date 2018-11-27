
class ParabolicSAR():

	previousSar= 0  
	currentSar= 0
	extremePoint= 0  #The highest high of the current uptrend or the lowest low of the current downtrend. 

	accelerationFactor= 0  #Determines the sensitivity of the SAR.

	parabolicSARdata= []


	bearish= False
	bullish= False

	def __init__(self, Open, high, low, Close):

		if Open > Close: 
			self.extremePoint= low
			self.accelerationFactor= 0.2
			self.previousSar= high + 10.5
			self.parabolicSARdata.append(self.previousSar)
			self.bearish= True 

		else: 
			self.extremePoint= high
			self.accelerationFactor= 0.2
			self.previousSar= low - 10.5			
			self.parabolicSARdata.append(self.previousSar)						
			self.bullish= True 

	def parabolicSAR(self, high, low):

		if self.bullish== True:

			self.risingParabolicSAR()

			if high> self.extremePoint:
					self.extremePoint= high
					self.accelerationFactor+= 0.2


			if low> self.currentSar:
				self.parabolicSARdata.append(self.currentSar)
				self.previousSar= self.currentSar			
				
				
			else:
				self.previousSar= self.extremePoint
				self.parabolicSARdata.append(self.previousSar)
				self.extremePoint= low
				self.accelerationFactor= 0.2
				self.bullish= False
				self.bearish= True

				return 


				
		if self.bearish== True:

			self.fallingParabolicSAR()
			
			if low< self.extremePoint:
				self.extremePoint= low
				self.accelerationFactor+= 0.2	

			if high< self.currentSar:
				self.parabolicSARdata.append(self.currentSar)
				self.previousSar= self.currentSar	

			else:
				self.previousSar= self.extremePoint
				self.parabolicSARdata.append(self.previousSar)
				self.extremePoint= high
				self.accelerationFactor= 0.2
				self.bullish= True
				self.bearish= False

				return
							

		
	def risingParabolicSAR(self):
		self.currentSar= self.previousSar + self.accelerationFactor*(self.extremePoint- self.previousSar)

	def fallingParabolicSAR(self):
		self.currentSar= self.previousSar - self.accelerationFactor*(self.previousSar- self.extremePoint)

	def getParabolicSAR(self):
		return self.parabolicSARdata
