from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='UserName']")
    password = (By.XPATH, "//input[@id='Password']")
    submit = (By.XPATH, "//button[@type='submit']")


class MainLocators(object):
    menu = (By.XPATH, "//button[contains(@class,'left-menu-toggle')]")

    # menu_close = (By.XPATH, "//button[@class='left-menu-toggle active']")

class MenuLocators(object):
    menu = (By.XPATH, "//button[contains(@class,'left-menu-toggle')]")
    eagle = (By.XPATH, "//*[@class='qa-header-icon-logo']")
    calculation = (By.XPATH,"//a[contains(.,'Расчеты')]")
    inner_calculation = (By.XPATH, "(//a[contains(.,'Расчеты')])[2]")
    statement_processing = (By.XPATH,"//a[contains(.,'Обработка выписки из л/с')]")
    unloading_informationSUFD = (By.XPATH,"//a[contains(.,'Выгрузка Сведений о бюджетном обязательстве (загрузка) в формате СУФД ФК (или Электронного бюджета)')]")
    unloading_information= (By.XPATH,"//a[contains(.,'Выгрузка Сведений о денежном обязательстве в Электронный бюджет')]")
    references = (By.XPATH, "//a[contains(.,'Справочники')]")
    report = (By.XPATH, "//a[contains(.,'Отчет')]")
    turnover_statement = (By.XPATH, "//a[contains(.,'Оборотная ведомость')]")
    summary_reporting = (By.XPATH, "//a[contains(.,'Сводная отчетность')]")
    printed_forms = (By.XPATH, "//a[contains(.,'Печатные формы')]")
    remainsNFA = (By.XPATH, "//a[contains(.,'Остатки НФА')]")
    salary = (By.XPATH,"//a[contains(.,'АИС «Зарплата.NET»')]")
    document_journal = (By.XPATH,"//a[contains(.,'Журнал документов')]")
    recycle_bin = (By.XPATH, "//a[contains(.,'Корзина документов ')]")


