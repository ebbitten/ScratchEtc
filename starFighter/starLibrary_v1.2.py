'''
This will be a library of all the functions I might want while operating stockFighter

v1.1 Move the market object to a class
v1.2 start using the requests framework
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
        print(r,r.json()) #currently just in for debugging/confirmation purposes

    # def cancelOrder(self, ): implement get functionality

    # def get(self,url):
    #     r=requests.get(url)
    #  Consider making a basic function that all of the below "gets" call into

    def orderBook(self):
        url = base_url + '/venues/' + self.venues + '/stocks/' + self.stock
        r = requests.get(url)
        print(r, r.json())

    def getStockList(self):
        # put venues and 'stocks' into url
        url = base_url + '/venues/' + self.venues + '/stocks'
        r = requests.get(url)
        print(r, r.json())

    def heartBeat(self):
        url = base_url + '/venues/' + self.venues + '/heartbeat'
        r = requests.get(url)
        print(r, r.json())

    def quoteStock(self):
        url=base_url + '/venues/' + self.venues + '/stocks/' + self.stock + '/quote'
        r = requests.get(url)
        print(r, r.json)

    def orderStatus(self,orderID):
        url=base_url + '/venues/' + self.venues + '/stocks/' + self.stock + '/orders/'+orderID
        r = requests.get(url)
        print(r, r.json)

    def getMyOrders(self):
        url=base_url+'/venues/' + self.venues + '/accounts/' + self.account + '/orders'
        r = requests.get(url)
        print(r, r.json)

    def getOrdersForStock(self,stock):
        url = base_url + '/venues/' + self.venues + '/accounts/' + self.account + '/stocks/'+ stock + '/orders'
        r = requests.get(url)
        print(r, r.json)


account='LTB55786117'
stock='RSH'
venues='RIVEX'

x=starMarket(venues,stock,account)
x.orderStock(50,50)
# x.getStocks()
x.getMyOrders()
x.getOrdersForStock(stock)
x.getStockList()
x.heartBeat()
x.orderBook()
x.quoteStock()


