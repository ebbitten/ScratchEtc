'''
This will be a library of all the functions I might want while operating stockFighter

v1.1 Move the market object to a class
v1.2 start using the requests framework
v1.3 going to start incorporating some business logic
'''
global apikey,base_url,header
apikey = '7791d4b66cea4c0fd94b15150300fc378c085074'
base_url = 'https://api.stockfighter.io/ob/api'
#authenticate
header = {'X-Starfighter-Authorization': apikey}
# import libraries
import requests
import json


class starMarket(object):
    def __init__(self,venues,stock,account):
        self.venues=venues
        self.stock=stock
        self.account=account
    def orderStock(self, price, qty, direction = 'buy', orderType = 'limit'):
        #Should handle buys/sells of all order types. Default to buy and limit
        # put price, qty, direction, orderType into dictionary
        data={}
        data['price']=price
        data['qty']=qty
        data['direction']=direction
        data['orderType']=orderType
        data['account']=self.account
        #encode data in json so that it gets passed as a string
        data=json.dumps(data)
        #put Venue, stock and 'orders' into the url
        url=base_url+'/venues/'+self.venues+'/stocks/'+self.stock+'/orders'
        r=requests.post(url, data=data, headers=header)
        return(r.json())
        # print(r,r.json()) #currently just in for debugging/confirmation purposes

    # def cancelOrder(self, ): implement get functionality

    # def get(self,url):
    #     r=requests.get(url)
    #  Consider making a basic function that all of the below "gets" call into
    # below are all the various "get" methods

    def orderBook(self):
        url = base_url + '/venues/' + self.venues + '/stocks/' + self.stock
        r = requests.get(url)
        # print(r, r.json())
        return r.json()

    def getStockList(self):
        # put venues and 'stocks' into url
        url = base_url + '/venues/' + self.venues + '/stocks'
        r = requests.get(url)
        # print(r, r.json())
        return r.json()


    def heartBeat(self):
        url = base_url + '/venues/' + self.venues + '/heartbeat'
        r = requests.get(url)
        # print(r, r.json())
        return r.json()

    def quoteStock(self):
        url=base_url + '/venues/' + self.venues + '/stocks/' + self.stock + '/quote'
        r = requests.get(url)
        # print(r, r.json())
        return r.json()

    def orderStatus(self,orderID):
        url=base_url + '/venues/' + self.venues + '/stocks/' + self.stock + '/orders/'+str(orderID)
        r = requests.get(url, headers=header)
        # print(r, r.json())
        return r.json()

    def getMyOrders(self):
        url=base_url+'/venues/' + self.venues + '/accounts/' + self.account + '/orders'
        r = requests.get(url, headers=header)
        # print(r, r.json())
        return r.json()

    def getOrdersForStock(self,stock):
        url = base_url + '/venues/' + self.venues + '/accounts/' + self.account + '/stocks/'+ stock + '/orders'
        r = requests.get(url)
        # print(r, r.json())
        return r.json()




#Test cases for above APIs
# x=starMarket(venues,stock,account)
# x.orderStock(50,50)
# # x.getStocks()
# x.getMyOrders()
# x.getOrdersForStock(stock)
# x.getStockList()
# x.heartBeat()
# x.orderBook()
# stockQuote=x.quoteStock()

#let's start implementing some business logic

import time

def runTrain(amount):
    #Function to beat the breaking apart a share game
    x=starMarket(venues, stock, account)
    qty=50
    quoteTotal=0
    initialQuote=x.quoteStock()
    # print(initialQuote)
    while quoteTotal<(amount):
        for i in range(10): #try re-initializing starMarket
            #Consider adding a line where you cancel/make sure you don't have previous orders
            quote=x.quoteStock()
            try:
                print(quote['ask'], 'current quote')
                ask=quote['ask']
                askSize=quote['askSize']
                print(initialQuote['ask'], ask, 'inital and current quote')
                if initialQuote['ask'] * 1.02 > ask:
                    myBid = int((ask * 1.01))
                    order=x.orderStock(myBid, int(askSize / 100))
                    print(order,order.json())
                    quoteTotal+=int(askSize/100)

                else:
                    time.sleep(.2)
            except KeyError:
                print('error, couldnt find any asks')
                time.sleep(1)
            # bid=quote['bid']
            time.sleep(.1)
        # x=starMarket(venues, stock, account)




