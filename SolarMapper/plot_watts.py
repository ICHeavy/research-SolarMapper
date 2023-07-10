import openpyxl
import matplotlib.pyplot as plt

def get_values(file_path):
    # Load the Excel file
    wb = openpyxl.load_workbook(file_path)
    
    # Get the sheet with the data
    sheet = wb['Sheet1']
    
    # Define the ranges of cells
    ranges = [('D', 4, 32), ('F', 4, 44), ('H', 4, 56)]
    
    # Extract the values from the ranges and store them in a dictionary
    data_dict = {}
    for lumens, col, start_row, end_row in zip([1050, 3003, 10000], ['D', 'F', 'H'], [4, 4, 4], [32, 44, 56]):
        current = []
        voltage = []
        wattage = []
        IR = []
        for row in range(start_row, end_row + 1):
            Itmp = sheet[col + str(row)].value
            current.append(Itmp)
            Vtmp = sheet[chr(ord(col) + 1) + str(row)].value
            voltage.append(Vtmp)
            Wtmp = Itmp * Vtmp
            IRtmp = Vtmp / Itmp
            wattage.append(Wtmp)
            IR.append(IRtmp)
        data_dict[lumens] = {'current': current, 'voltage': voltage, 'Power':wattage, 'Internal Resistance':IR}
    
    return data_dict

def plot_voltage_current(data_dict):
    plt.figure()
    for lumens, sub_dict in data_dict.items():
        plt.plot(sub_dict['voltage'], sub_dict['current'], label='Lumens: {}'.format(lumens))
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (-mA)')
    plt.title('Voltage x Current')
    plt.legend()
    plt.grid()
    plt.show()


def plot_voltage_power(data_dict):
    plt.figure()
    for lumens, sub_dict in data_dict.items():
        plt.plot(sub_dict['voltage'], sub_dict['Power'], label='Lumens: {}'.format(lumens))
    plt.xlabel('Voltage (V)')
    plt.ylabel('Power (mW)')
    plt.title('Voltage x Power')
    plt.legend()
    plt.grid(axis='y')
    plt.show()

def plot_voltage_IR(data_dict):
    plt.figure()
    for lumens, sub_dict in data_dict.items():
        plt.plot(sub_dict['voltage'], sub_dict['Internal Resistance'], label='Lumens: {}'.format(lumens))
    plt.xlabel('Voltage (V)')
    plt.ylabel('Internal Resistance (Ohm)')
    plt.title('Voltage x Internal Resistance')
    plt.legend()
    plt.grid(axis='y')
    plt.show()

def plot_power_IR(data_dict):
    plt.figure()
    for lumens, sub_dict in data_dict.items():
        plt.plot(sub_dict['Power'], sub_dict['Internal Resistance'], label='Lumens: {}'.format(lumens))
    plt.xlabel('Power (W)')
    plt.ylabel('Internal Resistance (Ohm)')
    plt.title('Power x Internal Resistance')
    plt.legend()
    plt.grid(axis='y')
    plt.show()

# Example usage
file_path = 'LuxTst.xlsx'
data_dict = get_values(file_path)

plot_voltage_current(data_dict)
plot_voltage_power(data_dict)
for lumens, sub_dict in data_dict.items():
    ir_list = sub_dict['Internal Resistance']
    print('Lumens: {}, IR: {}'.format(lumens, ir_list))
