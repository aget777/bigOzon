import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getFinanceTotals"]
head = stringBuilder.getHeaders()
body = stringBuilder.getTotalUrl()

def getFinanceTotals():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    financeTotalsModels = []


    dateStart = '2022-07-20T00:00:00.000Z'
    dateEnd = '2022-07-25T00:00:00.000Z'
    baseURL = 'https://api-seller.ozon.ru'
    orderUrl = '/v3/finance/transaction/totals'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getTotalUrl(dateStart=dateStart, dateEnd=dateEnd)

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
        jsonResults = response.json()['result']
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        financeTotalsModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return financeTotalsModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    financeTotalsModels = []

    financeTotalsModel = ResponseModels.FinanceTotalsModels(jsonResults)
    financeTotalsModels.append(financeTotalsModel)

    return financeTotalsModels