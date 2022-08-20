# Модель сделок


class InfoStockModel:
    def __init__(self, json) -> None:
        self.productId = json['product_id']                                                   # id товара
        self.offerId = json['offer_id']                                                       # ID товара в системе продавца — артикул
        self.stockTypeFirst = json['stocks'][0]['type']                                       # тип склада FBO
        self.presentStockFirst = json['stocks'][0]['present']                                 # количество на складе FBO
        self.reservedStockFirst = json['stocks'][0]['reserved']                               # зарезирвированно на складе FBO
        # self.stockTypeSecond = json['stocks'][1]['type']                                    # тип склада FBS
        self.stockTypeSecond = self._getAdditionalParams(json['stocks'], 'type', 1)           # тип склада FBS
        # self.presentStockSecond = json['stocks'][1]['present']                              # количество на складе FBS
        self.presentStockSecond = self._getAdditionalParams(json['stocks'], 'present', 1)     # количество на складе FBS
        # self.reservedStockSecond = json['stocks'][1]['reserved']                            # зарезирвированно на складе FBS
        self.reservedStockSecond = self._getAdditionalParams(json['stocks'], 'reserved', 1)   # зарезирвированно на складе FBS

 # Две очень простые и очень мощные функции
    def _getFirstOrDefault(self, items, itemName):
        result = []
        for item in items:
            result.append(item[itemName])
        return result

    def _getAdditionalParams(self, services, itemName, index):
        return services[index][itemName] if len(services) > index else ''

class InfoStockModelList:
    def __init__(self, json) -> None:
        self.id = json['id']                                                   # Идентификатор товара
        self.name = json['name']                                               # Наименование товара
        self.offerId = json['offer_id']                                        # ID товара в системе продавца — артикул
        self.barcode = json['barcode']                                         # Штрих-код
        self.buyboxPrice = json['buybox_price']                                # Цена упаковки
        self.categoryId = json['category_id']                                  # Идентификатор категории
        self.createdAt = json['created_at']                                    # Дата создания
        self.marketingPrice = json['marketing_price']                         # Маркетинговая цена
        self.minOzonPrice = json['min_ozon_price']                            # Минимальная цена товара после применения акций
        self.oldPrice = json['old_price']                                     # Прежняя цена
        self.premiumPrice = json['premium_price']                             # Цена для покупателей с подпиской Ozon Premium
        self.price = json['price']                                            # Цена, по которой товар продаётся сейчас
        self.recommendedPrice = json['recommended_price']                     # Рекомендуемая цена
        self.fboSku = json['fbo_sku']                                         # FBO Идентификатор товара в системе Ozon
        self.fbsSku = json['fbs_sku']                                         # FBS Идентификатор товара в системе Ozon
        self.state = json['state']                                            # Состояние
        self.stocksComing = json['stocks']['coming']                          # Приход
        self.stocksPresent = json['stocks']['present']                        # Наличие
        self.stocksReserved = json['stocks']['reserved']                      # Зарезервировано поĸупателями
        self.vat = json['vat']                                                # НДС
        self.visible = json['visible']                                        # Видимость
        self.visibilityDetailsHasPrice = json['visibility_details']['has_price']               # Детали цены
        self.visibilityDetailsHasStock = json['visibility_details']['has_stock']               # Наличие на складе
        self.visibilityDetailsActiveProduct = json['visibility_details']['active_product']     # Активный продукт
        self.visibilityDetailsReasons = json['visibility_details']['reasons']                   # Причины
        self.priceIndex = json['price_index']                                 # Индекс цен
        self.statusState = json['status']['state']                            # Статус состояние
        self.statusStateFailed = json['status']['state_failed']               # Отказ в публикации
        self.statusModerateStatus = json['status']['moderate_status']         # Статус модерации
        self.statusValidationState = json['status']['validation_state']       # Статус валидации
        self.statusStateName = json['status']['state_name']                   # Название статуса
        self.statusStateDescription = json['status']['state_description']     # Описание статуса
        self.statusIsFailed = json['status']['is_failed']                     # Отказ в регистрации
        self.statusIsCreated = json['status']['is_created']                   # Опубликован
        self.statusStateTooltip = json['status']['state_tooltip']             # Подсказки для состояния
        self.statusStateUpdatedAt = json['status']['state_updated_at']        # Дата обновления
        self.statusDeclineReasons = json['status']['decline_reasons']        # Причины отказа
        self.statusItemErrors = json['status']['item_errors']                # Ошибки при создании
        self.images = json['images']                                         # Изображение
        self.colorImage = json['color_image']                                # Цветное изображение
        self.images360 = json['images360']                                   # Изображения на 360
        self.primaryImage = json['primary_image']                            # Главное изображение
        self.errors = json['errors']                                         # Ошибки




