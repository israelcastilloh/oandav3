# oandav3

## Set-Up
```python
$ git clone https://github.com/israelcastilloh/oandav3
```

## API

```python
from oandav3 import * 

upper_account = accountID
access_token = token
connection = API(environment, access_token, account_id)
        ''' @ Params: 
              environment = 'practice' / 'live' / 'sandbox'
              access_token = 'asda567b...'
              account_id = 'XXX-XXX-XXXXXXXX-XXX' 
        '''
        
    
endpoint = connection.endpoint(**params)
```

## Endpoints

```python

  '''''''''
  Accounts
  '''''''''
  get_instruments(self)

  get_accounts(self)

  account_detail(self)

  account_summary(self)
```
```python

  '''''''''
  Instruments
  '''''''''
  instrument_candles(self, instrument)

  order_book(self, instrument)

  position_book(self, instrument)

```
```python

  '''''''''
  Orders
  '''''''''
  orders(self)

  pending_orders(self)

  single_order(self, orderID)
    
```
```python

  '''''''''
  Trade
  '''''''''
  trades(self)

  open_trades(self)

  single_trade(self, tradeID)

```
```python

  '''''''''
  Position
  '''''''''
  positions(self)

  open_positions(self)

  instrument_position(self, instrument)

```
```python

  '''''''''
  Transactions
  '''''''''
  transactions(self)

  single_transaction(self, transaction)

  transaction_range(self, from_t_id, to_t_id)

  transaction_since(self, since_t_id)

```
```python

  '''''''''
  Pricing
  '''''''''
  pricing(self, instrument)


```



```python
'''

Developed by: Israel Castillo. // Financial Engineer // castillo.israelh@gmail.com

'''
