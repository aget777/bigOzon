import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getPostingFBSListOrdersDelivered"]
head = stringBuilder.getHeaders()
body = stringBuilder.getPostingFBOListOrdersDeliveredURL()

def getPostingFBSListOrdersDelivered():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    postingFBSListOrdersDeliveredModels = []


    dateStart = '2021-12-09T00:00:00.000Z'
    dateEnd = '2022-07-25T00:00:00.000Z'
    limit = 5
    baseURL = 'https://api-seller.ozon.ru'
    orderUrl = '/v3/posting/fbs/list'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getPostingFBOListOrdersDeliveredURL(dateStart=dateStart, dateEnd=dateEnd, limit=limit)

    i = 0
    while i < 1:
        # Подумать над асинхронным запросом
        url = baseURL + orderUrl
        # print(url)
        # print(head)
        # print(body)
        response = requests.post(url, headers=head, data=body)
        # print(response)
        # Логировать ошибки!
        # print(response.status_code)
        if response.status_code != 200:
            break
        # print(response.json())
        jsonResults = response.json()['result']['postings']
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        postingFBSListOrdersDeliveredModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return postingFBSListOrdersDeliveredModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    postingFBSListOrdersDeliveredModels = []
    for jsonResult in jsonResults:

        postingFBSListOrdersDeliveredModel = ResponseModels.PostingFBSListOrdersDeliveredModels(jsonResult)
        postingFBSListOrdersDeliveredModels.append(postingFBSListOrdersDeliveredModel)

    return postingFBSListOrdersDeliveredModels