class CashExpenseRequestLocators(object):

    class DocumentHeader(object):
        document_number = (By.XPATH, "//input[@id='documentNumber']")
        document_date = (By.XPATH, "//input[@id='documentDate']")
        document_kind = (By.XPATH, "(//button[@title='Выбрать'])[1]")
        ofk_number = (By.XPATH, "//input[@id='ofkNumber']")
        entry_date = (By.XPATH, "//input[@id='EntryDate']")
        operation = (By.XPATH, "(//button[@title='Выбрать'])[2]")
        current_organization_account = (By.XPATH, "(//button[@title='Выбрать'])[3]")
        short = (By.XPATH, "//input[@id='short']")
        limit_date = (By.XPATH, "//input[@id='limitDate']")
        tracking_number = (By.XPATH, "//input[@id='trackingNumber']")
        federal_targeted_investment_program = (By.XPATH, "(//button[@title='Выбрать'])[4]")
        priority = (By.XPATH, "//input[@id='priority']")
        currency_amount = (By.XPATH, "//input[@id='currencyAmount']")
        currency_nds_amount = (By.XPATH, "//input[@id='currencyNdsAmount']")
        currency_classifier = (By.XPATH, "(//button[@title='Выбрать'])[5]")
        amount = (By.XPATH, "//input[@id='amount']")
        nds_amount = (By.XPATH, "//input[@id='ndsAmount']")
        amount_without_nds = (By.XPATH, "//input[@id='amountWithoutNds']")
        is_advance = (By.XPATH, "//input[@id='isAdvance']")
        payment_priority = (By.XPATH, "//input[@id='paymentPriority']")
        payment_form = (By.XPATH, "//select[@name='paymentForm']")
        payment_purpose = (By.XPATH, "//input[@id='paymentPurpose']")
        document_foundation = (By.XPATH, "(//button[@title='Выбрать'])[6]")
        document_foundation_kind = (By.XPATH, "(//button[@title='Выбрать'])[7]")
        document_foundation_number = (By.XPATH, "//input[@id='documentFoundationNumber']")
        document_foundation_date = (By.XPATH, "//input[@id='documentFoundationDate']")
        document_foundation_subject = (By.XPATH, "//input[@id='documentFoundationSubject']")
        counterparty = (By.XPATH, "(//button[@title='Выбрать'])[8]")
        counterparty_account_details = (By.XPATH, "(//button[@title='Выбрать'])[9]")
        is_employee = (By.XPATH, "//input[@id='isEmployee']")
        is_tax = (By.XPATH, "//input[@id='isTax']")
        chief = (By.XPATH, "(//button[@title='Выбрать'])[10]")
        chief_account = (By.XPATH, "(//button[@title='Выбрать'])[11]")

    class Requisites(object):

        document = (By.XPATH, "(//button[@title='Выбрать'])[12]")
        document_type = (By.XPATH, "(//button[@title='Выбрать'])[13]")
        document_number = (By.XPATH, "//input[@id='documentNumber']")
        document_date = (By.XPATH, "//input[@id='documentDate']")
        subject = (By.XPATH, "//input[@id='subject']")

    class Transcript(object):
        activity_kind = (By.XPATH, "//select[@name='activityKind']")
        kbk = (By.XPATH, "(//button[@title='Выбрать'])[12]")
        drawee_kbk_type = (By.XPATH, "//select[@name='draweeKbkType']")
        kosgu = (By.XPATH, "(//button[@title='Выбрать'])[13]")
        cost_element = (By.XPATH, "(//button[@title='Выбрать'])[14]")
        recepient_kbk = (By.XPATH, "(//button[@title='Выбрать'])[15]")
        recepient_kbk_type = (By.XPATH, "//select[@name='recepientKbkType']")
        goal_code = (By.XPATH, "(//button[@title='Выбрать'])[16]")
        department = (By.XPATH, "(//button[@title='Выбрать'])[17]")
        expenditure_goal_act = (By.XPATH, "(//button[@title='Выбрать'])[18]")
        document_foundation_counterparty = (By.XPATH, "(//button[@title='Выбрать'])[19]")
        foundation = (By.XPATH, "(//button[@title='Выбрать'])[20]")
        report_code = (By.XPATH, "(//button[@title='Выбрать'])[21]")
        operation = (By.XPATH, "(//button[@title='Выбрать'])[22]")
        currency_amount = (By.XPATH, "//input[@id='currencyAmount']")
        currency_nds_amount = (By.XPATH, "//input[@id='currencyNdsAmount']")
        amount = (By.XPATH, "//input[@id='amount']")
        nds_amount = (By.XPATH, "//input[@id='ndsAmount']")
        amount_without_nds = (By.XPATH, "//input[@id='amountWithoutNds']")
        nds_percent = (By.XPATH, "//input[@id='ndsPercent']")
        payment_purpose = (By.XPATH, "//input[@id='paymentPurpose']")
        comment = (By.XPATH, "//input[@id='comment']")
        drawee_subsidy_code = (By.XPATH, "//input[@id='draweeSubsidyCode']")
        recepient_subsidy_code = (By.XPATH, "//input[@id='recepientSubsidyCode']")
        act = (By.XPATH, "(//button[@title='Выбрать'])[23]")