class ProductInfoPricesModels:
    def __init__(self, json) -> None:
        self.productId = json['product_id']  # Идентификатор товара
        self.offerId = json['offer_id']  # ID товара в системе продавца — артикул
        self.pricePrice = json['price']['price']  # Цена, по которой товар продаётся сейчас
        self.priceOldPrice = json['price']['old_price']  # Прежняя цена
        self.pricePremiumPrice = json['price']['premium_price']  # Цена для покупателей с подпиской Ozon Premium
        self.priceRecommendedPrice = json['price']['recommended_price']  # Рекомендуемая цена
        self.priceRetailPrice = json['price']['retail_price']  #
        self.priceVat = json['price']['vat']                     # НДС

        self.priceMinPrice = json['price']['min_price']  # Минимальная цена товара после применения акций
        self.priceMarketingPrice = json['price']['marketing_price']  # Маркетинговая цена
        self.priceMarketingSellerPrice = json['price']['marketing_seller_price']  #
        self.priceIndex = json['price_index']  # Индекс цен
        self.volumeWeight = json['volume_weight']  #


class ProductInfoPricesCommissionsModels:
    def __init__(self, json) -> None:
        self.productId = json['product_id']  # Идентификатор товара
        self.offerId = json['offer_id']  # ID товара в системе продавца — артикул
        self.pricePrice = json['price']['price']  # Цена, по которой товар продаётся сейчас

        self.commissionsSalesPercent = json['commissions']['sales_percent']  #
        self.commissionsFboFulfillmentAmount = json['commissions']['fbo_fulfillment_amount']  #
        self.commissionsFboDirectFlowTransMinAmount = json['commissions']['fbo_direct_flow_trans_min_amount']  #
        self.commissionsFboDirectFlowTransMaxAmount = json['commissions']['fbo_direct_flow_trans_max_amount']  #
        self.commissionsFboDelivToCustomerAmount = json['commissions']['fbo_deliv_to_customer_amount']  #
        self.commissionsFboReturnFlowAmount = json['commissions']['fbo_return_flow_amount']  #
        self.commissionsFbsFirstMileMinAmount = json['commissions']['fbs_first_mile_min_amount']  #
        self.commissionsFbsFirstMileMaxAmount = json['commissions']['fbs_first_mile_max_amount']  #
        self.commissionsFbsDirectFlowTransMinAmount = json['commissions']['fbs_direct_flow_trans_min_amount']  #
        self.commissionsFbsDirectFlowTransMaxAmount = json['commissions']['fbs_direct_flow_trans_max_amount']  #
        self.commissionsFbsDelivToCustomerAmount = json['commissions']['fbs_deliv_to_customer_amount']  #
        self.commissionsFbsReturnFlowAmount = json['commissions']['fbs_return_flow_amount']  #
        self.commissionsFbsReturnFlowTransMinAmount = json['commissions']['fbs_return_flow_trans_min_amount']  #
        self.commissionsFbsReturnFlowTransMaxAmount = json['commissions']['fbs_return_flow_trans_max_amount']  #


class ProductlistModels:
    def __init__(self, json) -> None:
        self.productId = json['product_id']  # Идентификатор товара
        self.offerId = json['offer_id']  # ID товара в системе продавца — артикул

