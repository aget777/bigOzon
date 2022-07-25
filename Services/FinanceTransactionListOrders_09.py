import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getFinanceTransactionListOrders"]
head = stringBuilder.getHeaders()
body = stringBuilder.getOrderUrl()

def getFinanceTransactionListOrders():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    financeTransactionListOrdersModels = []


    dateStart = '2022-07-20T00:00:00.000Z'
    dateEnd = '2022-07-22T00:00:00.000Z'
    page_size = 50
    baseURL = 'https://api-seller.ozon.ru'
    orderUrl = '/v3/finance/transaction/list'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getOrderUrl(dateStart=dateStart, dateEnd=dateEnd, page_size=page_size)

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
        jsonResults = response.json()['result']['operations']
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        financeTransactionListOrdersModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return financeTransactionListOrdersModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    financeTransactionListOrdersModels = []
    for jsonResult in jsonResults:
        financeTransactionListOrdersModel = ResponseModels.FinanceTransactionListOrdersModels(jsonResult)
        financeTransactionListOrdersModels.append(financeTransactionListOrdersModel)

    return financeTransactionListOrdersModels