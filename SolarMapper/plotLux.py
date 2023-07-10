import openpyxl
import matplotlib.pyplot as plt

def get_values(file_path, mnR, mxR, c):
    # Open the workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select the sheet you want to extract data from
    worksheet = workbook['Data']  # replace 'Sheet1' with the name of your sheet

    # Extract data from column D, rows 2-11833
    data = []
    for row in worksheet.iter_rows(min_row=mnR, max_row=mxR, min_col=c, max_col=c):
        for cell in row:
            data.append(cell.value)

    return data


lux = []
lux = get_values("luxReal.xlsx", 2, 11833, 4)

dates = get_values("luxReal.xlsx", 2, 11833, 2)
for date in dates:
     print(date.datetime)
# print(tmp)