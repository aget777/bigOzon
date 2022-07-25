import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getProductInfolistAll"]
head = stringBuilder.getHeaders()
body = stringBuilder.getInfoListStocks()

def getProductInfolistAll():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    productInfolistAllModels = []
    offer_id = []
    items1 = "7020"
    items2 = "2506"
    offer_id.append(items1)
    offer_id.append(items2)

    baseURL = 'https://api-seller.ozon.ru'
    orderUrl = '/v2/product/info/list'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getInfoListStocks(offer_id=offer_id)



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

        productInfolistAllModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return productInfolistAllModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    productInfolistAllModels = []
    for jsonResult in jsonResults:
        productInfolistAllModel = ResponseModels.InfoStockModelList(jsonResult)
        productInfolistAllModels.append(productInfolistAllModel)

    # infoStocksV3Model = ResponseModels.TransactionV1Model(jsonResults)
    # infoStocksV3Models.append(infoStocksV3Model)

    return productInfolistAllModels