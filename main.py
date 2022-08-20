from Services import ProductInfoStock_01
from Services import ProductInfoListStocks_02
from Services import ProductInfoPrices_03
from Services import ProductInfoPricesСommissions_04
from Services import Productlist_05
from Services import ProductInfolistAll_06
from Services import PostingFBOListOrdersDelivered_07
from Services import PostingFBSListOrdersDelivered_08
from Services import FinanceTransactionListOrders_09
from Services import FinanceTotals_10


from Repositories import FileRepository
from Repositories import ExcelRepository

if __name__ == '__main__':
    offerIds = ProductInfoStock_01.getOfferIds()
    infoStocksByOfferIds = ProductInfoListStocks_02.getProductInfosByOfferIds(offerIds) # блок 1 список товаров и характеристик
    ExcelRepository.writeInfoListStocksDataFramesInExcel(infoStocksByOfferIds) # блок 1 список товаров и характеристик

    infoStocksModels = ProductInfoStock_01.getProductInfoStocks() # блок 1 список товаров и характеристик

    # infoStocksListModels = ProductInfoListStocks_02.getProductInfoListStocks() # старый файл не нужен

    postingFBOListOrdersDeliveredModels = PostingFBOListOrdersDelivered_07.getPostingFBOListOrdersDelivered()
    postingFBSListOrdersDeliveredModels = PostingFBSListOrdersDelivered_08.getPostingFBSListOrdersDelivered()
    financeTransactionListOrdersModels = FinanceTransactionListOrders_09.getFinanceTransactionListOrders()
    financeTotalsModels = FinanceTotals_10.getFinanceTotals()


    # ExcelRepository.writeInfoStocksDataFramesInExcel(infoStocksModels) # блок 1 список товаров и характеристик
    # ExcelRepository.writeInfoListStocksDataFramesInExcel(infoStocksListModels)

    # ExcelRepository.writeProductInfoPricesDataFramesInExcel(productInfoPricesModels)                # не нужен
    # ExcelRepository.writeProductInfoPricesCommissionsDataFramesInExcel(productInfoPricesCommissionsModels)                # не нужен
    # ExcelRepository.writeProductlistDataFramesInExcel(productlistModels)                # не нужен
    # ExcelRepository.writeProductInfolistAllDataFramesInExcel(productInfolistAllModels)                # не нужен

    ExcelRepository.writePostingFBOListOrdersDeliveredDataFramesInExcel(postingFBOListOrdersDeliveredModels)
    ExcelRepository.writePostingFBSListOrdersDeliveredDataFramesInExcel(postingFBSListOrdersDeliveredModels)
    ExcelRepository.writeFinanceTransactionListOrdersDataFramesInExcel(financeTransactionListOrdersModels)
    ExcelRepository.writeFinanceTotalsDataFramesInExcel(financeTotalsModels)