class PostingFBOListOrdersDeliveredModels:
    def __init__(self, json) -> None:
        self.orderId = json['order_id']  # ID заказа
        self.orderNumber = json['order_number']  # Номер заказа
        self.postingNumber = json['posting_number']  # Номер отправления
        self.status = json['status']  # Статус отправления
        self.cancelReasonId = json['cancel_reason_id']  # ID причины отказа
        self.createdAt = json['created_at']  # Дата создания
        self.inProcessAt = json['in_process_at']  # В обработке
        self.productsSku = json['products'][0]['sku']  # Идентификатор товара в системе Ozon
        self.productsName = json['products'][0]['name']  # Наименование товара
        self.productsQuantity = json['products'][0]['quantity']  # Количество товара
        self.productsOfferId = json['products'][0]['offer_id']  # ID товара в системе продавца — артикул
        self.productsPrice = json['products'][0]['price']  # Цена продажи
        self.analyticsDataRegion = json['analytics_data']['region']  # Регион
        self.analyticsDataCity = json['analytics_data']['city']  # Город
        self.analyticsDataDeliveryType = json['analytics_data']['delivery_type']  # Тип доставки
        self.analyticsDataIsPremium = json['analytics_data']['is_premium']  #  Подписка Ozon Premium
        self.analyticsDataPaymentType = json['analytics_data']['payment_type_group_name']  # Способ оплаты
        self.analyticsDataWarehouseId = json['analytics_data']['warehouse_id']  # ID склада
        self.analyticsDataWarehouseName = json['analytics_data']['warehouse_name']  # Наименование склада
        self.analyticsDataIsLegal = json['analytics_data']['is_legal']  #
        self.financialDataCommissionAmount = json['financial_data']['products'][0]['commission_amount']  # Размер комиссии
        self.financialDataCommissionPercent = json['financial_data']['products'][0]['commission_percent']  # Процент комиссии
        self.financialDataPayout = json['financial_data']['products'][0]['payout']  # Выплата
        self.financialDataProductId = json['financial_data']['products'][0]['product_id']  # Идентификатор товара
        self.financialDataOldPrice = json['financial_data']['products'][0]['old_price']  # Прежняя цена
        self.financialDataPrice = json['financial_data']['products'][0]['price']  # Цена продажи
        self.financialDataTotalDiscountValue = json['financial_data']['products'][0]['total_discount_value']  # Общая стоимость скидки
        self.financialDataTotalDiscountPercent = json['financial_data']['products'][0]['total_discount_percent']  # Общий процент скидки
        self.financialDataActions = json['financial_data']['products'][0]['actions']  # Акции
        self.financialDataPicking = json['financial_data']['products'][0]['picking']  # Сортировка
        self.financialDataQuantity = json['financial_data']['products'][0]['quantity']  # Количество
        self.financialDataClientPrice = json['financial_data']['products'][0]['client_price']  # Цена клиента
        self.financialDataFulfillment = json['financial_data']['products'][0]['item_services']['marketplace_service_item_fulfillment']  #
        self.financialDataPickup = json['financial_data']['products'][0]['item_services']['marketplace_service_item_pickup']  #
        self.financialDataPvz = json['financial_data']['products'][0]['item_services']['marketplace_service_item_dropoff_pvz']  #
        self.financialDataSc = json['financial_data']['products'][0]['item_services']['marketplace_service_item_dropoff_sc']  #
        self.financialDataFf = json['financial_data']['products'][0]['item_services']['marketplace_service_item_dropoff_ff']  #
        self.financialDataDirectTrans = json['financial_data']['products'][0]['item_services']['marketplace_service_item_direct_flow_trans']  #
        self.financialDataReturnTrans = json['financial_data']['products'][0]['item_services']['marketplace_service_item_return_flow_trans']  #
        self.financialDataDelivToCustomer = json['financial_data']['products'][0]['item_services']['marketplace_service_item_deliv_to_customer']  #
        self.financialDataReturnNotDelivToCustomer = json['financial_data']['products'][0]['item_services']['marketplace_service_item_return_not_deliv_to_customer']  #
        self.financialDataReurnPartGoodToCustomer = json['financial_data']['products'][0]['item_services']['marketplace_service_item_return_part_goods_customer']  #
        self.financialDataReturnAfterDeliv = json['financial_data']['products'][0]['item_services']['marketplace_service_item_return_after_deliv_to_customer']  #
        self.postingFulfillment = json['financial_data']['posting_services']['marketplace_service_item_fulfillment']
        self.postingPickup = json['financial_data']['posting_services']['marketplace_service_item_pickup']
        self.postingPvz = json['financial_data']['posting_services']['marketplace_service_item_dropoff_pvz']
        self.postingSc = json['financial_data']['posting_services']['marketplace_service_item_dropoff_sc']
        self.postingFf = json['financial_data']['posting_services']['marketplace_service_item_dropoff_ff']
        self.postingTrans = json['financial_data']['posting_services']['marketplace_service_item_direct_flow_trans']
        self.postingReturnTrans = json['financial_data']['posting_services']['marketplace_service_item_return_flow_trans']
        self.postingDelivToCustomer = json['financial_data']['posting_services']['marketplace_service_item_deliv_to_customer']
        self.postingReturnNotDelivToCustomer = json['financial_data']['posting_services']['marketplace_service_item_return_not_deliv_to_customer']
        self.postingReurnPartGoodToCustomer = json['financial_data']['posting_services']['marketplace_service_item_return_part_goods_customer']
        self.postingReturnAfterDeliv = json['financial_data']['posting_services']['marketplace_service_item_return_after_deliv_to_customer']
        self.additionalData = json['additional_data']



