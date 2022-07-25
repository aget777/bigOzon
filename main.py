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


    infoStocksModels = ProductInfoStock_01.getProductInfoStocks()
    infoStocksListModels = ProductInfoListStocks_02.getProductInfoListStocks()
    productInfoPricesModels = ProductInfoPrices_03.getProductInfoPrices()
    productInfoPricesCommissionsModels = ProductInfoPricesСommissions_04.getProductInfoPricesCommissionsModels()
    productlistModels = Productlist_05.getProductlist()
    productInfolistAllModels = ProductInfolistAll_06.getProductInfolistAll()
    postingFBOListOrdersDeliveredModels = PostingFBOListOrdersDelivered_07.getPostingFBOListOrdersDelivered()
    postingFBSListOrdersDeliveredModels = PostingFBSListOrdersDelivered_08.getPostingFBSListOrdersDelivered()
    financeTransactionListOrdersModels = FinanceTransactionListOrders_09.getFinanceTransactionListOrders()
    financeTotalsModels = FinanceTotals_10.getFinanceTotals()


    # FileRepository.setInfoStocksInFile(infoStocksModels)
    # FileRepository.setInfoListStocksInFile(infoStocksListModels)
    # FileRepository.setProductInfoPricesInFile(productInfoPricesModels)
    # FileRepository.setProductInfoPricesCommissionsInFile(productInfoPricesCommissionsModels)
    # FileRepository.setProductlistInFile(productlistModels)
    # FileRepository.setProductInfolistAllInFile(productInfolistAllModels)
    # FileRepository.setPostingFBOListOrdersDeliveredInFile(postingFBOListOrdersDeliveredModels)


    ExcelRepository.writeInfoStocksDataFramesInExcel(infoStocksModels)
    ExcelRepository.writeInfoListStocksDataFramesInExcel(infoStocksListModels)
    ExcelRepository.writeProductInfoPricesDataFramesInExcel(productInfoPricesModels)
    ExcelRepository.writeProductInfoPricesCommissionsDataFramesInExcel(productInfoPricesCommissionsModels)
    ExcelRepository.writeProductlistDataFramesInExcel(productlistModels)
    ExcelRepository.writeProductInfolistAllDataFramesInExcel(productInfolistAllModels)
    ExcelRepository.writePostingFBOListOrdersDeliveredDataFramesInExcel(postingFBOListOrdersDeliveredModels)
    ExcelRepository.writePostingFBSListOrdersDeliveredDataFramesInExcel(postingFBSListOrdersDeliveredModels)
    ExcelRepository.writeFinanceTransactionListOrdersDataFramesInExcel(financeTransactionListOrdersModels)
    ExcelRepository.writeFinanceTotalsDataFramesInExcel(financeTotalsModels)


