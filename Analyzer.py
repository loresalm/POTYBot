
class Analyzer():
	fee= 0
	startBalance= 0
	quantityBuy= 0
	balance= 0
	investment= 0
	highestGain= 0
	highestGainTime= 0
	highestLost= 0
	highestLostTime= 0
	trade=0
	profit=0
	tradeAverage= []
	lastTrade= "SELL"

	buyPrice= []
	buyTime= []
	sellPrice= []
	sellTime= []

	def __init__(self,_startBalance,_quantityBuy,_fee):
		self.startBalance= _startBalance
		self.balance= _startBalance
		self.fee= _fee
		self.quantityBuy= _quantityBuy

	def signalAnalyzer(self,signal,price,time):

		if signal== "BUY":
			self.investment=(self.quantityBuy/price)* self.fee
			self.balance=float(self.balance)- self.quantityBuy
			print" "
			print "BUY ", price, "TIME ",time, "WALLET ", self.balance
			self.buyPrice.append(price)
			self.buyTime.append(time)

			self.lastTrade= "BUY"

		if signal== "SELL":
			self.trade=(self.investment*price)* self.fee
			self.profit=(self.trade/self.quantityBuy)*100-100
			self.tradeAverage.append(self.profit) 
			self.balance+= self.trade
			print "SELL", price, "TIME ", time, "WALLET ", self.balance, "PROFIT ", self.profit, "%"
			self.sellPrice.append(price)
			self.sellTime.append(time)

			if self.trade-self.quantityBuy> self.highestGain:
				self.highestGain= self.trade-self.quantityBuy
				self.highestGainTime= time
			if self.trade-self.quantityBuy< self.highestLost:
				self.highestLost= self.trade-self.quantityBuy
				self.highestLostTime= time

			self.lastTrade= "SELL"

	def drawAnalyzer(self, graphics):
		graphics.plot(self.buyTime, self.buyPrice,'d',label= 'Buy')
		graphics.plot(self.sellTime, self.sellPrice,'d',label= 'Sell')
		graphics.legend()

	def finalRapport(self):
		
		average=0
		if self.lastTrade== "BUY":
			 self.balance+= self.quantityBuy 
		print "StartBalance ", self.startBalance, "FinalBalance ", self.balance, "Gain ", (self.balance/ self.startBalance)*100-100, "%"
		print" "
		print "HighestGain ", self.highestGain, "HighestGainTime ", self.highestGainTime
		print" "
		print "HighestLost ", self.highestLost, "HighestLostTime ", self.highestLostTime
		print" "
		for i in range(0,len(self.tradeAverage)):
			average+= self.tradeAverage[i]
		print "TradeAverage ", average/len(self.tradeAverage), "%"




