class CashPullRequestLocators(object):

    filter = (By.XPATH, "//input[@placeholder='Все поля']")

    class HoldingRequest(object):
        lddate_prov = (By.XPATH, "//input[@id='lddate_prov']")
        typical_operation = (By.XPATH, "//button[@title='Выбрать']")
        submit = (By.XPATH, "//button[.='Провести']")

    class NewDocument(object):
        # Реквизиты документа
        account_number = (By.XPATH, "(//button[@title='Выбрать'])[1]")
        tracking_number = (By.XPATH, "//input[@id='TrackingNumber']")
        operation = (By.XPATH, "(//button[@title='Выбрать'])[2]")
        # Информация о документе
        document_number = (By.XPATH, "//input[@id='DocumentNumber']")
        document_date = (By.XPATH, "//input[@id='date1']")
        entry_date = (By.XPATH, "//input[@id='date2']")
        deadline = (By.XPATH, "//input[@id='date3']")
        # Дополнительно - Доверенность
        trustee = (By.XPATH, "(//button[@title='Выбрать'])[3]")
        trustee_name_dative_case = (By.XPATH, "//input[@id='TrusteeNameDativeCase']")
        trustee_position = (By.XPATH, "(//button[@title='Выбрать'])[4]")
        trustee_position_dative_case = (By.XPATH, "//input[@id='TrusteePositionDativeCase']")
        foundation = (By.XPATH, "//input[@id='Foundation']")
        # Дополнительно - Чек
        check_series = (By.XPATH, "//input[@id='CheckSeries']")
        check_number = (By.XPATH, "//input[@id='CheckNumber']")
        check_date = (By.XPATH, "//input[@id='CheckDate']")
        check_valid_till = (By.XPATH, "//input[@id='CheckValidTill']")
        # Дополнительно - Подписывающие лица
        manager = (By.XPATH, "(//button[@title='Выбрать'])[5]")
        chief_accountant = (By.XPATH, "(//button[@title='Выбрать'])[6]")

        class NewLine(object):
            kbk = (By.XPATH, "(//button[@title='Выбрать'])[7]")
            kbk_type = (By.XPATH, "//select[@name='kbkType']")
            kosgu = (By.XPATH, "(//button[@title='Выбрать'])[8]")
            costs_type = (By.XPATH, "(//button[@title='Выбрать'])[9]")
            operation = (By.XPATH, "(//button[@title='Выбрать'])[10]")
            funds_source = (By.XPATH, "//select[@name='fundsSource']")
            cash_transaction_code = (By.XPATH, "//select[@name='CashTransactionCode']")
            code_goal = (By.XPATH, "//input[@id='CodeGoal']")
            payment_purpose = (By.XPATH, "//input[@id='PaymentPurpose']")
            amount = (By.XPATH, "//input[@id='amount']")
            comment = (By.XPATH, "//input[@id='Comment']")


class ZNVLocators(object):
    document_number = (By.XPATH, "//*[@name='documentNumber']//input") ### //*[@name='documentNumber']//input
    document_date = (By.XPATH, "//*[@name='documentDate']//input") ### document_date = (By.XPATH, "//input[@id='date1']")
    personal_account = (By.XPATH, "//*[@name='accountDetails']")

    recipient_name = (By.XPATH, "(//button[@title='Выбрать'])[2]")
    ofk_registration_number = (By.XPATH, "//input[@id='ofkRegistrationNumber']")
    entry_date = (By.XPATH, "//input[@id='entryDate']")
    typical_operation = (By.XPATH, "(//button[@title='Выбрать'])[3]")
    recipient_account = (By.XPATH, "(//button[@title='Выбрать'])[4]")
    document_type = (By.XPATH, "(//button[@title='Выбрать'])[5]")

    class Request(object):
        # Закладка Расшифровка заявки
        summa_rub = (By.XPATH, "//input[@id='outstandingPaymentDocumentAmount']")
        kbk = (By.XPATH, "(//button[@title='Выбрать'])[6]")
        kosgu = (By.XPATH, "(//button[@title='Выбрать'])[7]")
        stavka_nds = (By.XPATH, "//input[@id='ndsPercent']")
        tip_kbk = (By.XPATH, "//select[@name='kbkType']")
        vid_zatrat = (By.XPATH, "(//button[@title='Выбрать'])[8]")
        summa_nds = (By.XPATH, "//input[@id='ndsAmount']")
        # Фрэйм Дополнительные реквизиты
        kod_cely = (By.XPATH, "//select[@name='goalCode']")
        oktmo = (By.XPATH, "(//button[@title='Выбрать'])[10]")

    class Doc(object):
        # Закладка Документы по зачислению невыясненного платежа
        number = (By.XPATH, "//input[@id='outstandingPaymentDocumentNumber']")

class PKOLocators(object):
    pass



class carryingOutOfDocumentsLocators(object):
    lddate_prov = (By.XPATH, "//*[@name='lddate_prov']//input")
    operation_master = (By.XPATH, "//*[@name='OperationMaster']")

