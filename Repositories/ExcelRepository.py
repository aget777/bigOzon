import pandas as pd

# Подумать, куда вынести отсюда имена как константы
# В принципе, уже сейчас думать над документацией проекта





def writeInfoStocksDataFramesInExcel(infoStocksV3Models):
    writer = pd.ExcelWriter('./infoStocks.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    infoStocksV3ModelsDataFrame = _getDataFrameByInfoStocks(infoStocksV3Models)
    dataSheets = {'stocksResult': infoStocksV3ModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

def _getDataFrameByInfoStocks(infoStocksV3Models):
    productIdList = []
    offerIdList = []
    stockTypeFirstList = []
    presentStockFirstList = []
    reservedStockFirstList = []
    stockTypeSecondList = []
    presentStockSecondList = []
    reservedStockSecondList = []

    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for infoStocksV3Model in infoStocksV3Models:
        productIdList.append(infoStocksV3Model.productId)
        offerIdList.append(infoStocksV3Model.offerId)
        stockTypeFirstList.append(infoStocksV3Model.stockTypeFirst)
        presentStockFirstList.append(infoStocksV3Model.presentStockFirst)
        reservedStockFirstList.append(infoStocksV3Model.reservedStockFirst)
        stockTypeSecondList.append(infoStocksV3Model.stockTypeSecond)
        presentStockSecondList.append(infoStocksV3Model.presentStockSecond)
        reservedStockSecondList.append(infoStocksV3Model.reservedStockSecond)

    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame(
                 {'productId': productIdList,
                 'offerId': offerIdList,
                 'stockTypeFirst': stockTypeFirstList,
                 'presentStockFirst': presentStockFirstList,
                 'reservedStockFirst': reservedStockFirstList,
                 'stockTypeSecond': stockTypeSecondList,
                 'presentStockSecond': presentStockSecondList,
                 'reservedStockSecond': reservedStockSecondList})


    return dataFrame


# Подумать, куда вынести отсюда имена как константы
# В принципе, уже сейчас думать над документацией проекта
def writeInfoListStocksDataFramesInExcel(infoStocksListModels):
    writer = pd.ExcelWriter('./infoListStocks.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    infoStocksListModelsDataFrame = _getDataFrameByInfoListStocks(infoStocksListModels)
    dataSheets = {'stocksListResult': infoStocksListModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер
def _getDataFrameByInfoListStocks(infoStocksListModels):
    idList = []
    nameList = []
    offerIdList = []
    barcodeList = []
    buyboxPriceList = []
    categoryIdList = []
    createdAtList = []
    marketingPriceList = []
    minOzonPriceList = []
    oldPriceList = []
    premiumPriceList = []

    priceList = []
    recommendedPriceList = []
    fboSkuList = []
    fbsSkuList = []
    stateList = []
    stocksComingList = []
    stocksPresentList = []
    stocksReservedList = []
    vatList = []
    visibleList = []
    visibilityDetailsHasPriceList = []
    visibilityDetailsHasStockList = []
    visibilityDetailsActiveProductList = []
    visibilityDetailsReasonsList = []
    priceIndexList = []
    statusStateList = []
    statusStateFailedList = []
    statusModerateStatusList = []
    statusValidationStateList = []
    statusStateNameList = []
    statusStateDescriptionList = []
    statusIsFailedList = []
    statusIsCreatedList = []
    statusStateTooltipList = []
    statusStateUpdatedAtList = []
    statusDeclineReasonsList = []
    statusItemErrorsList = []
    imagesList = []
    colorImageList = []
    images360List = []
    primaryImageList = []
    errorsList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for infoStocksListModel in infoStocksListModels:
        idList.append(infoStocksListModel.id)
        nameList.append(infoStocksListModel.name)
        offerIdList.append(infoStocksListModel.offerId)
        barcodeList.append(infoStocksListModel.barcode)
        buyboxPriceList.append(infoStocksListModel.buyboxPrice)
        categoryIdList.append(infoStocksListModel.categoryId)
        createdAtList.append(infoStocksListModel.createdAt)
        marketingPriceList.append(infoStocksListModel.marketingPrice)
        minOzonPriceList.append(infoStocksListModel.minOzonPrice)
        oldPriceList.append(infoStocksListModel.oldPrice)
        premiumPriceList.append(infoStocksListModel.premiumPrice)

        priceList.append(infoStocksListModel.price)
        recommendedPriceList.append(infoStocksListModel.recommendedPrice)
        fboSkuList.append(infoStocksListModel.fboSku)
        fbsSkuList.append(infoStocksListModel.fbsSku)
        stateList.append(infoStocksListModel.state)
        stocksComingList.append(infoStocksListModel.stocksComing)
        stocksPresentList.append(infoStocksListModel.stocksPresent)
        stocksReservedList.append(infoStocksListModel.stocksReserved)
        vatList.append(infoStocksListModel.vat)
        visibleList.append(infoStocksListModel.visible)
        visibilityDetailsHasPriceList.append(infoStocksListModel.visibilityDetailsHasPrice)
        visibilityDetailsHasStockList.append(infoStocksListModel.visibilityDetailsHasStock)
        visibilityDetailsActiveProductList.append(infoStocksListModel.visibilityDetailsActiveProduct)
        visibilityDetailsReasonsList.append(infoStocksListModel.visibilityDetailsReasons)
        priceIndexList.append(infoStocksListModel.priceIndex)
        statusStateList.append(infoStocksListModel.statusState)
        statusStateFailedList.append(infoStocksListModel.statusStateFailed)
        statusModerateStatusList.append(infoStocksListModel.statusModerateStatus)
        statusValidationStateList.append(infoStocksListModel.statusValidationState)
        statusStateNameList.append(infoStocksListModel.statusStateName)
        statusStateDescriptionList.append(infoStocksListModel.statusStateDescription)
        statusIsFailedList.append(infoStocksListModel.statusIsFailed)
        statusIsCreatedList.append(infoStocksListModel.statusIsCreated)
        statusStateTooltipList.append(infoStocksListModel.statusStateTooltip)
        statusStateUpdatedAtList.append(infoStocksListModel.statusStateUpdatedAt)
        statusDeclineReasonsList.append(infoStocksListModel.statusDeclineReasons)
        statusItemErrorsList.append(infoStocksListModel.statusItemErrors)
        imagesList.append(infoStocksListModel.images)
        colorImageList.append(infoStocksListModel.colorImage)
        images360List.append(infoStocksListModel.images360)
        primaryImageList.append(infoStocksListModel.primaryImage)
        errorsList.append(infoStocksListModel.errors)


    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'id': idList,
                 'name': nameList,
                 'offerId': offerIdList,
                 'barcode': barcodeList,
                 'buyboxPrice': buyboxPriceList,
                 'categoryId': categoryIdList,
                 'createdAt': createdAtList,
                 'marketingPrice': marketingPriceList,

                 'minOzonPrice': minOzonPriceList,
                 'oldPrice': oldPriceList,
                 'premiumPrice': premiumPriceList,
                 'price': priceList,
                 'recommendedPrice': recommendedPriceList,
                 'fboSku': fboSkuList,
                 'fbsSku': fbsSkuList,
                 'state': stateList,
                 'stocksComing': stocksComingList,
                 'stocksPresent': stocksPresentList,
                 'stocksReserved': stocksReservedList,
                 'vat': vatList,
                 'visible': visibleList,
                 'visibilityDetailsHasPrice': visibilityDetailsHasPriceList,
                 'visibilityDetailsHasStock': visibilityDetailsHasStockList,
                 'visibilityDetailsActiveProduct': visibilityDetailsActiveProductList,
                 'visibilityDetailsReasons': visibilityDetailsReasonsList,
                 'priceIndex': priceIndexList,
                 'statusState': statusStateList,
                 'statusStateFailed': statusStateFailedList,
                 'statusModerateStatus': statusModerateStatusList,
                 'statusValidationState': statusValidationStateList,
                 'statusStateName': statusStateNameList,
                 'statusStateDescription': statusStateDescriptionList,
                 'statusIsFailed': statusIsFailedList,
                 'statusIsCreated': statusIsCreatedList,
                 'statusStateTooltip': statusStateTooltipList,
                 'statusStateUpdatedAt': statusStateUpdatedAtList,
                 'statusDeclineReasons': statusDeclineReasonsList,
                 'statusItemErrors': statusItemErrorsList,
                 'images': imagesList,
                 'colorImage': colorImageList,
                 'images360': images360List,
                 'primaryImage': primaryImageList,
                 'errors': errorsList,
    })


    return dataFrame




def writeProductInfoPricesDataFramesInExcel(productInfoPricesModels):
    writer = pd.ExcelWriter('./productInfoPrices.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    productInfoPricesModelsDataFrame = _getDataFrameByProductInfoPricesModels(productInfoPricesModels)
    dataSheets = {'productInfoPricesResult': productInfoPricesModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер
def _getDataFrameByProductInfoPricesModels(productInfoPricesModels):
    productIdList = []
    offerIdList = []
    pricePriceList = []
    priceOldPriceList = []
    pricePremiumPriceList = []
    priceRecommendedPriceList = []
    priceRetailPriceList = []
    priceVatList = []
    priceMinPriceList = []
    priceMarketingPriceList = []

    priceMarketingSellerPriceList = []
    priceIndexList = []
    volumeWeightList = []



    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for productInfoPricesModel in productInfoPricesModels:
        productIdList.append(productInfoPricesModel.productId)
        offerIdList.append(productInfoPricesModel.offerId)
        pricePriceList.append(productInfoPricesModel.pricePrice)
        priceOldPriceList.append(productInfoPricesModel.priceOldPrice)
        pricePremiumPriceList.append(productInfoPricesModel.pricePremiumPrice)
        priceRecommendedPriceList.append(productInfoPricesModel.priceRecommendedPrice)
        priceRetailPriceList.append(productInfoPricesModel.priceRetailPrice)
        priceVatList.append(productInfoPricesModel.priceVat)
        priceMinPriceList.append(productInfoPricesModel.priceMinPrice)
        priceMarketingPriceList.append(productInfoPricesModel.priceMarketingPrice)
        priceMarketingSellerPriceList.append(productInfoPricesModel.priceMarketingSellerPrice)
        priceIndexList.append(productInfoPricesModel.priceIndex)
        volumeWeightList.append(productInfoPricesModel.volumeWeight)



    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'productId': productIdList,
                 'offerId': offerIdList,
                 'pricePrice': pricePriceList,
                 'priceOldPrice': priceOldPriceList,
                 'pricePremiumPrice': pricePremiumPriceList,
                 'priceRecommendedPrice': priceRecommendedPriceList,
                 'priceRetailPrice': priceRetailPriceList,

                 'priceVat': priceVatList,
                 'priceMinPrice': priceMinPriceList,
                 'priceMarketingPrice': priceMarketingPriceList,
                 'priceMarketingSellerPrice': priceMarketingSellerPriceList,
                 'priceIndex': priceIndexList,
                 'volumeWeight': volumeWeightList,
                 
    })


    return dataFrame


def writeProductInfoPricesCommissionsDataFramesInExcel(productInfoPricesCommissionsModels):
    writer = pd.ExcelWriter('./productInfoPricesCommissions.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    productInfoPricesCommissionsModelsDataFrame = _getDataFrameByProductInfoPricesCommissionsModels(productInfoPricesCommissionsModels)
    dataSheets = {'productInfoPricesCommissions': productInfoPricesCommissionsModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()


# Уйти потом от этого
# Либо, написать нормальный маппер
def _getDataFrameByProductInfoPricesCommissionsModels(productInfoPricesCommissionsModels):
    productIdList = []
    offerIdList = []
    pricePriceList = []

    commissionsSalesPercentList = []
    commissionsFboFulfillmentAmountList = []
    commissionsFboDirectFlowTransMinAmountList = []
    commissionsFboDirectFlowTransMaxAmountList = []
    commissionsFboDelivToCustomerAmountList = []
    commissionsFboReturnFlowAmountList = []
    commissionsFbsFirstMileMinAmountList = []
    commissionsFbsFirstMileMaxAmountList = []
    commissionsFbsDirectFlowTransMinAmountList = []
    commissionsFbsDirectFlowTransMaxAmountList = []
    commissionsFbsDelivToCustomerAmountList = []
    commissionsFbsReturnFlowAmountList = []
    commissionsFbsReturnFlowTransMinAmountList = []
    commissionsFbsReturnFlowTransMaxAmountList = []



    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for productInfoPricesCommissionsModel in productInfoPricesCommissionsModels:
        productIdList.append(productInfoPricesCommissionsModel.productId)
        offerIdList.append(productInfoPricesCommissionsModel.offerId)
        pricePriceList.append(productInfoPricesCommissionsModel.pricePrice)

        commissionsSalesPercentList.append(productInfoPricesCommissionsModel.commissionsSalesPercent)
        commissionsFboFulfillmentAmountList.append(productInfoPricesCommissionsModel.commissionsFboFulfillmentAmount)
        commissionsFboDirectFlowTransMinAmountList.append(productInfoPricesCommissionsModel.commissionsFboDirectFlowTransMinAmount)
        commissionsFboDirectFlowTransMaxAmountList.append(productInfoPricesCommissionsModel.commissionsFboDirectFlowTransMaxAmount)
        commissionsFboDelivToCustomerAmountList.append(productInfoPricesCommissionsModel.commissionsFboDelivToCustomerAmount)
        commissionsFboReturnFlowAmountList.append(productInfoPricesCommissionsModel.commissionsFboReturnFlowAmount)
        commissionsFbsFirstMileMinAmountList.append(productInfoPricesCommissionsModel.commissionsFbsFirstMileMinAmount)
        commissionsFbsFirstMileMaxAmountList.append(productInfoPricesCommissionsModel.commissionsFbsFirstMileMaxAmount)
        commissionsFbsDirectFlowTransMinAmountList.append(productInfoPricesCommissionsModel.commissionsFbsDirectFlowTransMinAmount)
        commissionsFbsDirectFlowTransMaxAmountList.append(productInfoPricesCommissionsModel.commissionsFbsDirectFlowTransMaxAmount)
        commissionsFbsDelivToCustomerAmountList.append(productInfoPricesCommissionsModel.commissionsFbsDelivToCustomerAmount)
        commissionsFbsReturnFlowAmountList.append(productInfoPricesCommissionsModel.commissionsFbsReturnFlowAmount)
        commissionsFbsReturnFlowTransMinAmountList.append(productInfoPricesCommissionsModel.commissionsFbsReturnFlowTransMinAmount)
        commissionsFbsReturnFlowTransMaxAmountList.append(productInfoPricesCommissionsModel.commissionsFbsReturnFlowTransMaxAmount)


    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
        'productId': productIdList,
        'offerId': offerIdList,
        'pricePrice': pricePriceList,

        'commissionsSalesPercent': commissionsSalesPercentList,
        'commissionsFboFulfillmentAmount': commissionsFboFulfillmentAmountList,
        'commissionsFboDirectFlowTransMinAmount': commissionsFboDirectFlowTransMinAmountList,
        'commissionsFboDirectFlowTransMaxAmount': commissionsFboDirectFlowTransMaxAmountList,
        'commissionsFboDelivToCustomerAmount': commissionsFboDelivToCustomerAmountList,
        'commissionsFboReturnFlowAmount': commissionsFboReturnFlowAmountList,
        'commissionsFbsFirstMileMinAmount': commissionsFbsFirstMileMinAmountList,
        'commissionsFbsFirstMileMaxAmount': commissionsFbsFirstMileMaxAmountList,
        'commissionsFbsDirectFlowTransMinAmount': commissionsFbsDirectFlowTransMinAmountList,
        'commissionsFbsDirectFlowTransMaxAmount': commissionsFbsDirectFlowTransMaxAmountList,
        'commissionsFbsDelivToCustomerAmount': commissionsFbsDelivToCustomerAmountList,
        'commissionsFbsReturnFlowAmount': commissionsFbsReturnFlowAmountList,
        'commissionsFbsReturnFlowTransMinAmount': commissionsFbsReturnFlowTransMinAmountList,
        'commissionsFbsReturnFlowTransMaxAmount': commissionsFbsReturnFlowTransMaxAmountList,



    })

    return dataFrame


def writeProductlistDataFramesInExcel(productlistModels):
    writer = pd.ExcelWriter('./productlist.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    productlistModelsDataFrame = _getDataFrameByProductlist(productlistModels)
    dataSheets = {'productlist': productlistModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

def _getDataFrameByProductlist(productlistModels):
    productIdList = []
    offerIdList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for productlistModel in productlistModels:
        productIdList.append(productlistModel.productId)
        offerIdList.append(productlistModel.offerId)


    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame(
                 {'productId': productIdList,
                 'offerId': offerIdList,
                 })


    return dataFrame


def writeProductInfolistAllDataFramesInExcel(infoStocksListModels):
    writer = pd.ExcelWriter('./productInfolistAll.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    infoStocksListModelsDataFrame = _getDataFrameByProductInfolistAll(infoStocksListModels)
    dataSheets = {'stocksListResult': infoStocksListModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер
def _getDataFrameByProductInfolistAll(infoStocksListModels):
    idList = []
    nameList = []
    offerIdList = []
    barcodeList = []
    buyboxPriceList = []
    categoryIdList = []
    createdAtList = []
    marketingPriceList = []
    minOzonPriceList = []
    oldPriceList = []
    premiumPriceList = []

    priceList = []
    recommendedPriceList = []
    fboSkuList = []
    fbsSkuList = []
    stateList = []
    stocksComingList = []
    stocksPresentList = []
    stocksReservedList = []
    vatList = []
    visibleList = []
    visibilityDetailsHasPriceList = []
    visibilityDetailsHasStockList = []
    visibilityDetailsActiveProductList = []
    visibilityDetailsReasonsList = []
    priceIndexList = []
    statusStateList = []
    statusStateFailedList = []
    statusModerateStatusList = []
    statusValidationStateList = []
    statusStateNameList = []
    statusStateDescriptionList = []
    statusIsFailedList = []
    statusIsCreatedList = []
    statusStateTooltipList = []
    statusStateUpdatedAtList = []
    statusDeclineReasonsList = []
    statusItemErrorsList = []
    imagesList = []
    colorImageList = []
    images360List = []
    primaryImageList = []
    errorsList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for infoStocksListModel in infoStocksListModels:
        idList.append(infoStocksListModel.id)
        nameList.append(infoStocksListModel.name)
        offerIdList.append(infoStocksListModel.offerId)
        barcodeList.append(infoStocksListModel.barcode)
        buyboxPriceList.append(infoStocksListModel.buyboxPrice)
        categoryIdList.append(infoStocksListModel.categoryId)
        createdAtList.append(infoStocksListModel.createdAt)
        marketingPriceList.append(infoStocksListModel.marketingPrice)
        minOzonPriceList.append(infoStocksListModel.minOzonPrice)
        oldPriceList.append(infoStocksListModel.oldPrice)
        premiumPriceList.append(infoStocksListModel.premiumPrice)

        priceList.append(infoStocksListModel.price)
        recommendedPriceList.append(infoStocksListModel.recommendedPrice)
        fboSkuList.append(infoStocksListModel.fboSku)
        fbsSkuList.append(infoStocksListModel.fbsSku)
        stateList.append(infoStocksListModel.state)
        stocksComingList.append(infoStocksListModel.stocksComing)
        stocksPresentList.append(infoStocksListModel.stocksPresent)
        stocksReservedList.append(infoStocksListModel.stocksReserved)
        vatList.append(infoStocksListModel.vat)
        visibleList.append(infoStocksListModel.visible)
        visibilityDetailsHasPriceList.append(infoStocksListModel.visibilityDetailsHasPrice)
        visibilityDetailsHasStockList.append(infoStocksListModel.visibilityDetailsHasStock)
        visibilityDetailsActiveProductList.append(infoStocksListModel.visibilityDetailsActiveProduct)
        visibilityDetailsReasonsList.append(infoStocksListModel.visibilityDetailsReasons)
        priceIndexList.append(infoStocksListModel.priceIndex)
        statusStateList.append(infoStocksListModel.statusState)
        statusStateFailedList.append(infoStocksListModel.statusStateFailed)
        statusModerateStatusList.append(infoStocksListModel.statusModerateStatus)
        statusValidationStateList.append(infoStocksListModel.statusValidationState)
        statusStateNameList.append(infoStocksListModel.statusStateName)
        statusStateDescriptionList.append(infoStocksListModel.statusStateDescription)
        statusIsFailedList.append(infoStocksListModel.statusIsFailed)
        statusIsCreatedList.append(infoStocksListModel.statusIsCreated)
        statusStateTooltipList.append(infoStocksListModel.statusStateTooltip)
        statusStateUpdatedAtList.append(infoStocksListModel.statusStateUpdatedAt)
        statusDeclineReasonsList.append(infoStocksListModel.statusDeclineReasons)
        statusItemErrorsList.append(infoStocksListModel.statusItemErrors)
        imagesList.append(infoStocksListModel.images)
        colorImageList.append(infoStocksListModel.colorImage)
        images360List.append(infoStocksListModel.images360)
        primaryImageList.append(infoStocksListModel.primaryImage)
        errorsList.append(infoStocksListModel.errors)


    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'id': idList,
                 'name': nameList,
                 'offerId': offerIdList,
                 'barcode': barcodeList,
                 'buyboxPrice': buyboxPriceList,
                 'categoryId': categoryIdList,
                 'createdAt': createdAtList,
                 'marketingPrice': marketingPriceList,

                 'minOzonPrice': minOzonPriceList,
                 'oldPrice': oldPriceList,
                 'premiumPrice': premiumPriceList,
                 'price': priceList,
                 'recommendedPrice': recommendedPriceList,
                 'fboSku': fboSkuList,
                 'fbsSku': fbsSkuList,
                 'state': stateList,
                 'stocksComing': stocksComingList,
                 'stocksPresent': stocksPresentList,
                 'stocksReserved': stocksReservedList,
                 'vat': vatList,
                 'visible': visibleList,
                 'visibilityDetailsHasPrice': visibilityDetailsHasPriceList,
                 'visibilityDetailsHasStock': visibilityDetailsHasStockList,
                 'visibilityDetailsActiveProduct': visibilityDetailsActiveProductList,
                 'visibilityDetailsReasons': visibilityDetailsReasonsList,
                 'priceIndex': priceIndexList,
                 'statusState': statusStateList,
                 'statusStateFailed': statusStateFailedList,
                 'statusModerateStatus': statusModerateStatusList,
                 'statusValidationState': statusValidationStateList,
                 'statusStateName': statusStateNameList,
                 'statusStateDescription': statusStateDescriptionList,
                 'statusIsFailed': statusIsFailedList,
                 'statusIsCreated': statusIsCreatedList,
                 'statusStateTooltip': statusStateTooltipList,
                 'statusStateUpdatedAt': statusStateUpdatedAtList,
                 'statusDeclineReasons': statusDeclineReasonsList,
                 'statusItemErrors': statusItemErrorsList,
                 'images': imagesList,
                 'colorImage': colorImageList,
                 'images360': images360List,
                 'primaryImage': primaryImageList,
                 'errors': errorsList,
    })


    return dataFrame

def writePostingFBOListOrdersDeliveredDataFramesInExcel(postingFBOListOrdersDeliveredModels):
    writer = pd.ExcelWriter('./postingFBOListOrdersDelivered.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    postingFBOListOrdersDeliveredModelsDataFrame = _getDataFrameByPostingFBOListOrdersDeliveredModels(postingFBOListOrdersDeliveredModels)
    dataSheets = {'postingFBOListOrdersDelivered': postingFBOListOrdersDeliveredModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

def _getDataFrameByPostingFBOListOrdersDeliveredModels(postingFBOListOrdersDeliveredModels):
    orderIdList = []
    orderNumberList = []
    postingNumberList = []
    statusList = []
    cancelReasonIdList = []
    createdAtList = []
    inProcessAtList = []
    productsSkuList = []
    productsNameList = []
    productsQuantityList = []
    productsOfferIdList = []
    productsPriceList = []
    analyticsDataRegionList = []
    analyticsDataCityList = []
    analyticsDataDeliveryTypeList = []
    analyticsDataIsPremiumList = []
    analyticsDataPaymentTypeList = []
    analyticsDataWarehouseIdList = []
    analyticsDataWarehouseNameList = []
    analyticsDataIsLegalList = []
    financialDataCommissionAmountList = []
    financialDataCommissionPercentList = []
    financialDataPayoutList = []
    financialDataProductIdList = []
    financialDataOldPriceList = []
    financialDataPriceList = []
    financialDataTotalDiscountValueList = []
    financialDataTotalDiscountPercentList = []
    financialDataActionsList = []
    financialDataPickingList = []
    financialDataQuantityList = []
    financialDataClientPriceList = []
    financialDataFulfillmentList = []
    financialDataPickupList = []
    financialDataPvzList = []
    financialDataScList = []
    financialDataFfList = []
    financialDataDirectTransList = []
    financialDataReturnTransList = []
    financialDataDelivToCustomerList = []
    financialDataReturnNotDelivToCustomerList = []
    financialDataReurnPartGoodToCustomerList = []
    financialDataReturnAfterDelivList = []
    postingFulfillmentList = []
    postingPickupList = []
    postingPvzList = []
    postingScList = []
    postingFfList = []
    postingTransList = []
    postingReturnTransList = []
    postingDelivToCustomerList = []
    postingReturnNotDelivToCustomerList = []
    postingReurnPartGoodToCustomerList = []
    postingReturnAfterDelivList = []
    additionalDataList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for postingFBOListOrdersDeliveredModel in postingFBOListOrdersDeliveredModels:
        orderIdList.append(postingFBOListOrdersDeliveredModel.orderId)
        orderNumberList.append(postingFBOListOrdersDeliveredModel.orderNumber)
        postingNumberList.append(postingFBOListOrdersDeliveredModel.postingNumber)
        statusList.append(postingFBOListOrdersDeliveredModel.status)
        cancelReasonIdList.append(postingFBOListOrdersDeliveredModel.cancelReasonId)
        createdAtList.append(postingFBOListOrdersDeliveredModel.createdAt)
        inProcessAtList.append(postingFBOListOrdersDeliveredModel.inProcessAt)
        productsSkuList.append(postingFBOListOrdersDeliveredModel.productsSku)
        productsNameList.append(postingFBOListOrdersDeliveredModel.productsName)
        productsQuantityList.append(postingFBOListOrdersDeliveredModel.productsQuantity)
        productsOfferIdList.append(postingFBOListOrdersDeliveredModel.productsOfferId)
        productsPriceList.append(postingFBOListOrdersDeliveredModel.productsPrice)
        analyticsDataRegionList.append(postingFBOListOrdersDeliveredModel.analyticsDataRegion)
        analyticsDataCityList.append(postingFBOListOrdersDeliveredModel.analyticsDataCity)
        analyticsDataDeliveryTypeList.append(postingFBOListOrdersDeliveredModel.analyticsDataDeliveryType)
        analyticsDataIsPremiumList.append(postingFBOListOrdersDeliveredModel.analyticsDataIsPremium)
        analyticsDataPaymentTypeList.append(postingFBOListOrdersDeliveredModel.analyticsDataPaymentType)
        analyticsDataWarehouseIdList.append(postingFBOListOrdersDeliveredModel.analyticsDataWarehouseId)
        analyticsDataWarehouseNameList.append(postingFBOListOrdersDeliveredModel.analyticsDataWarehouseName)
        analyticsDataIsLegalList.append(postingFBOListOrdersDeliveredModel.analyticsDataIsLegal)
        financialDataCommissionAmountList.append(postingFBOListOrdersDeliveredModel.financialDataCommissionAmount)
        financialDataCommissionPercentList.append(postingFBOListOrdersDeliveredModel.financialDataCommissionPercent)
        financialDataPayoutList.append(postingFBOListOrdersDeliveredModel.financialDataPayout)
        financialDataProductIdList.append(postingFBOListOrdersDeliveredModel.financialDataProductId)
        financialDataOldPriceList.append(postingFBOListOrdersDeliveredModel.financialDataOldPrice)
        financialDataPriceList.append(postingFBOListOrdersDeliveredModel.financialDataPrice)
        financialDataTotalDiscountValueList.append(postingFBOListOrdersDeliveredModel.financialDataTotalDiscountValue)
        financialDataTotalDiscountPercentList.append(postingFBOListOrdersDeliveredModel.financialDataTotalDiscountPercent)
        financialDataActionsList.append(postingFBOListOrdersDeliveredModel.financialDataActions)
        financialDataPickingList.append(postingFBOListOrdersDeliveredModel.financialDataPicking)
        financialDataQuantityList.append(postingFBOListOrdersDeliveredModel.financialDataQuantity)
        financialDataClientPriceList.append(postingFBOListOrdersDeliveredModel.financialDataClientPrice)
        financialDataFulfillmentList.append(postingFBOListOrdersDeliveredModel.financialDataFulfillment)
        financialDataPickupList.append(postingFBOListOrdersDeliveredModel.financialDataPickup)
        financialDataPvzList.append(postingFBOListOrdersDeliveredModel.financialDataPvz)
        financialDataScList.append(postingFBOListOrdersDeliveredModel.financialDataSc)
        financialDataFfList.append(postingFBOListOrdersDeliveredModel.financialDataFf)
        financialDataDirectTransList.append(postingFBOListOrdersDeliveredModel.financialDataDirectTrans)
        financialDataReturnTransList.append(postingFBOListOrdersDeliveredModel.financialDataReturnTrans)
        financialDataDelivToCustomerList.append(postingFBOListOrdersDeliveredModel.financialDataDelivToCustomer)
        financialDataReturnNotDelivToCustomerList.append(postingFBOListOrdersDeliveredModel.financialDataReturnNotDelivToCustomer)
        financialDataReurnPartGoodToCustomerList.append(postingFBOListOrdersDeliveredModel.financialDataReurnPartGoodToCustomer)
        financialDataReturnAfterDelivList.append(postingFBOListOrdersDeliveredModel.financialDataReturnAfterDeliv)
        postingFulfillmentList.append(postingFBOListOrdersDeliveredModel.postingFulfillment)
        postingPickupList.append(postingFBOListOrdersDeliveredModel.postingPickup)
        postingPvzList.append(postingFBOListOrdersDeliveredModel.postingPvz)
        postingScList.append(postingFBOListOrdersDeliveredModel.postingSc)
        postingFfList.append(postingFBOListOrdersDeliveredModel.postingFf)
        postingTransList.append(postingFBOListOrdersDeliveredModel.postingTrans)
        postingReturnTransList.append(postingFBOListOrdersDeliveredModel.postingReturnTrans)
        postingDelivToCustomerList.append(postingFBOListOrdersDeliveredModel.postingDelivToCustomer)
        postingReturnNotDelivToCustomerList.append(postingFBOListOrdersDeliveredModel.postingReturnNotDelivToCustomer)
        postingReurnPartGoodToCustomerList.append(postingFBOListOrdersDeliveredModel.postingReurnPartGoodToCustomer)
        postingReturnAfterDelivList.append(postingFBOListOrdersDeliveredModel.postingReturnAfterDeliv)
        additionalDataList.append(postingFBOListOrdersDeliveredModel.additionalData)



    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame(
                 {'orderId': orderIdList,
                 'orderNumber': orderNumberList,
                 'postingNumber': postingNumberList,
                 'status': statusList,
                 'cancelReasonId': cancelReasonIdList,
                 'createdAt': createdAtList,
                 'inProcessAt': inProcessAtList,
                 'productsSku': productsSkuList,
                 'productsName': productsNameList,
                 'productsQuantity': productsQuantityList,
                 'productsOfferId': productsOfferIdList,
                 'productsPrice': productsPriceList,
                 'analyticsDataRegion': analyticsDataRegionList,
                 'analyticsDataCity': analyticsDataCityList,
                 'analyticsDataDeliveryType': analyticsDataDeliveryTypeList,
                 'analyticsDataIsPremium': analyticsDataIsPremiumList,
                 'analyticsDataPaymentType': analyticsDataPaymentTypeList,
                 'analyticsDataWarehouseId': analyticsDataWarehouseIdList,
                 'analyticsDataWarehouseName': analyticsDataWarehouseNameList,
                 'analyticsDataIsLegal': analyticsDataIsLegalList,
                 'financialDataCommissionAmount': financialDataCommissionAmountList,
                 'financialDataCommissionPercent': financialDataCommissionPercentList,
                 'financialDataPayout': financialDataPayoutList,
                 'financialDataProductId': financialDataProductIdList,
                 'financialDataOldPrice': financialDataOldPriceList,
                 'financialDataPrice': financialDataPriceList,
                 'financialDataTotalDiscountValue': financialDataTotalDiscountValueList,
                 'financialDataTotalDiscountPercent': financialDataTotalDiscountPercentList,
                 'financialDataActions': financialDataActionsList,
                 'financialDataPicking': financialDataPickingList,
                 'financialDataQuantity': financialDataQuantityList,
                 'financialDataClientPrice': financialDataClientPriceList,
                 'financialDataFulfillment': financialDataFulfillmentList,
                 'financialDataPickup': financialDataPickupList,
                 'financialDataPvz': financialDataPvzList,
                 'financialDataSc': financialDataScList,
                 'financialDataFf': financialDataFfList,
                 'financialDataDirectTrans': financialDataDirectTransList,
                 'financialDataReturnTrans': financialDataReturnTransList,
                 'financialDataDelivToCustomer': financialDataDelivToCustomerList,
                 'financialDataReturnNotDelivToCustomer': financialDataReturnNotDelivToCustomerList,
                 'financialDataReurnPartGoodToCustomer': financialDataReurnPartGoodToCustomerList,
                 'financialDataReturnAfterDeliv': financialDataReturnAfterDelivList,
                 'postingFulfillment': postingFulfillmentList,
                 'postingPickup': postingPickupList,
                 'postingPvz': postingPvzList,
                 'postingSc': postingScList,
                 'postingFf': postingFfList,
                 'postingTrans': postingTransList,
                 'postingReturnTrans': postingReturnTransList,
                 'postingDelivToCustomer': postingDelivToCustomerList,
                 'postingReturnNotDelivToCustomer': postingReturnNotDelivToCustomerList,
                 'postingReurnPartGoodToCustomer': postingReurnPartGoodToCustomerList,
                 'postingReturnAfterDeliv': postingReturnAfterDelivList,
                 'additionalData': additionalDataList,
                 })


    return dataFrame


def writePostingFBSListOrdersDeliveredDataFramesInExcel(postingFBSListOrdersDeliveredModels):
    writer = pd.ExcelWriter('./postingFBSListOrdersDelivered.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    postingFBSListOrdersDeliveredModelsDataFrame = _getDataFrameByPostingFBSListOrdersDeliveredModels(postingFBSListOrdersDeliveredModels)
    dataSheets = {'postingFBSListOrdersDelivered': postingFBSListOrdersDeliveredModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

def _getDataFrameByPostingFBSListOrdersDeliveredModels(postingFBSListOrdersDeliveredModels):
    orderIdList = []
    orderNumberList = []
    postingNumberList = []
    statusList = []
    deliveringDateList = []
    shipmentDateList = []
    inProcessAtList = []
    trackingNumberList = []
    tplIntegrationTypeList = []
    tplProviderIdList = []
    providerNameList = []
    tplProviderList = []
    deliveryMethodIdList = []
    warehouseIdList = []
    warehouseList = []
    cancelReasonIdList = []
    cancellationInitiatorList = []
    cancellationTypeList = []
    affectCancellationRatingList = []
    cancelledAfterShipList = []
    cancelReasonList = []
    productsSkuList = []
    productsNameList = []
    productsQuantityList = []
    productsOfferIdList = []
    productsPriceList = []
    productsMandatoryMarkList = []
    analyticsDataRegionList = []
    analyticsDataCityList = []
    analyticsDataDeliveryTypeList = []
    analyticsDataIsPremiumList = []
    analyticsDataPaymentTypeList = []
    analyticsDataWarehouseIdList = []
    analyticsDataWarehouseList = []
    analyticsDataTplProviderIdList = []
    analyticsDataTplProviderList = []
    analyticsDataDeliveryDateBeginList = []
    analyticsDataDeliveryDateEndList = []
    analyticsDataIsLegalList = []
    financialDataProductIdList = []
    financialDataCommissionPercentList = []
    financialDataPayoutList = []
    financialDataTotalDiscountValueList = []
    financialDataOldPriceList = []
    financialDataActionsList = []
    financialDataTotalDiscountPercentList = []
    financialDataPickingList = []
    financialDataCommissionAmountList = []
    financialDataPickupList = []
    financialDataQuantityList = []
    financialDataClientPriceList = []
    postingFulfillmentList = []
    postingPickupList = []
    postingPvzList = []
    postingScList = []
    postingFfList = []
    postingTransList = []
    postingReturnTransList = []
    postingDelivToCustomerList = []
    postingReturnNotDelivToCustomerList = []
    postingReurnPartGoodToCustomerList = []
    postingReturnAfterDelivList = []
    customerList = []
    addresseeList = []
    isExpressList = []
    requirementsCountryList = []
    requirementsGtdList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for postingFBSListOrdersDeliveredModel in postingFBSListOrdersDeliveredModels:
        orderIdList.append(postingFBSListOrdersDeliveredModel.orderId)
        orderNumberList.append(postingFBSListOrdersDeliveredModel.orderNumber)
        postingNumberList.append(postingFBSListOrdersDeliveredModel.postingNumber)
        statusList.append(postingFBSListOrdersDeliveredModel.status)
        deliveringDateList.append(postingFBSListOrdersDeliveredModel.deliveringDate)
        shipmentDateList.append(postingFBSListOrdersDeliveredModel.shipmentDate)
        inProcessAtList.append(postingFBSListOrdersDeliveredModel.inProcessAt)
        trackingNumberList.append(postingFBSListOrdersDeliveredModel.trackingNumber)
        tplIntegrationTypeList.append(postingFBSListOrdersDeliveredModel.tplIntegrationType)
        tplProviderIdList.append(postingFBSListOrdersDeliveredModel.tplProviderId)
        providerNameList.append(postingFBSListOrdersDeliveredModel.providerName)
        tplProviderList.append(postingFBSListOrdersDeliveredModel.tplProvider)
        deliveryMethodIdList.append(postingFBSListOrdersDeliveredModel.deliveryMethodId)
        warehouseIdList.append(postingFBSListOrdersDeliveredModel.warehouseId)
        warehouseList.append(postingFBSListOrdersDeliveredModel.warehouse)
        cancelReasonIdList.append(postingFBSListOrdersDeliveredModel.cancelReasonId)
        cancellationInitiatorList.append(postingFBSListOrdersDeliveredModel.cancellationInitiator)
        cancellationTypeList.append(postingFBSListOrdersDeliveredModel.cancellationType)
        affectCancellationRatingList.append(postingFBSListOrdersDeliveredModel.affectCancellationRating)
        cancelledAfterShipList.append(postingFBSListOrdersDeliveredModel.cancelledAfterShip)
        cancelReasonList.append(postingFBSListOrdersDeliveredModel.cancelReason)
        productsSkuList.append(postingFBSListOrdersDeliveredModel.productsSku)
        productsNameList.append(postingFBSListOrdersDeliveredModel.productsName)
        productsQuantityList.append(postingFBSListOrdersDeliveredModel.productsQuantity)
        productsOfferIdList.append(postingFBSListOrdersDeliveredModel.productsOfferId)
        productsPriceList.append(postingFBSListOrdersDeliveredModel.productsPrice)
        productsMandatoryMarkList.append(postingFBSListOrdersDeliveredModel.productsMandatoryMark)
        analyticsDataRegionList.append(postingFBSListOrdersDeliveredModel.analyticsDataRegion)
        analyticsDataCityList.append(postingFBSListOrdersDeliveredModel.analyticsDataCity)
        analyticsDataDeliveryTypeList.append(postingFBSListOrdersDeliveredModel.analyticsDataDeliveryType)
        analyticsDataIsPremiumList.append(postingFBSListOrdersDeliveredModel.analyticsDataIsPremium)
        analyticsDataPaymentTypeList.append(postingFBSListOrdersDeliveredModel.analyticsDataPaymentType)
        analyticsDataWarehouseIdList.append(postingFBSListOrdersDeliveredModel.analyticsDataWarehouseId)
        analyticsDataWarehouseList.append(postingFBSListOrdersDeliveredModel.analyticsDataWarehouse)
        analyticsDataTplProviderIdList.append(postingFBSListOrdersDeliveredModel.analyticsDataTplProviderId)
        analyticsDataTplProviderList.append(postingFBSListOrdersDeliveredModel.analyticsDataTplProvider)
        analyticsDataDeliveryDateBeginList.append(postingFBSListOrdersDeliveredModel.analyticsDataDeliveryDateBegin)
        analyticsDataDeliveryDateEndList.append(postingFBSListOrdersDeliveredModel.analyticsDataDeliveryDateEnd)
        analyticsDataIsLegalList.append(postingFBSListOrdersDeliveredModel.analyticsDataIsLegal)
        financialDataProductIdList.append(postingFBSListOrdersDeliveredModel.financialDataProductId)
        financialDataCommissionPercentList.append(postingFBSListOrdersDeliveredModel.financialDataCommissionPercent)
        financialDataPayoutList.append(postingFBSListOrdersDeliveredModel.financialDataPayout)
        financialDataTotalDiscountValueList.append(postingFBSListOrdersDeliveredModel.financialDataTotalDiscountValue)
        financialDataOldPriceList.append(postingFBSListOrdersDeliveredModel.financialDataOldPrice)
        financialDataActionsList.append(postingFBSListOrdersDeliveredModel.financialDataActions)
        financialDataTotalDiscountPercentList.append(postingFBSListOrdersDeliveredModel.financialDataTotalDiscountPercent)
        financialDataPickingList.append(postingFBSListOrdersDeliveredModel.financialDataPicking)
        financialDataCommissionAmountList.append(postingFBSListOrdersDeliveredModel.financialDataCommissionAmount)
        financialDataPickupList.append(postingFBSListOrdersDeliveredModel.financialDataPickup)
        financialDataQuantityList.append(postingFBSListOrdersDeliveredModel.financialDataQuantity)
        financialDataClientPriceList.append(postingFBSListOrdersDeliveredModel.financialDataClientPrice)
        postingFulfillmentList.append(postingFBSListOrdersDeliveredModel.postingFulfillment)
        postingPickupList.append(postingFBSListOrdersDeliveredModel.postingPickup)
        postingPvzList.append(postingFBSListOrdersDeliveredModel.postingPvz)
        postingScList.append(postingFBSListOrdersDeliveredModel.postingSc)
        postingFfList.append(postingFBSListOrdersDeliveredModel.postingFf)
        postingTransList.append(postingFBSListOrdersDeliveredModel.postingTrans)
        postingReturnTransList.append(postingFBSListOrdersDeliveredModel.postingReturnTrans)
        postingDelivToCustomerList.append(postingFBSListOrdersDeliveredModel.postingDelivToCustomer)
        postingReturnNotDelivToCustomerList.append(postingFBSListOrdersDeliveredModel.postingReturnNotDelivToCustomer)
        postingReurnPartGoodToCustomerList.append(postingFBSListOrdersDeliveredModel.postingReurnPartGoodToCustomer)
        postingReturnAfterDelivList.append(postingFBSListOrdersDeliveredModel.postingReturnAfterDeliv)
        customerList.append(postingFBSListOrdersDeliveredModel.customer)
        addresseeList.append(postingFBSListOrdersDeliveredModel.addressee)
        isExpressList.append(postingFBSListOrdersDeliveredModel.isExpress)
        requirementsCountryList.append(postingFBSListOrdersDeliveredModel.requirementsCountry)
        requirementsGtdList.append(postingFBSListOrdersDeliveredModel.requirementsGtd)



    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame(
                 {'orderId': orderIdList,
                 'orderNumber': orderNumberList,
                 'postingNumber': postingNumberList,
                 'status': statusList,
                 'deliveringDate': deliveringDateList,
                 'shipmentDate': shipmentDateList,
                 'inProcessAt': inProcessAtList,
                 'trackingNumber': trackingNumberList,
                 'tplIntegrationType': tplIntegrationTypeList,
                 'tplProviderId': tplProviderIdList,
                 'providerName': providerNameList,
                 'tplProvider': tplProviderList,
                 'deliveryMethodId': deliveryMethodIdList,
                 'warehouseId': warehouseIdList,
                 'warehouse': warehouseList,
                 'cancelReasonId': cancelReasonIdList,
                 'cancellationInitiator': cancellationInitiatorList,
                 'cancellationType': cancellationTypeList,
                 'affectCancellationRating': affectCancellationRatingList,
                 'cancelledAfterShip': cancelledAfterShipList,
                 'cancelReason': cancelReasonList,
                 'productsSku': productsSkuList,
                 'productsName': productsNameList,
                 'productsQuantity': productsQuantityList,
                 'productsOfferId': productsOfferIdList,
                 'productsPrice': productsPriceList,
                 'productsMandatoryMark': productsMandatoryMarkList,

                 'analyticsDataRegion': analyticsDataRegionList,
                 'analyticsDataCity': analyticsDataCityList,
                 'analyticsDataDeliveryType': analyticsDataDeliveryTypeList,
                 'analyticsDataIsPremium': analyticsDataIsPremiumList,
                 'analyticsDataPaymentType': analyticsDataPaymentTypeList,
                 'analyticsDataWarehouseId': analyticsDataWarehouseIdList,
                 'analyticsDataWarehouse': analyticsDataWarehouseList,
                 'analyticsDataTplProviderId': analyticsDataTplProviderIdList,
                 'analyticsDataTplProvider': analyticsDataTplProviderList,
                 'analyticsDataDeliveryDateBegin': analyticsDataDeliveryDateBeginList,
                 'analyticsDataDeliveryDateEnd': analyticsDataDeliveryDateEndList,
                 'analyticsDataIsLegal': analyticsDataIsLegalList,
                 'financialDataProductId': financialDataProductIdList,
                 'financialDataCommissionPercent': financialDataCommissionPercentList,
                 'financialDataPayout': financialDataPayoutList,
                 'financialDataTotalDiscountValue': financialDataTotalDiscountValueList,
                 'financialDataOldPrice': financialDataOldPriceList,
                 'financialDataActions': financialDataActionsList,
                 'financialDataTotalDiscountPercent': financialDataTotalDiscountPercentList,
                  'financialDataPicking': financialDataPickingList,
                 'financialDataCommissionAmount': financialDataCommissionAmountList,
                  'financialDataPickup': financialDataPickupList,
                  'financialDataQuantity': financialDataQuantityList,
                 'financialDataClientPrice': financialDataClientPriceList,

                 'postingFulfillment': postingFulfillmentList,
                 'postingPickup': postingPickupList,
                 'postingPvz': postingPvzList,
                 'postingSc': postingScList,
                 'postingFf': postingFfList,
                 'postingTrans': postingTransList,
                 'postingReturnTrans': postingReturnTransList,
                 'postingDelivToCustomer': postingDelivToCustomerList,
                 'postingReturnNotDelivToCustomer': postingReturnNotDelivToCustomerList,
                 'postingReurnPartGoodToCustomer': postingReurnPartGoodToCustomerList,
                 'postingReturnAfterDeliv': postingReturnAfterDelivList,

                 'customer': customerList,
                 'addressee': addresseeList,
                 'isExpress': isExpressList,
                 'requirementsCountry': requirementsCountryList,
                 'requirementsGtd': requirementsGtdList,
                 })


    return dataFrame


def writeFinanceTransactionListOrdersDataFramesInExcel(financeTransactionListOrdersModels):
    writer = pd.ExcelWriter('./financeTransactionOrders.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    financeTransactionListOrdersModelsDataFrame = _getDataFrameByFinanceTransactionListOrders(financeTransactionListOrdersModels)
    dataSheets = {'financeOrdersResult': financeTransactionListOrdersModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

def _getDataFrameByFinanceTransactionListOrders(financeTransactionListOrdersModels):
    operationIdList = []
    operationTypeList = []
    operationDateList = []
    operationTypeNameList = []
    deliveryChargeList = []
    returnDeliveryChargeList = []
    accrualsForSaleList = []
    saleCommissionList = []
    amountList = []
    typeList = []
    postingDeliverySchemaList = []
    postingPostingNumberList = []
    postingOrderDateList = []
    postingWarehouseIdList = []
    itemsNameList = []
    itemsSkuList = []
    servicesDelivToCustomerNameList = []
    servicesDelivToCustomerPriceList = []
    servicesDirectFlowLogisticNameList = []
    servicesDirectFlowLogisticPriceList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for financeTransactionListOrdersModel in financeTransactionListOrdersModels:
        operationIdList.append(financeTransactionListOrdersModel.operationId)
        operationTypeList.append(financeTransactionListOrdersModel.operationType)
        operationDateList.append(financeTransactionListOrdersModel.operationDate)
        operationTypeNameList.append(financeTransactionListOrdersModel.operationTypeName)
        deliveryChargeList.append(financeTransactionListOrdersModel.deliveryCharge)
        returnDeliveryChargeList.append(financeTransactionListOrdersModel.returnDeliveryCharge)
        accrualsForSaleList.append(financeTransactionListOrdersModel.accrualsForSale)
        saleCommissionList.append(financeTransactionListOrdersModel.saleCommission)
        amountList.append(financeTransactionListOrdersModel.amount)
        typeList.append(financeTransactionListOrdersModel.type)
        postingDeliverySchemaList.append(financeTransactionListOrdersModel.postingDeliverySchema)
        postingPostingNumberList.append(financeTransactionListOrdersModel.postingPostingNumber)
        postingOrderDateList.append(financeTransactionListOrdersModel.postingOrderDate)
        postingWarehouseIdList.append(financeTransactionListOrdersModel.postingWarehouseId)
        itemsNameList.append(financeTransactionListOrdersModel.itemsName)
        itemsSkuList.append(financeTransactionListOrdersModel.itemsSku)
        servicesDelivToCustomerNameList.append(financeTransactionListOrdersModel.servicesDelivToCustomerName)
        servicesDelivToCustomerPriceList.append(financeTransactionListOrdersModel.servicesDelivToCustomerPrice)
        servicesDirectFlowLogisticNameList.append(financeTransactionListOrdersModel.servicesDirectFlowLogisticName)
        servicesDirectFlowLogisticPriceList.append(financeTransactionListOrdersModel.servicesDirectFlowLogisticPrice)



    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame(
                 {'operationId': operationIdList,
                 'operationType': operationTypeList,
                 'operationDate': operationDateList,
                 'operationTypeName': operationTypeNameList,
                 'deliveryCharge': deliveryChargeList,
                 'returnDeliveryCharge': returnDeliveryChargeList,
                 'accrualsForSale': accrualsForSaleList,
                 'saleCommission': saleCommissionList,
                 'amount': amountList,
                 'type': typeList,
                 'postingDeliverySchema': postingDeliverySchemaList,
                 'postingPostingNumber': postingPostingNumberList,
                 'postingOrderDate': postingOrderDateList,
                 'postingWarehouseId': postingWarehouseIdList,
                 'itemsName': itemsNameList,
                 'itemsSku': itemsSkuList,
                 'servicesDelivToCustomerName': servicesDelivToCustomerNameList,
                 'servicesDelivToCustomerPrice': servicesDelivToCustomerPriceList,
                 'servicesDirectFlowLogisticName': servicesDirectFlowLogisticNameList,
                 'servicesDirectFlowLogisticPrice': servicesDirectFlowLogisticPriceList,
                 })


    return dataFrame


def writeFinanceTotalsDataFramesInExcel(financeTotalsModels):
    writer = pd.ExcelWriter('./financeTotals.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    financeTotalsModelsDataFrame = _getDataFrameByFinanceTotals(financeTotalsModels)
    dataSheets = {'financeTotals': financeTotalsModelsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

def _getDataFrameByFinanceTotals(financeTotalsModels):
    accrualsForSaleList = []
    saleCommissionList = []
    processingAndDeliveryList = []
    refundsAndCancellationsList = []
    servicesAmountList = []
    compensationAmountList = []
    moneyTransferList = []
    othersAmountList = []



    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for financeTotalsModel in financeTotalsModels:
        accrualsForSaleList.append(financeTotalsModel.accrualsForSale)
        saleCommissionList.append(financeTotalsModel.saleCommission)
        processingAndDeliveryList.append(financeTotalsModel.processingAndDelivery)
        refundsAndCancellationsList.append(financeTotalsModel.refundsAndCancellations)
        servicesAmountList.append(financeTotalsModel.servicesAmount)
        compensationAmountList.append(financeTotalsModel.compensationAmount)
        moneyTransferList.append(financeTotalsModel.moneyTransfer)
        othersAmountList.append(financeTotalsModel.othersAmount)



    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame(
                 {'accrualsForSale': accrualsForSaleList,
                 'saleCommission': saleCommissionList,
                 'processingAndDelivery': processingAndDeliveryList,
                 'refundsAndCancellations': refundsAndCancellationsList,
                 'servicesAmount': servicesAmountList,
                 'compensationAmount': compensationAmountList,
                 'moneyTransfer': moneyTransferList,
                 'othersAmount': othersAmountList,
                 })


    return dataFrame


