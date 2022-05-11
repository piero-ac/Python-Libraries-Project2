# Example 2: Create a Column Chart from a List of Lists of Information
import xlsxwriter

# # Create a workbook (excel file) and a worksheet (excel sheet)
workbook = xlsxwriter.Workbook("example2.xlsx")
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Year', 'Q4 Earnings']
data = [
    ["2018", "2019", "2020", "2021"],
	[15_363, 14_801, 15_196, 16_937]
]

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])

# Create a new column chart.
chart1 = workbook.add_chart({'type': 'column'})

# Configure the series.
chart1.add_series({'name': '=Sheet1!$B$1','categories': '=Sheet1!$A$2:$A$5',
    'values': '=Sheet1!$B$2:$B$5'})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Comparison of Q4 Earnings'})
chart1.set_x_axis({'name': 'Fiscal Year'})
chart1.set_y_axis({'name': 'Earnings (in millions)'})

# Set an Excel chart style.
chart1.set_style(10)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

workbook.close()