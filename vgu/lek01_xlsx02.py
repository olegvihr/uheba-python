import xlsxwriter

workbook = xlsxwriter.Workbook('диаграммы.xlsx')
worksheet = workbook.add_worksheet()

# Данные
data = [10, 40, 50, 20, 10, 50, 20]
worksheet.write_column('A1', data)

# Тип диаграммы
chart = workbook.add_chart({'type': 'line'})
# chart = workbook.add_chart({'type': 'pie'})

# Строим по нашим данным
chart.add_series({'values': '=Sheet1!A1:A7'})

worksheet.insert_chart('C1', chart)
workbook.close()