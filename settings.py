import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_FILENAME = 'workbook.xlsx'
SPREADSHEET_NAME = 'Sheet1'
EMAIL_FROM = "@gmail.com"
EMAIL_TO = "qa@ontrackretail.co.uk"

# todo: create the password
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

# todo: understand the dictionaries. Here there is a tuple (a, b, c).
# todo: understand append / update the dictionary
PLANS = {
    # price/plan name : 0 price on page, 1 select duration, 2 click top, 3 click bottom
    '2018_basic_annual': ('PriceBasicAnnual', 'BillingYearly', 'PriceBasicTop', 'PriceBasicMonthlyBottom'),
    '2018_plus_annual': ('PricePlusAnnual', 'BillingYearly', 'PricePlusTop', 'PricePlusBottom'),
    '2018_starter': ('PriceStarter', 'BillingMonthly', 'PriceStarterTop', 'PriceStarterBottom'),
    '2018_basic_monthly': ('PriceBasicMonthly', 'BillingMonthly', 'PriceBasicTop', 'PriceBasicMonthlyBottom'),
    '2018_plus_monthly': ('PricePlusMonthly', 'BillingMonthly', 'PricePlusTop', 'PricePlusBottom'),
}

BROWSERS = {
    # Internet Explorer v11+
    "ie": {
        'browser': 'IE',
        'browser_version': '11.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '2048x1536'},
    # Firefox v51+
    "firefox": {
        'browser': 'Firefox',
        'browser_version': '62.0 beta',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '2048x1536'},
    # Chrome v50+
}
# todo: check the lists
MY_LIST = ['one', 'two', 3, 'four']