'''
This will be a library of all the functions I might want while operating stockFighter

'''



def starBuy(price, qty):
    # import libraries
    import http
    import urllib
    import locale
    import urllib.parse
    import urllib.request
    import json

    # initialize the account
    venues = 'EFVEX'
    stock = 'RTM'
    account = 'KLB64148141'
    apikey = '7791d4b66cea4c0fd94b15150300fc378c085074'
    base_url = 'https://api.stockfighter.io/ob/api'
    header = {'X-Starfighter-Authorization': apikey}
    # setup the trade
    direction = 'buy'
    orderType = 'limit'
    # authenticate
    # send the trade
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



# #
# # account=FEB67661172
# # ticker=MMC
# base_url = "https://api.stockfighter.io/ob/api"

starBuy(10,10)