def stealTrain(profPercent,buyMargin,sellMargin,defaultAsk,defaultBid,currentStocks=0): #TODO Really need a better way to get defaults
    #Used for market making "Sell_side" level
    #initiailize variables we'll use later
    x = starMarket(venues, stock, account)
    placedBuys={}
    placedSells={}
    cash=0


    while True: #TODO need to handle connection exceptions
        #First compute how many outstanding buys and sells we have
        outstandingBuys=0
        for i in placedBuys.keys():
            outstandingBuys+=i
        outstandingSells=0
        for i in placedSells.keys():
            outstandingSells+=i
        #query to get the asks/bids, also implement some sort of logic to determine if prices are "reasonable", currently trying spread size v price
        quote=x.quoteStock()
        try: #Consider replacing with some sort of "get" for the ask
            ask=quote.get('ask', quote.get('bid',defaultBid)*profPercent*1.01) #Implementing some defaults for if only asks or only bids are available
            bid=quote.get('bid', quote.get('ask',defaultAsk)*(1-profPercent)*.99)
            spread=ask-bid
            spreadPerc=1+spread/bid #basing off of bid as that's how we're deciding what to buy
            #if we have volume to buy AND asks are "reasonable" then buy, add this to placedBuys
            if spreadPerc>profPercent and outstandingBuys+currentStocks<900:
                price=int(ask*sellMargin)
                quantity=int(min(quote['askSize']/10,50))
                buyID=x.orderStock(price,quantity)['id']
                placedBuys[buyID]=[price,quantity] #Storing in the form "ID: P,Q"
                cash-=price*quantity
            #query current outstanding buys to see if we can remove them and add the volume, possibly also keep a price avg of what you've bought
                #Currently assuming that all orders are either completely filled or not filled at all, will see if it bites me
            for i in placedBuys.copy().keys():
                status=x.orderStatus(i)
                if status['open'] == False:
                    print('bought order '+str(i)+' for a price of ' + str(placedBuys[i][0]) + ' and a volume of ' + str(placedBuys[i][1]))
                    volume=placedBuys[i][1]
                    currentStocks+=volume
                    placedBuys.pop(i)
        except KeyError:
            time.sleep(.2)
        #if we have volume to sell AND Bids are "reasonable" then sell, let's first try getting quotes
        quote=x.quoteStock()
        try:
            ask=quote.get('ask', quote.get('bid',defaultBid)*profPercent*1.01) #Implementing some defaults for if only asks or only bids are available
            bid=quote.get('bid', quote.get('ask',defaultBid)*(1-profPercent)*.99)
            spread=ask-bid
            spreadPerc=1+spread/bid #TODO Consider modularizing this
            # print(spreadPerc,quote)
            if spreadPerc>profPercent and currentStocks-outstandingSells>-900:
                price=int(bid*buyMargin)
                quantity=int(min(quote['bidSize']/10,50))
                sellID=x.orderStock(price,quantity,direction='sell')['id']
                placedSells[sellID]=[price,quantity]
                cash+=price*quantity
            # query current outstanding sells to see if we can remove then and remove them from volume, also see if we want to adjust how much money we've made
            for i in placedSells.copy().keys():
                status=x.orderStatus(i)
                if status['open'] == False:
                    print('Sold order ' + str(i) + ' for a price of ' + str(placedSells[i][0]) + ' and a volume of ' + str(placedSells[i][1]))
                    volume=placedSells[i][1]
                    currentStocks-=volume
                    placedSells.pop(i)
            # TODO Cancel any of my orders that have gotten too out of price range to keep them from filling up the buy/sell volume
        except KeyError:
            time.sleep(.2)
        print('cash is'+str(cash)+' buys are '+str(outstandingBuys)+' sells are '+str(outstandingSells),' current stocks are '+str(currentStocks))
        print('last quote was'+str(quote))
        time.sleep(.1)

    #Let's construct a loop that's always running

account = 'YAL62736392'
stock = 'YEPS'
venues = 'OXEBEX'
x = starMarket(venues, stock, account)
# stealTrain(1.0001,1.00005,.99995,2700,2500,currentStocks=0)
runTrain(938)
