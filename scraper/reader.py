from openpyxl import Workbook
from openpyxl import load_workbook

# Reads in case number from excel at filepath
def read(path_arg):
    wb = load_workbook(path_arg)
    ws = wb.active
    row = 1
    col = 1
    case_num_list = []
    for col in ws.values:
        for value in col:
            if not value:
                break
            case_num_list.append(value)
    print('Case numbers: ', case_num_list)
    return case_num_list

