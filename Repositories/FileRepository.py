import os

# Добавить нормальные проверки и нормальное отслеживание состояния файлов в каталоге
# Возможно, свои эксепшены. Логировать.



# Новые запросы

def setInfoStocksInFile(infoStocksV3Models) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\infoStocksV3Models', 'w', encoding='utf-8')

    for infoStocksV3Model in infoStocksV3Models:
        file.writelines('productId: ' + str(infoStocksV3Model.productId) + '\n')
        file.writelines('offerId: ' + str(infoStocksV3Model.offerId) + '\n')
        file.writelines('stockTypeFirst: ' + str(infoStocksV3Model.stockTypeFirst) + '\n')
        file.writelines('presentStockFirst: ' + str(infoStocksV3Model.presentStockFirst) + '\n')
        file.writelines('reservedStockFirst: ' + str(infoStocksV3Model.reservedStockFirst) + '\n')
        file.writelines('stockTypeSecond: ' + str(infoStocksV3Model.stockTypeSecond) + '\n')
        file.writelines('presentStockSecond: ' + str(infoStocksV3Model.presentStockSecond) + '\n')
        file.writelines('reservedStockSecond: ' + str(infoStocksV3Model.reservedStockSecond) + '\n')
        file.writelines('\n')

    file.close()


def setInfoListStocksInFile(infoStocksListModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\infoStocksListModel', 'w', encoding='utf-8')

    for infoStocksListModel in infoStocksListModels:
        file.writelines('id: ' + str(infoStocksListModel.id) + '\n')
        file.writelines('name: ' + str(infoStocksListModel.name) + '\n')
        file.writelines('offerId: ' + str(infoStocksListModel.offerId) + '\n')
        file.writelines('barcode: ' + str(infoStocksListModel.barcode) + '\n')
        file.writelines('buyboxPrice: ' + str(infoStocksListModel.buyboxPrice) + '\n')
        file.writelines('categoryId: ' + str(infoStocksListModel.categoryId) + '\n')
        file.writelines('createdAt: ' + str(infoStocksListModel.createdAt) + '\n')
        file.writelines('marketingPrice: ' + str(infoStocksListModel.marketingPrice) + '\n')
        file.writelines('minOzonPrice: ' + str(infoStocksListModel.minOzonPrice) + '\n')
        file.writelines('oldPrice: ' + str(infoStocksListModel.oldPrice) + '\n')
        file.writelines('premiumPrice: ' + str(infoStocksListModel.premiumPrice) + '\n')
        file.writelines('price: ' + str(infoStocksListModel.price) + '\n')
        file.writelines('recommendedPrice: ' + str(infoStocksListModel.recommendedPrice) + '\n')
        file.writelines('fboSku: ' + str(infoStocksListModel.fboSku) + '\n')
        file.writelines('fbsSku: ' + str(infoStocksListModel.fbsSku) + '\n')
        file.writelines('state: ' + str(infoStocksListModel.state) + '\n')
        file.writelines('stocksComing: ' + str(infoStocksListModel.stocksComing) + '\n')
        file.writelines('stocksPresent: ' + str(infoStocksListModel.stocksPresent) + '\n')
        file.writelines('stocksReserved: ' + str(infoStocksListModel.stocksReserved) + '\n')
        file.writelines('vat: ' + str(infoStocksListModel.vat) + '\n')
        file.writelines('visible: ' + str(infoStocksListModel.visible) + '\n')
        file.writelines('visibilityDetailsHasPrice: ' + str(infoStocksListModel.visibilityDetailsHasPrice) + '\n')
        file.writelines('visibilityDetailsHasStock: ' + str(infoStocksListModel.visibilityDetailsHasStock) + '\n')
        file.writelines('visibilityDetailsActiveProduct: ' + str(infoStocksListModel.visibilityDetailsActiveProduct) + '\n')
        file.writelines('visibilityDetailsReasons: ' + str(infoStocksListModel.visibilityDetailsReasons) + '\n')
        file.writelines('priceIndex: ' + str(infoStocksListModel.priceIndex) + '\n')
        file.writelines('statusState: ' + str(infoStocksListModel.statusState) + '\n')
        file.writelines('statusStateFailed: ' + str(infoStocksListModel.statusStateFailed) + '\n')
        file.writelines('statusModerateStatus: ' + str(infoStocksListModel.statusModerateStatus) + '\n')
        file.writelines('statusValidationState: ' + str(infoStocksListModel.statusValidationState) + '\n')
        file.writelines('statusStateName: ' + str(infoStocksListModel.statusStateName) + '\n')
        file.writelines('statusStateDescription: ' + str(infoStocksListModel.statusStateDescription) + '\n')
        file.writelines('statusIsFailed: ' + str(infoStocksListModel.statusIsFailed) + '\n')
        file.writelines('statusIsCreated: ' + str(infoStocksListModel.statusIsCreated) + '\n')
        file.writelines('statusStateTooltip: ' + str(infoStocksListModel.statusStateTooltip) + '\n')
        file.writelines('statusStateUpdatedAt: ' + str(infoStocksListModel.statusStateUpdatedAt) + '\n')
        file.writelines('statusDeclineReasons: ' + str(infoStocksListModel.statusDeclineReasons) + '\n')
        file.writelines('statusItemErrors: ' + str(infoStocksListModel.statusItemErrors) + '\n')
        file.writelines('images: ' + str(infoStocksListModel.images) + '\n')
        file.writelines('colorImage: ' + str(infoStocksListModel.colorImage) + '\n')
        file.writelines('images360: ' + str(infoStocksListModel.images360) + '\n')
        file.writelines('primaryImage: ' + str(infoStocksListModel.primaryImage) + '\n')
        file.writelines('errors: ' + str(infoStocksListModel.errors) + '\n')
        file.writelines('\n')

    file.close()



# Пока костыль, потом посмотреть доработать
def createCatalog(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)
    else:
        print("Успешно создана директория %s " % path)



def setProductInfoPricesInFile(productInfoPricesModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\productInfoPricesModels', 'w', encoding='utf-8')

    for productInfoPricesModel in productInfoPricesModels:
        file.writelines('productId: ' + str(productInfoPricesModel.productId) + '\n')
        file.writelines('offerId: ' + str(productInfoPricesModel.offerId) + '\n')
        file.writelines('pricePrice: ' + str(productInfoPricesModel.pricePrice) + '\n')
        file.writelines('priceOldPrice: ' + str(productInfoPricesModel.priceOldPrice) + '\n')
        file.writelines('pricePremiumPrice: ' + str(productInfoPricesModel.pricePremiumPrice) + '\n')
        file.writelines('priceRecommendedPrice: ' + str(productInfoPricesModel.priceRecommendedPrice) + '\n')
        file.writelines('priceRetailPrice: ' + str(productInfoPricesModel.priceRetailPrice) + '\n')
        file.writelines('priceVat: ' + str(productInfoPricesModel.priceVat) + '\n')
        file.writelines('priceMinPrice: ' + str(productInfoPricesModel.priceMinPrice) + '\n')
        file.writelines('priceMarketingPrice: ' + str(productInfoPricesModel.priceMarketingPrice) + '\n')
        file.writelines('priceMarketingSellerPrice: ' + str(productInfoPricesModel.priceMarketingSellerPrice) + '\n')
        file.writelines('priceIndex: ' + str(productInfoPricesModel.priceIndex) + '\n')
        file.writelines('volumeWeight: ' + str(productInfoPricesModel.volumeWeight) + '\n')


        file.writelines('\n')

    file.close()


def setProductInfoPricesCommissionsInFile(productInfoPricesCommissionsModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\productInfoPricesCommissionsModels', 'w', encoding='utf-8')

    for productInfoPricesCommissionsModel in productInfoPricesCommissionsModels:
        file.writelines('productId: ' + str(productInfoPricesCommissionsModel.productId) + '\n')
        file.writelines('offerId: ' + str(productInfoPricesCommissionsModel.offerId) + '\n')
        file.writelines('pricePrice: ' + str(productInfoPricesCommissionsModel.pricePrice) + '\n')

        file.writelines('commissionsSalesPercent: ' + str(productInfoPricesCommissionsModel.commissionsSalesPercent) + '\n')
        file.writelines('commissionsFboFulfillmentAmount: ' + str(productInfoPricesCommissionsModel.commissionsFboFulfillmentAmount) + '\n')
        file.writelines('commissionsFboDirectFlowTransMinAmount: ' + str(productInfoPricesCommissionsModel.commissionsFboDirectFlowTransMinAmount) + '\n')
        file.writelines('commissionsFboDirectFlowTransMaxAmount: ' + str(productInfoPricesCommissionsModel.commissionsFboDirectFlowTransMaxAmount) + '\n')
        file.writelines('commissionsFboDelivToCustomerAmount: ' + str(productInfoPricesCommissionsModel.commissionsFboDelivToCustomerAmount) + '\n')
        file.writelines('commissionsFboReturnFlowAmount: ' + str(productInfoPricesCommissionsModel.commissionsFboReturnFlowAmount) + '\n')
        file.writelines('commissionsFbsFirstMileMinAmount: ' + str(productInfoPricesCommissionsModel.commissionsFbsFirstMileMinAmount) + '\n')
        file.writelines('commissionsFbsFirstMileMaxAmount: ' + str(productInfoPricesCommissionsModel.commissionsFbsFirstMileMaxAmount) + '\n')
        file.writelines('commissionsFbsDirectFlowTransMinAmount: ' + str(productInfoPricesCommissionsModel.commissionsFbsDirectFlowTransMinAmount) + '\n')
        file.writelines('commissionsFbsDirectFlowTransMaxAmount: ' + str(productInfoPricesCommissionsModel.commissionsFbsDirectFlowTransMaxAmount) + '\n')
        file.writelines('commissionsFbsDelivToCustomerAmount: ' + str(productInfoPricesCommissionsModel.commissionsFbsDelivToCustomerAmount) + '\n')
        file.writelines('commissionsFbsReturnFlowAmount: ' + str(productInfoPricesCommissionsModel.commissionsFbsReturnFlowAmount) + '\n')
        file.writelines('commissionsFbsReturnFlowTransMinAmount: ' + str(productInfoPricesCommissionsModel.commissionsFbsReturnFlowTransMinAmount) + '\n')
        file.writelines('commissionsFbsReturnFlowTransMaxAmount: ' + str(productInfoPricesCommissionsModel.commissionsFbsReturnFlowTransMaxAmount) + '\n')


        file.writelines('\n')

    file.close()

def setProductlistInFile(productlistModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\productlistModels', 'w', encoding='utf-8')

    for productlistModel in productlistModels:
        file.writelines('productId: ' + str(productlistModel.productId) + '\n')
        file.writelines('offerId: ' + str(productlistModel.offerId) + '\n')

        file.writelines('\n')

    file.close()

def setProductInfolistAllInFile(infoStocksListModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\productInfolistAllModel', 'w', encoding='utf-8')

    for infoStocksListModel in infoStocksListModels:
        file.writelines('id: ' + str(infoStocksListModel.id) + '\n')
        file.writelines('name: ' + str(infoStocksListModel.name) + '\n')
        file.writelines('offerId: ' + str(infoStocksListModel.offerId) + '\n')
        file.writelines('barcode: ' + str(infoStocksListModel.barcode) + '\n')
        file.writelines('buyboxPrice: ' + str(infoStocksListModel.buyboxPrice) + '\n')
        file.writelines('categoryId: ' + str(infoStocksListModel.categoryId) + '\n')
        file.writelines('createdAt: ' + str(infoStocksListModel.createdAt) + '\n')
        file.writelines('marketingPrice: ' + str(infoStocksListModel.marketingPrice) + '\n')
        file.writelines('minOzonPrice: ' + str(infoStocksListModel.minOzonPrice) + '\n')
        file.writelines('oldPrice: ' + str(infoStocksListModel.oldPrice) + '\n')
        file.writelines('premiumPrice: ' + str(infoStocksListModel.premiumPrice) + '\n')
        file.writelines('price: ' + str(infoStocksListModel.price) + '\n')
        file.writelines('recommendedPrice: ' + str(infoStocksListModel.recommendedPrice) + '\n')
        file.writelines('fboSku: ' + str(infoStocksListModel.fboSku) + '\n')
        file.writelines('fbsSku: ' + str(infoStocksListModel.fbsSku) + '\n')
        file.writelines('state: ' + str(infoStocksListModel.state) + '\n')
        file.writelines('stocksComing: ' + str(infoStocksListModel.stocksComing) + '\n')
        file.writelines('stocksPresent: ' + str(infoStocksListModel.stocksPresent) + '\n')
        file.writelines('stocksReserved: ' + str(infoStocksListModel.stocksReserved) + '\n')
        file.writelines('vat: ' + str(infoStocksListModel.vat) + '\n')
        file.writelines('visible: ' + str(infoStocksListModel.visible) + '\n')
        file.writelines('visibilityDetailsHasPrice: ' + str(infoStocksListModel.visibilityDetailsHasPrice) + '\n')
        file.writelines('visibilityDetailsHasStock: ' + str(infoStocksListModel.visibilityDetailsHasStock) + '\n')
        file.writelines('visibilityDetailsActiveProduct: ' + str(infoStocksListModel.visibilityDetailsActiveProduct) + '\n')
        file.writelines('visibilityDetailsReasons: ' + str(infoStocksListModel.visibilityDetailsReasons) + '\n')
        file.writelines('priceIndex: ' + str(infoStocksListModel.priceIndex) + '\n')
        file.writelines('statusState: ' + str(infoStocksListModel.statusState) + '\n')
        file.writelines('statusStateFailed: ' + str(infoStocksListModel.statusStateFailed) + '\n')
        file.writelines('statusModerateStatus: ' + str(infoStocksListModel.statusModerateStatus) + '\n')
        file.writelines('statusValidationState: ' + str(infoStocksListModel.statusValidationState) + '\n')
        file.writelines('statusStateName: ' + str(infoStocksListModel.statusStateName) + '\n')
        file.writelines('statusStateDescription: ' + str(infoStocksListModel.statusStateDescription) + '\n')
        file.writelines('statusIsFailed: ' + str(infoStocksListModel.statusIsFailed) + '\n')
        file.writelines('statusIsCreated: ' + str(infoStocksListModel.statusIsCreated) + '\n')
        file.writelines('statusStateTooltip: ' + str(infoStocksListModel.statusStateTooltip) + '\n')
        file.writelines('statusStateUpdatedAt: ' + str(infoStocksListModel.statusStateUpdatedAt) + '\n')
        file.writelines('statusDeclineReasons: ' + str(infoStocksListModel.statusDeclineReasons) + '\n')
        file.writelines('statusItemErrors: ' + str(infoStocksListModel.statusItemErrors) + '\n')
        file.writelines('images: ' + str(infoStocksListModel.images) + '\n')
        file.writelines('colorImage: ' + str(infoStocksListModel.colorImage) + '\n')
        file.writelines('images360: ' + str(infoStocksListModel.images360) + '\n')
        file.writelines('primaryImage: ' + str(infoStocksListModel.primaryImage) + '\n')
        file.writelines('errors: ' + str(infoStocksListModel.errors) + '\n')
        file.writelines('\n')

    file.close()

def setPostingFBOListOrdersDeliveredInFile(postingFBOListOrdersDeliveredModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\postingFBOListOrdersDeliveredModel', 'w', encoding='utf-8')

    for postingFBOListOrdersDeliveredModel in postingFBOListOrdersDeliveredModels:
        file.writelines('orderId : ' + str(postingFBOListOrdersDeliveredModel.orderId ) + '\n')
        file.writelines('orderNumber: ' + str(postingFBOListOrdersDeliveredModel.orderNumber) + '\n')
        file.writelines('postingNumber: ' + str(postingFBOListOrdersDeliveredModel.postingNumber) + '\n')
        file.writelines('status: ' + str(postingFBOListOrdersDeliveredModel.status) + '\n')
        file.writelines('cancelReasonId: ' + str(postingFBOListOrdersDeliveredModel.cancelReasonId) + '\n')
        file.writelines('createdAt: ' + str(postingFBOListOrdersDeliveredModel.createdAt) + '\n')
        file.writelines('inProcessAt: ' + str(postingFBOListOrdersDeliveredModel.inProcessAt) + '\n')
        file.writelines('productsSku: ' + str(postingFBOListOrdersDeliveredModel.productsSku) + '\n')
        file.writelines('productsName: ' + str(postingFBOListOrdersDeliveredModel.productsName) + '\n')
        file.writelines('productsQuantity: ' + str(postingFBOListOrdersDeliveredModel.productsQuantity) + '\n')
        file.writelines('productsOfferId: ' + str(postingFBOListOrdersDeliveredModel.productsOfferId) + '\n')
        file.writelines('productsPrice: ' + str(postingFBOListOrdersDeliveredModel.productsPrice) + '\n')
        file.writelines('analyticsDataRegion: ' + str(postingFBOListOrdersDeliveredModel.analyticsDataRegion) + '\n')
        file.writelines('analyticsDataCity: ' + str(postingFBOListOrdersDeliveredModel.analyticsDataCity) + '\n')
        file.writelines('analyticsDataDeliveryType: ' + str(postingFBOListOrdersDeliveredModel.analyticsDataDeliveryType) + '\n')
        file.writelines('analyticsDataIsPremium: ' + str(postingFBOListOrdersDeliveredModel.analyticsDataIsPremium) + '\n')
        file.writelines('analyticsDataPaymentType: ' + str(postingFBOListOrdersDeliveredModel.analyticsDataPaymentType) + '\n')
        file.writelines('analyticsDataWarehouseId: ' + str(postingFBOListOrdersDeliveredModel.analyticsDataWarehouseId) + '\n')
        file.writelines('analyticsDataWarehouseName: ' + str(postingFBOListOrdersDeliveredModel.analyticsDataWarehouseName) + '\n')
        file.writelines('analyticsDataIsLegal: ' + str(postingFBOListOrdersDeliveredModel.analyticsDataIsLegal) + '\n')
        file.writelines('financialDataCommissionAmount: ' + str(postingFBOListOrdersDeliveredModel.financialDataCommissionAmount) + '\n')
        file.writelines('financialDataCommissionPercent: ' + str(postingFBOListOrdersDeliveredModel.financialDataCommissionPercent) + '\n')
        file.writelines('financialDataPayout: ' + str(postingFBOListOrdersDeliveredModel.financialDataPayout) + '\n')
        file.writelines('financialDataProductId: ' + str(postingFBOListOrdersDeliveredModel.financialDataProductId) + '\n')
        file.writelines('financialDataOldPrice: ' + str(postingFBOListOrdersDeliveredModel.financialDataOldPrice) + '\n')
        file.writelines('financialDataPrice: ' + str(postingFBOListOrdersDeliveredModel.financialDataPrice) + '\n')
        file.writelines('financialDataTotalDiscountValue: ' + str(postingFBOListOrdersDeliveredModel.financialDataTotalDiscountValue) + '\n')
        file.writelines('financialDataTotalDiscountPercent: ' + str(postingFBOListOrdersDeliveredModel.financialDataTotalDiscountPercent) + '\n')
        file.writelines('financialDataActions: ' + str(postingFBOListOrdersDeliveredModel.financialDataActions) + '\n')
        file.writelines('financialDataPicking: ' + str(postingFBOListOrdersDeliveredModel.financialDataPicking) + '\n')
        file.writelines('financialDataQuantity: ' + str(postingFBOListOrdersDeliveredModel.financialDataQuantity) + '\n')
        file.writelines('financialDataClientPrice: ' + str(postingFBOListOrdersDeliveredModel.financialDataClientPrice) + '\n')
        file.writelines('financialDataFulfillment: ' + str(postingFBOListOrdersDeliveredModel.financialDataFulfillment) + '\n')
        file.writelines('financialDataPickup: ' + str(postingFBOListOrdersDeliveredModel.financialDataPickup) + '\n')
        file.writelines('financialDataPvz: ' + str(postingFBOListOrdersDeliveredModel.financialDataPvz) + '\n')
        file.writelines('financialDataSc: ' + str(postingFBOListOrdersDeliveredModel.financialDataSc) + '\n')
        file.writelines('financialDataFf: ' + str(postingFBOListOrdersDeliveredModel.financialDataFf) + '\n')
        file.writelines('financialDataDirectTrans: ' + str(postingFBOListOrdersDeliveredModel.financialDataDirectTrans) + '\n')
        file.writelines('financialDataReturnTrans: ' + str(postingFBOListOrdersDeliveredModel.financialDataReturnTrans) + '\n')
        file.writelines('financialDataDelivToCustomer: ' + str(postingFBOListOrdersDeliveredModel.financialDataDelivToCustomer) + '\n')
        file.writelines('financialDataReturnNotDelivToCustomer: ' + str(postingFBOListOrdersDeliveredModel.financialDataReturnNotDelivToCustomer) + '\n')
        file.writelines('financialDataReurnPartGoodToCustomer: ' + str(postingFBOListOrdersDeliveredModel.financialDataReurnPartGoodToCustomer) + '\n')
        file.writelines('financialDataReturnAfterDeliv: ' + str(postingFBOListOrdersDeliveredModel.financialDataReturnAfterDeliv) + '\n')
        file.writelines('postingFulfillment : ' + str(postingFBOListOrdersDeliveredModel.postingFulfillment ) + '\n')
        file.writelines('postingPickup: ' + str(postingFBOListOrdersDeliveredModel.postingPickup) + '\n')
        file.writelines('postingPvz: ' + str(postingFBOListOrdersDeliveredModel.postingPvz) + '\n')
        file.writelines('postingSc: ' + str(postingFBOListOrdersDeliveredModel.postingSc) + '\n')
        file.writelines('postingFf: ' + str(postingFBOListOrdersDeliveredModel.postingFf) + '\n')
        file.writelines('postingTrans: ' + str(postingFBOListOrdersDeliveredModel.postingTrans) + '\n')
        file.writelines('postingReturnTrans: ' + str(postingFBOListOrdersDeliveredModel.postingReturnTrans) + '\n')
        file.writelines('postingDelivToCustomer: ' + str(postingFBOListOrdersDeliveredModel.postingDelivToCustomer) + '\n')
        file.writelines('postingReturnNotDelivToCustomer: ' + str(postingFBOListOrdersDeliveredModel.postingReturnNotDelivToCustomer) + '\n')
        file.writelines('postingReurnPartGoodToCustomer: ' + str(postingFBOListOrdersDeliveredModel.postingReurnPartGoodToCustomer) + '\n')
        file.writelines('postingReturnAfterDeliv: ' + str(postingFBOListOrdersDeliveredModel.postingReturnAfterDeliv) + '\n')
        file.writelines('additionalData: ' + str(postingFBOListOrdersDeliveredModel.additionalData) + '\n')


        file.writelines('\n')

    file.close()


# Пока костыль, потом посмотреть доработать
def createCatalog(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)
    else:
        print("Успешно создана директория %s " % path)