

class MacdLine():

	macdLine= []
	macdSignal= []
	low= 0
	high= 0

	def __init__(self):
		print""

	def line(self,_macdLine,_macdSignal):

		self.macdLine.append(_macdLine)
		self.macdSignal.append(_macdSignal)

		if (_macdLine> self.high) or (_macdSignal> self.high):
			if self.macdLine>_macdSignal:
				self.high= _macdLine
			else:
				self.high= _macdSignal

		if (_macdLine< self.low) or (_macdSignal< self.low):
			if _macdLine<_macdSignal:
				self.low= _macdLine
			else:
				self.low= _macdSignal

	def drawLine(self, graphic, time):
		graphic.plot(time,self.macdLine,'r', label= 'macdLine' )
		graphic.plot(time,self.macdSignal,'g', label= 'macdSignal')
		graphic.legend()
		graphic.grid(True)
		graphic.set_ylim(self.low, self.high)