class PostingFBSListOrdersDeliveredModels:
    def __init__(self, json) -> None:
        self.orderId = json['order_id']  # ID заказа
        self.orderNumber = json['order_number']  # Номер заказа
        self.postingNumber = json['posting_number']  # Номер отправления
        self.status = json['status']  # Статус отправления
        self.deliveringDate = json['delivering_date']  # Дата доставки
        self.shipmentDate = json['shipment_date']  # Дата доставки
        self.inProcessAt = json['in_process_at']  # В обработке
        self.trackingNumber = json['tracking_number']  # Трек номер
        self.tplIntegrationType = json['tpl_integration_type']  # Тип интеграции
        self.tplProviderId = json['delivery_method']['tpl_provider_id']  # ID провайдера доставки
        self.providerName = json['delivery_method']['name']  # Наименование
        self.tplProvider = json['delivery_method']['tpl_provider']  # Провайдер
        self.deliveryMethodId = json['delivery_method']['id']  # Идентификатор
        self.warehouseId = json['delivery_method']['warehouse_id']  # ID склада
        self.warehouse = json['delivery_method']['warehouse']  # Склад
        self.cancelReasonId = json['cancellation']['cancel_reason_id']  # ID причины отмены
        self.cancellationInitiator = json['cancellation']['cancellation_initiator']  # Инициатор отмены
        self.cancellationType = json['cancellation']['cancellation_type']  # Тип отмены
        self.affectCancellationRating = json['cancellation']['affect_cancellation_rating']  # Влияние отмены на рейтинг
        self.cancelledAfterShip = json['cancellation']['cancelled_after_ship']  # Отменен после отправки
        self.cancelReason = json['cancellation']['cancel_reason']  # Причина отмены
        self.productsSku = json['products'][0]['sku']  # Идентификатор товара в системе Ozon
        self.productsName = json['products'][0]['name']  # Товар
        self.productsQuantity = json['products'][0]['quantity']  # Количество
        self.productsOfferId = json['products'][0]['offer_id']  # ID товара в системе продавца — артикул
        self.productsPrice = json['products'][0]['price']  # Цена
        self.productsMandatoryMark = json['products'][0]['mandatory_mark']  # Обязательная отметка
        self.analyticsDataRegion = json['analytics_data']['region']  # Регион
        self.analyticsDataCity = json['analytics_data']['city']  # Город
        self.analyticsDataDeliveryType = json['analytics_data']['delivery_type']  # Тип доставки
        self.analyticsDataIsPremium = json['analytics_data']['is_premium']  # Подписка Ozon Premium
        self.analyticsDataPaymentType = json['analytics_data']['payment_type_group_name']  # Способ оплаты
        self.analyticsDataWarehouseId = json['analytics_data']['warehouse_id']  # ID склада
        self.analyticsDataWarehouse = json['analytics_data']['warehouse']  # Наименование склада
        self.analyticsDataTplProviderId = json['analytics_data']['tpl_provider_id']  # ID провайдера
        self.analyticsDataTplProvider = json['analytics_data']['tpl_provider']  # Провайдер
        self.analyticsDataDeliveryDateBegin = json['analytics_data']['delivery_date_begin']  # Начало доставки
        self.analyticsDataDeliveryDateEnd = json['analytics_data']['delivery_date_end']  # Дата конца доставки
        self.analyticsDataIsLegal = json['analytics_data']['is_legal']  #
        self.financialDataProductId = json['financial_data']['products'][0]['product_id']  # Идентификатор товара
        self.financialDataCommissionPercent = json['financial_data']['products'][0]['commission_percent']  # Процент комиссии
        self.financialDataPayout = json['financial_data']['products'][0]['payout']  # Выплата
        self.financialDataTotalDiscountValue = json['financial_data']['products'][0]['total_discount_value']  # Общая стоимость скидки
        self.financialDataOldPrice = json['financial_data']['products'][0]['old_price']  # Прежняя цена
        self.financialDataActions = json['financial_data']['products'][0]['actions'][0]  # Акции
        self.financialDataTotalDiscountPercent = json['financial_data']['products'][0]['total_discount_percent']  # Общий процент скидки
        self.financialDataPicking = json['financial_data']['products'][0]['picking']  # Остаток
        self.financialDataCommissionAmount = json['financial_data']['products'][0]['commission_amount']  # Размер комиссии
        self.financialDataPickup = json['financial_data']['products'][0]['item_services']
        self.financialDataQuantity = json['financial_data']['products'][0]['quantity']  # Количество
        self.financialDataClientPrice = json['financial_data']['products'][0]['client_price']  # Цена клиента
        self.postingFulfillment = json['financial_data']['posting_services']['marketplace_service_item_fulfillment']
        self.postingPickup = json['financial_data']['posting_services']['marketplace_service_item_pickup']
        self.postingPvz = json['financial_data']['posting_services']['marketplace_service_item_dropoff_pvz']
        self.postingSc = json['financial_data']['posting_services']['marketplace_service_item_dropoff_sc']
        self.postingFf = json['financial_data']['posting_services']['marketplace_service_item_dropoff_ff']
        self.postingTrans = json['financial_data']['posting_services']['marketplace_service_item_direct_flow_trans']
        self.postingReturnTrans = json['financial_data']['posting_services']['marketplace_service_item_return_flow_trans']
        self.postingDelivToCustomer = json['financial_data']['posting_services']['marketplace_service_item_deliv_to_customer']
        self.postingReturnNotDelivToCustomer = json['financial_data']['posting_services']['marketplace_service_item_return_not_deliv_to_customer']
        self.postingReurnPartGoodToCustomer = json['financial_data']['posting_services']['marketplace_service_item_return_part_goods_customer']
        self.postingReturnAfterDeliv = json['financial_data']['posting_services']['marketplace_service_item_return_after_deliv_to_customer']
        self.customer = json['customer']                  # Клиент
        self.addressee = json['addressee']           # Получатель
        self.isExpress = json['is_express']
        self.requirementsCountry = json['requirements']['products_requiring_country']
        self.requirementsGtd = json['requirements']['products_requiring_gtd']


