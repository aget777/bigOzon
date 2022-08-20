import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
# __all__ = ["getProductInfoListStocks"]
head = stringBuilder.getHeaders()
body = stringBuilder.getInfoListStocks()

# def getProductInfoListStocks():
#     # Параметры. Подумать, как задавать
#     # Разобраться с конвертацией, пока это костыль!!!
#     # dateStart = datetime.datetime(2021, 12, 1).isoformat()
#     infoStocksListModels = []
#     offer_id = []
#     items1 = "378-01"
#     items2 = "378-07"
#     offer_id.append(items1)
#     offer_id.append(items2)
#
#     baseURL = 'https://api-seller.ozon.ru'
#     orderUrl = '/v2/product/info/list'
#     head = stringBuilder.getHeaders()
#     body = stringBuilder.getInfoListStocks(offer_id=offer_id)
#
#     i = 0
#     while i < 1:
#         # Подумать над асинхронным запросом
#         url = baseURL + orderUrl
#         # print(url)
#         # print(head)
#         # print(body)
#         response = requests.post(url, headers=head, data=body)
#
#         # Логировать ошибки!
#         # print(response.status_code)
#         if response.status_code != 200:
#             break
#         # print(response.json())
#         jsonResults = response.json()['result']['items']
#         # print(jsonResults)
#         # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
#         if not jsonResults:
#             break
#
#         infoStocksListModels += _mapModels(jsonResults)
#
#         print(len(jsonResults))
#         i += 1
#     return infoStocksListModels

def getProductInfosByOfferIds(offerIds):
    infoStocksListModels = []

    baseURL = 'https://api-seller.ozon.ru'
    orderUrl = '/v2/product/info/list'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getInfoListStocks(offer_id=offerIds)

    i = 0
    while i < 1:
        # Подумать над асинхронным запросом
        url = baseURL + orderUrl
        # print(url)
        # print(head)
        # print(body)
        response = requests.post(url, headers=head, data=body)

        # Логировать ошибки!
        # print(response.status_code)
        if response.status_code != 200:
            break
        # print(response.json())
        jsonResults = response.json()['result']['items']
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if not jsonResults:
            break

        infoStocksListModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return infoStocksListModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    infoStocksListModels = []
    for jsonResult in jsonResults:
        infoStocksListModel = ResponseModels.InfoStockModelList(jsonResult)
        infoStocksListModels.append(infoStocksListModel)

    # infoStocksV3Model = ResponseModels.TransactionV1Model(jsonResults)
    # infoStocksV3Models.append(infoStocksV3Model)

    return infoStocksListModels