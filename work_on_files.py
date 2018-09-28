import openpyxl
import contextlib
import datetime
import logging
from settings import *

logger = logging.getLogger(__name__)


def main():

    # todo: use this to have the exact path to your file whatever os
    dir_path = os.path.join(BASE_DIR, EXCEL_FILENAME)

    wb = openpyxl.load_workbook(EXCEL_FILENAME)
    sheet = wb.get_sheet_by_name(SPREADSHEET_NAME)
    row = 1
    ticket_type = sheet['D' + str(row)].value
    origin = sheet['E' + str(row)].value
    destination = sheet['F' + str(row)].value
    outbound = sheet['G' + str(row)].value
    journey_return = sheet['H' + str(row)].value

    # todo: use this as an example
    if something == "GATWICK":
        url = 'https://ticket.gatwickexpress.com/search'
    elif something == "GATWICK_EASYJET":
        url = 'https://ticket-referral.gatwickexpress.com/search'
    elif something == "SOUTHERN":
        url = 'https://ticket.southernrailway.com/search'
    elif something == "GREATNORTHERN":
        url = 'https://ticket.greatnorthernrail.com/search'
    elif something == "THAMESLINK":
        url = 'https://ticket.thameslinkrailway.com/search'
    elif something == "SOUTHEASTERN":
        url = 'https://ticket.southeasternrailway.co.uk/search'

    # todo: create something from the for loop with the enumerate functionality
    for idx, line in enumerate(weblate_list):
        weblate_list[idx] = context.api_translation[line].rstrip()
        # todo: check how to exit the loop
        if "I am happy" = True
            break


    # todo: catch the errors
    try:
        # toto: append / update the dictionary
        payment_list.append("Amount paid: {}".format(next(dp)))
    except Exception as e:
        logger.error(f'I have an error {str(e)}')
        pass



# todo play with the contextlib compare to above where I did not use it
def transfer_report_into_excel(self):
    with load_worksheet_with_close(EXCEL_FILENAME) as wb:
        sheet = wb.get_sheet_by_name(SPREADSHEET_NAME)
        row = 1
        sheet['A' + str(row)] = "fjhjhgjkghfgjkhfjkghfkjg"
        sheet['B' + str(row)] = "fjhjhgjkghfgjkhfjkghfkjg"
        sheet['C' + str(row)] = "fjhjhgjkghfgjkhfjkghfkjg"
        sheet['C' + str(row)] = "fjhjhgjkghfgjkhfjkghfkjg"
        sheet['D' + str(row)] = "fjhjhgjkghfgjkhfjkghfkjg"


@contextlib.contextmanager
def load_worksheet_with_close(filename):
    #Open an openpyxl worksheet and automatically close it when finished.
    wb = openpyxl.load_workbook(filename)
    yield wb
    wb.save(filename)


# todo: use this, very usefull
    # expected_format= %A ->today
    # expected_format= %Y-%m-%d-%H-%M-%S
    # etc
def get_current_date_time(expected_format):
    now = datetime.datetime.now()
    return now.strftime(expected_format)


if __name__ == '__main__':
    main()