class FinanceTransactionListOrdersModels:
    def __init__(self, json) -> None:
        self.operationId = json['operation_id']  #  Идентификатор операции
        self.operationType = json['operation_type']  # Тип операции
        self.operationDate = json['operation_date']  # Дата операции
        self.operationTypeName = json['operation_type_name']  #  Название типа операции
        self.deliveryCharge = json['delivery_charge']  # Плата за доставку
        self.returnDeliveryCharge = json['return_delivery_charge']  # Стоимость обратной доставки
        self.accrualsForSale = json['accruals_for_sale']  # Начисления на продажу
        self.saleCommission = json['sale_commission']  # Комиссия за продажу
        self.amount = json['amount']  # Сумма
        self.type = json['type']  # Тип
        self.postingDeliverySchema = json['posting']['delivery_schema']  # Схема доставки
        self.postingPostingNumber = json['posting']['posting_number']  # Номер поставки
        self.postingOrderDate = json['posting']['order_date']  # Дата заказа
        self.postingWarehouseId = json['posting']['warehouse_id']  # Идентификатор склада
        self.itemsName = self._getFirstOrDefault(json['items'], 'name') #[0]['name']  # Наименование
        self.itemsSku = self._getFirstOrDefault(json['items'], 'sku') #[0]['sku']  #  Идентификатор товара в системе Ozon
        self.servicesDelivToCustomerName = self._getAdditionalParams(json['services'], 'name', 0) #[0]['name']  #  Название Сервисный сбор маркет плейса за доставку
        self.servicesDelivToCustomerPrice = self._getAdditionalParams(json['services'], 'price', 0) #[0]['price']  # Цена Сервисный сбор маркет плейса за доставку
        self.servicesDirectFlowLogisticName = self._getAdditionalParams(json['services'], 'name', 1) #[1]['name']  # Название Прямые расходы на доставку
        self.servicesDirectFlowLogisticPrice = self._getAdditionalParams(json['services'], 'price', 1) #[1]['price']  # Цена Прямые расходы на доставку

    # Две очень простые и очень мощные функции
    def _getFirstOrDefault(self, items, itemName):
        result = []
        for item in items:
            result.append(item[itemName])
        return result

    def _getAdditionalParams(self, services, itemName, index):
        return services[index][itemName] if len(services) > index else ''




class FinanceTotalsModels:
    def __init__(self, json) -> None:
        self.accrualsForSale = json['accruals_for_sale']
        self.saleCommission = json['sale_commission']
        self.processingAndDelivery = json['processing_and_delivery']
        self.refundsAndCancellations = json['refunds_and_cancellations']
        self.servicesAmount = json['services_amount']
        self.compensationAmount = json['compensation_amount']
        self.moneyTransfer = json['money_transfer']
        self.othersAmount = json['others_amount']









