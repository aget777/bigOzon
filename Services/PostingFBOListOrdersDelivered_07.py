import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getPostingFBOListOrdersDelivered"]
head = stringBuilder.getHeaders()
body = stringBuilder.getPostingFBOListOrdersDeliveredURL()

def getPostingFBOListOrdersDelivered():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    postingFBOListOrdersDeliveredModels = []


    dateStart = '2022-07-25T00:00:00.000Z'
    dateEnd = '2022-07-30T00:00:00.000Z'
    status = ''
    limit = 1000
    baseURL = 'https://api-seller.ozon.ru'
    orderUrl = '/v2/posting/fbo/list'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getPostingFBOListOrdersDeliveredURL(dateStart=dateStart, dateEnd=dateEnd, status=status, limit=limit)

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
        jsonResults = response.json()['result']
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        postingFBOListOrdersDeliveredModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return postingFBOListOrdersDeliveredModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    postingFBOListOrdersDeliveredModels = []
    for jsonResult in jsonResults:
        postingFBOListOrdersDeliveredModel = ResponseModels.PostingFBOListOrdersDeliveredModels(jsonResult)
        postingFBOListOrdersDeliveredModels.append(postingFBOListOrdersDeliveredModel)

    return postingFBOListOrdersDeliveredModels