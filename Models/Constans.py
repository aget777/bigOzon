class URLs:
    def __init__(self) -> None:
        self.baseURL = 'https://api-seller.ozon.ru'
        self.orderUrl = '/v3/finance/transaction/list'
        self.analyticsData = '/v1/analytics/data'
        self.infoStocks = '/v3/product/info/stocks'

# Первое, что нужно убрать отсюда
# Или доработать
class Headers:
    def __init__(self) -> None:
        self.ClientId = 'Client-Id'
        self.authorization = 'Api-Key'

        self.ClientIdValue = '89287'
        self.APIKey = '452a5b5b-4134-4c6e-b2e4-a5620eafe224'

class OrderParameters:
    def __init__(self) -> None:
        self.dateStart = 'from'
        self.dateEnd = 'to'
        self.status = 'operation_type'


# Вынести в конфиги, либо как-то еще избавиться от них
class PathsToFiles:
    def __init__(self) -> None:
        self.catalogPath = r'C:\Users\Lenovo\Downloads\01_Текущие\26_Бизнес_Круче'
        self.dealPath = 'dealTest'