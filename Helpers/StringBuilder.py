from Models import Constans
import json

# Разобраться почему не работает сокрытие
# __all__ = ["getHeaders", "getOrderUrl"]

urls = Constans.URLs()
headers = Constans.Headers()
parameters = Constans.OrderParameters()

# добавить нормальную сборку заголовков, почитать про это
def getHeaders() -> dict:
    head = {headers.ClientId: headers.ClientIdValue, headers.authorization: headers.APIKey}

    return head


# новый код


def getInfoListStocks(offer_id=[], product_id=[], sku=[]):
    body = {'offer_id': offer_id, 'product_id': product_id, 'sku': sku}
    body = json.dumps(body)
    return body


def getProductInfoPricesURL(offer_id=[], product_id=[], last_id='', limit=50):
    body = {'filter':{'offer_id': offer_id, 'product_id': product_id, 'visibility': 'ALL'}, 'last_id': last_id, 'limit': limit}
    body = json.dumps(body)
    return body

def getPostingFBOListOrdersDeliveredURL(dir='ASC', dateStart='', status='delivered', dateEnd='', limit=1000, offset=0):
    body = {'dir': dir, 'filter': {'since': dateStart, 'status': status, 'to': dateEnd}, 'limit': limit, 'offset': offset,'translit': True, 'with': {'analytics_data': True, 'financial_data': True }}
    body = json.dumps(body)
    return body


def getOrderUrl(dateStart='', dateEnd='', transaction_type='orders', page_size=50):
    body = {'filter':{'date':{'from': dateStart, 'to': dateEnd}, 'operation_type': [], 'transaction_type':  transaction_type}, 'page': 1, 'page_size': page_size}
    body = json.dumps(body)
    return body


def getTotalUrl(dateStart='', dateEnd='', transaction_type='orders'):
    body = {'date': {'from': dateStart, 'to': dateEnd}, 'posting_number': '', 'transaction_type': transaction_type}
    body = json.dumps(body)
    return body


