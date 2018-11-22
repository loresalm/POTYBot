

class MacdDigester():

	Short= 0
	Long= 0
	Signal= 0

	MACD= 0
	MACDstate= 1
	MACDstateLast= 0 #state of last mesuorments used for crossovers
	state= 0 #0 ready to buy, 1 ready to sell

#used to calculate MovingAvarageConvergenceDivergence
	#12-exponential moving avarage
	lastShort= []
	EMAShort= 0

	#26-exponential moving avarage
	lastLong= []
	EMALong= 0

	#9-exponential moving avarage
	lastSignal= []
	EMASignal= 0

	#the two lines
	MACDline= 0
	SignalLine= 0






	def __init__(self, _short, _long, _signal):

		self.Short= _short
		self.Long=  _long
		self.Signal=  _signal

	def updateMacd(self, price):

		#MACD is calculated : MACDline- SignalLine
				#MACDline is 12EMA-26EMA
				#SignalLine is 9EMA of MACD

		#getting 12ExponentialMovingAvarage
		#First 12times just get data
		if len(self.lastShort)< self.Short:
			self.lastShort.append(price)
			#compute StandartMovingAvarage from first 12 prices
		if len(self.lastShort)== self.Short:
			del self.lastShort[0] # remove oldes
			self.lastShort.append(price) # add current price
			summ= 0
			for i in self.lastShort:
				summ+= i
			self.EMAShort=summ/ self.Short; # get avarage of last 12 

		#same thing as for 12EMA
		if len(self.lastLong)< self.Long:
			self.lastLong.append(price)

		if len(self.lastLong)== self.Long:
			del self.lastLong[0]
			self.lastLong.append(price)
			summ= 0
			for i in self.lastLong:
				summ+= i
			self.EMALong=summ/ self.Long;


        #if data of last 26 times is here:
		if(self.EMALong!= 0):

			#compute 9EMA but instead of price use MACDline
			if len(self.lastSignal)< self.Signal:
				self.lastSignal.append(float(self.EMAShort- self.EMALong))  #EMA12-EMA26 = MACDline

			if len(self.lastSignal)== self.Signal:
				del self.lastSignal[0]
				self.lastSignal.append(float(self.EMAShort- self.EMALong))
				summ= 0
				for i in self.lastSignal:
					summ+= i
				self.EMASignal=summ/ self.Signal;



		#if data for EMA9 is here 
		if(self.EMASignal!= 0):
			#compute 9EMA but instead of price use MACDline
			if len(self.lastSignal)< self.Signal:
				self.lastSignal.append(float(self.EMAShort- self.EMALong))  #EMA12-EMA26 = MACDline

			if len(self.lastSignal)== self.Signal:
				del self.lastSignal[0]
				self.lastSignal.append(float(self.EMAShort- self.EMALong))
				summ= 0
				for i in self.lastSignal:
					summ+= i
				self.EMASignal=summ/ self.Signal;

		#if data for EMA9 is here 
		if(self.EMASignal!= 0):

			#get lines
			self.MACDline= self.EMAShort- self.EMALong
			self.SignalLine= self.EMASignal

		#get MACD by applying formula
		self.MACD= self.MACDline- self.SignalLine;
		
		return self.MACD

	def macdSignal(self, price):
		#check if bullish or bearish
		if(self.updateMacd(price)> 0):
			self.MACDstate= 1

		else:
			self.MACDstate= 0

		#state 0 -> wants to buy
		if self.state== 0:  
			#check for MACD crossover
			if self.MACDstate!= self.MACDstateLast :
				#update latest MACD
				self.MACDstateLast= self.MACDstate
				#set state to be ready to sell
				self.state= 1
				return "BUY"
		#state 1 -> wants to sell
		if self.state== 1:
			#check for MACD crossover
			if self.MACDstate!= self.MACDstateLast  :
				#update MACD
				self.MACDstateLast= self.MACDstate
				#set state back to for next buy
				self.state= 0
				return "SELL"
		#set current MACD state to be Last in next round
		self.MACDstateLast= self.MACDstate

			
		return "HOLD"

	def getMACDline(self):
		return self.MACDline

	def getSignalLine(self):
		return self.SignalLine


		

		























			
			