#! python3

import openpyxl
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p %Z')

user_input = input('(a)ll (o)ff_the_clock or (q)uit:')
if user_input == 'q':
    exit()


if user_input == 'o':
    logging.debug("Generating Off the clock alarms")
else:
    logging.debug("Generating for all alarms")

wb = openpyxl.load_workbook("alarms.xlsx")
sheet = wb.active

output_file = open('output.txt', 'w')


for row in range(1, sheet.max_row + 1):
    off_the_clock_list = []
    for col in range(1, sheet.max_column + 1):
        if sheet.cell(row=row, column=col).value == None:
            break

        if user_input == 'a':
            if col == 1:
                output_file.write(f'Truck: {sheet.cell(row=row, column=col).value}\n')
            if col == 2:
                output_file.write(f'Alarm Type: {sheet.cell(row=row, column=col).value}\n')
            if col == 3:
                output_file.write(f'Alarm Time: {sheet.cell(row=row, column=col).value}\n')
            if col == 4:
                output_file.write(f'Speed: {sheet.cell(row=row, column=col).value}\n')
            if col == 5:
                output_file.write(f'Location: {sheet.cell(row=row, column=col).value}\n')

        if user_input == 'o':
            if sheet.cell(row=row, column=2).value == 'Off the clock':
                
                if float(sheet.cell(row=row, column=4).value) < 10:
                    break

                if col == 1:
                    output_file.write(f'Truck: {sheet.cell(row=row, column=col).value}\n')
                if col == 2:
                    output_file.write(f'Alarm Type: {sheet.cell(row=row, column=col).value}\n')
                if col == 3:
                    output_file.write(f'Alarm Time: {sheet.cell(row=row, column=col).value}\n')
                if col == 4:
                    output_file.write(f'Speed: {sheet.cell(row=row, column=col).value}\n')
                if col == 5:
                    output_file.write(f'Location: {sheet.cell(row=row, column=col).value}\n')

    output_file.write('\n\n')

        

output_file.close()
logging.debug("Check the output file")


    