import openpyxl

def get_values(file_path):
    # Load the Excel file
    wb = openpyxl.load_workbook(file_path)
    
    # Get the sheet with the data
    sheet = wb['Sheet1']
    
    # Define the ranges of cells to extract the data from
    lumens = [1050, 3003, 10.05]
    columns = ['D', 'F', 'H']
    voltage_columns = ['E', 'G', 'I']
    start_rows = [4, 4, 4]
    end_rows = [32, 44, 56]
    
    # Loop through the data ranges and extract the values
    data = {}
    for i in range(len(lumens)):
        lumen = lumens[i]
        column = columns[i]
        voltage_column = voltage_columns[i]
        start_row = start_rows[i]
        end_row = end_rows[i]
        
        currents = []
        voltages = []
        for row in range(start_row, end_row + 1):
            current = sheet[column + str(row)].value
            voltage = sheet[voltage_column + str(row)].value
            if current is not None and voltage is not None:
                currents.append(current)
                voltages.append(voltage)
        
        data[str(lumen) + ' lumens'] = {
            'currents': currents,
            'voltages': voltages
        }
    
    return data


data = get_values('LuxTst.xlsx')
print(data)