class ContractWithSupplierLocators(object):
    documen_type = (By.XPATH, "//*[@name='documentKind']")
    number = (By.XPATH, "//*[@name='documentNumber']//input")
    date = (By.XPATH, "//*[@name='documentDate']//input")
    сounterparty = (By.XPATH, "//*[@name='counterparty']")
    bank_account_number= (By.XPATH, "//*[@name='transactionAccount']")
    uin = (By.XPATH, "//*[@name='chargeUniqueIdentifier']//input")
    currency = (By.XPATH, "//*[@name='currency']")
    date_begin = (By.XPATH, "//*[@name='startDate']//input")
    date_end = (By.XPATH, "//*[@name='endDate']//input")
    payment_type = (By.XPATH, "//*[@name='considerationPeriod']//select")
    subject_contract = (By.XPATH, "//*[@name='subject']//textarea")
    payment_terms = (By.XPATH, "//*[@name='paymentTerm']//textarea")
    note = (By.XPATH, "//*[@name='comment']//textarea")


class ContractWithSupplierDetailKBKPageLocators(object):
    financial_year = (By.XPATH, "//*[@name='financialYear']//input")
    entry_date = (By.XPATH, "//*[@name='entryDate']//input")
    operation = (By.XPATH, "//*[@name='operation']")
    kbk = (By.XPATH, "//*[@name='kbk']")
    kosgu = (By.XPATH, "//*[@name='kosgu']")
    contract_subject = (By.XPATH, "//*[@name='contractSubject']//textarea")
    amounts_amount = (By.XPATH, "//*[@name='amountsAmount']//input")
    amounts_nds_percent = (By.XPATH, "//*[@name='amountsNdsPercent']//input")
    advance = (By.XPATH, "//*[@name='advance']//input")
    cost_Element = (By.XPATH, "//*[@name='costElement']")


class CardIndexOSNMANPALocators(object):
    tag_no_first_part = (By.XPATH, "//*[@name='tagNoFirstPart']//input")
    tag_no_second_part = (By.XPATH, "//*[@name='tagNoSecondPart']//input")
    tag_no = (By.XPATH, "//*[@name='tagNo']//input")
    full_name = (By.XPATH, "//*[@name='fullName']//input")
    property_designation = (By.XPATH, "//*[@name='propertyDesignation']//input")
    start_up_date = (By.XPATH, "//*[@name='startUpDate']//input")
    serialNumber = (By.XPATH, "//*[@name='serialNumber']//input")
    group = (By.XPATH, "//li[contains(.,'С/блоки')]")
    unit_of_measure = (By.XPATH, "//*[@name='unitOfMeasure']")
    cost = (By.XPATH, "//*[@name='cost']//input")
    exclude_from_depreciation_accrual = (By.XPATH,"//*[@name='exludeFromDepreciationAccrual']//input")
    value_added_used = (By.XPATH, "//*[@name='valueAddedUsed']//input")
    amortization_group = (By.XPATH, "//*[@name='amortizationGroup']")
    okof = (By.XPATH, "//*[@name='okof']")

class ApplicationCashFlowLocators(object):
    documen_type = (By.XPATH, "//*[@name='documentKind']")
    number =  (By.XPATH, "//*[@name='documentNumber']//input")
    date = (By.XPATH, "//*[@name='documentDate']//input")
    personal_account = (By.XPATH, "//*[@name='accountDetails']")
    bank_account_number = (By.XPATH, "//*[@name='counterpartyAccountDetails']")
    recipient = (By.XPATH, "//*[@name='counterparty']")
    number_ufk = (By.XPATH, "//*[@name='ofkNumber']//input")
    limit_date = (By.XPATH, "//*[@name='limitDate']//input")
    foundation =(By.XPATH, "//div[@class='tab-content']//*[@name='foundation']")


class DecodingOfTheApplicationLocators(object):

    operation = (By.XPATH, "//div[@class='modal-content']//*[@name='operation']")
    kbk = (By.XPATH, "//div[@class='modal-content']//*[@name='kbk']")
    kosgu = (By.XPATH, "//*[@name='kosgu']")
    cost_element = (By.XPATH, "//*[@name='costElement']")
    amount = (By.XPATH, "//div[@class='modal-content']//*[@name='amount']//input")
    nds_percent = (By.XPATH, "//*[@name='ndsPercent']//input")
    document_foundation_counterparty = (By.XPATH, "//*[@name='documentFoundationCounterparty']")
    foundation = (By.XPATH, "//div[@class='modal-content']//*[@name='foundation']")
    comment = (By.XPATH, "//*[@name='comment']//textarea")

