'''
This will be a library of all the functions I might want while operating stockFighter

'''
global apikey,base_url,header
apikey = '7791d4b66cea4c0fd94b15150300fc378c085074'
base_url = 'https://api.stockfighter.io/ob/api'
#authenticate
header = {'X-Starfighter-Authorization': apikey}
# import libraries
import http
import urllib
import locale
import urllib.parse
import urllib.request
import json

class starMarket(object):
    def __init__(self,venues,stock,account):
        self.venues=venues
        self.stock=stock
        self.account=account
    def starTrans(self,direction = 'buy', orderType = 'limit'):
        info = {'price': price, 'qty': qty, 'direction': direction, 'orderType': orderType, 'account': account}
        # currently think this next line is formatting into wrong format
        # info=urllib.parse.urlencode(info)
        # somehow encode the info that you'll be sending in the data key parameter as Json
        info = json.JSONEncoder().encode(info)
        # make the request object
        buy = urllib.request.Request(url=str(base_url +
                                             '/venues/' + venues + '/stocks/' + stock + '/orders'),
                                     data=bytes(info, locale.getpreferredencoding()),
                                     headers=header, method='POST')
        response = urllib.request.urlopen(buy)
        # send the request
        print(response.read())


