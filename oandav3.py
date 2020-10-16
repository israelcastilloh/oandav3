import requests
import pandas as pd


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

class Endpoints(object):

    '''
    Accounts
    '''

    def get_instruments(self):
        endpoint = '/instruments'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def get_accounts(self):
        endpoint = '/accounts'
        response = requests.get(self.api_url+'/v3'+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def account_detail(self):
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account, auth=self.access_token)
        return pd.read_json(response.text)

    def account_summary(self):
        endpoint = '/summary'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    '''
    Instruments
    '''

    def instrument_candles(self, instrument):
        endpoint = '/candles'
        response = requests.get(self.api_url+'/v3/instruments/'+instrument+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def order_book(self, instrument):
        endpoint = '/orderBook'
        response = requests.get(self.api_url+'/v3/instruments/'+instrument+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def position_book(self, instrument):
        endpoint = '/positionBook'
        response = requests.get(self.api_url+'/v3/instruments/'+instrument+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    '''
    Orders
    '''
    def orders(self):
        endpoint = '/orders'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def pending_orders(self):
        endpoint = '/pendingOrders'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def single_order(self, order):
        endpoint = '/orders/'+order
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)


    '''
    Trade
    '''

    def trades(self):
        endpoint = '/trades'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def open_trades(self):
        endpoint = '/openTrades'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def single_trade(self, trade):
        endpoint = '/trades/'+trade
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    '''
    Position
    '''

    def positions(self):
        endpoint = '/trades'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def open_positions(self):
        endpoint = '/openTrades'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def instrument_position(self, instrument):
        endpoint = '/positions/'+instrument #must containt "_" in between currencies
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    '''
    Transactions
    '''

    def transactions(self):
        endpoint = '/transactions'
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def single_transaction(self, transaction):
        endpoint = '/transactions/'+transaction
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def transaction_range(self, f, t):
        endpoint = '/transactions/idrange?'+'to='+t+'&from='+f
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)

    def transaction_since(self, since):
        endpoint = '/transactions/sinceid?id='+since
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)


    '''
    Pricing
    '''

    def pricing(self, instrument):
        endpoint = '/pricing?instruments='+instrument
        response = requests.get(self.api_url+'/v3/accounts/'+self.upper_account+endpoint, auth=self.access_token)
        return pd.read_json(response.text)


class API(Endpoints, object):
    def __init__(self, environment, access_token, upper_account, **params):
        self.access_token = BearerAuth(access_token)
        self.upper_account = upper_account

        if environment == 'sandbox':
            self.api_url = 'http://api-sandbox.oanda.com'
        elif environment == 'practice':
            self.api_url = 'https://api-fxpractice.oanda.com'
        elif environment == 'live':
            self.api_url = 'https://api-fxtrade.oanda.com'
        else:
            print("Environment '%s' does not exist \n" % environment)




upper_account = ""
access_token = ""

test = API('practice', access_token, upper_account)
test = test.get_instruments()
print(test)
# def get_instruments(environment, token, upper_account):
# response = requests.get('https://api-fxpractice.oanda.com/v3/accounts/101-011-16494438-002/instruments', auth=BearerAuth('4d5aad4aa2939a132fe264df7592d9ab-6a99aceb020a93917af53376dbb1a8d5'))
# general = pd.read_json(response.text)
