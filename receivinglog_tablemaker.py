# Main Program: 
# Create Receiving Daily Logs for Seajet

from datetime import datetime, date, timedelta
import calendar
import xlsxwriter

###########################################################
# 						 METHODS                          #
###########################################################
# add_rows method
# Method to insert the row numbers to the tables
def add_rows(start_row, col, row_size, col_size):
	row = start_row

	# Add the record formatting to each row and column
	for i in range(row_size):
		for j in range(col_size):
			worksheet.write(row + i, col + j, ' ', record_formats)

	# Add the row numbers to each row
	for i in range(row_size):
		worksheet.write(row + i, col, i+1, record_formats)


# add_headers method
# Method to insert the headers to table tables
def add_headers(row, start_col):
	col = start_col
	for i in range(6):
		if i == 0:
			worksheet.write(row, col + i, '#', header_formats)
		elif i == 1:
			worksheet.write(row, col + i, 'CONTAINER #', header_formats)
		elif i == 2:
			worksheet.write(row, col + i, 'LOT #', header_formats)
		elif i == 3:
			worksheet.write(row, col + i, 'QTY', header_formats)
		elif i == 4:
			worksheet.write(row, col + i, 'STYLE NAME', header_formats)
		elif i == 5:
			worksheet.write(row, col + i, 'BIN', header_formats)

# clear_row method
# Method to clear the formatting of the specified row, for i columns
def clear_row(row, start_col, size):
	col = start_col
	for i in range(size):
		worksheet.write(row, col + i, ' ', clear_row_formats)

# clear_col method
# Method to clear the formatting of the specified column, for i rows
def clear_col(start_row, col, size):
	row = start_row
	for i in range(size):
		worksheet.write(row + i, col, ' ', clear_col_formats)

###########################################################
# 	 CHANGE WORKBOOK MONTH AND START AND END DATES        #
###########################################################

# Loop to create a Receiving Log for Every Day of Selected Month
year = 2022

# CHANGE START AND END DATES AS NEEDED
start = date(year, 12, 1) # Start Date 
end = date(year, 1, 1) # End Date

# Create a Workbook for the Month
workbook = xlsxwriter.Workbook("DECEMBER_RECEIVING_DAILY_LOG.xlsx") # CHANGE MONTH AS NEEDED


###########################################################
# 	           DONT TOUCH THE CODE BELOW                  #
###########################################################
delta = end - start
for offset in range(delta.days):
	day = start + timedelta(offset)
	day_format_underscore = day.strftime('%m_%d_%y') # Date in Format: MM_DD_YY
	day_format_slash = day.strftime('%m/%d/%y') # Date in Format: MM/DD/YY
	date = datetime.strptime(day_format_underscore, '%m_%d_%y').weekday() # Get the weekday
	weekday = calendar.day_name[date] # Get the weekday from the date

	# Create a Sheet for every day of the month except Sundays
	if weekday != "Sunday":
		msi_table_title = 'MSI ' + day_format_slash
		msir_table_title = 'MSIR ' + day_format_slash
		b3_table_title = 'MSI Building #3 ' + day_format_slash
		td_table_title = 'Transfer & Delivery ' + day_format_slash

		# Sheet Declaration
		worksheet = workbook.add_worksheet(day_format_underscore) 

		# FORMATS
		# Add the Title Formats to Title Cells
		title_formats = workbook.add_format(
			{
				'bold' : True,
				'bg_color' : '#FFFF00',
				'font_size' : 18,
				'align' : 'center',
				'valign' : 'vcenter',
				'font_name' : 'Calibri',
				'border' : 1
			}
		)

		# Add the Header Formats to Header Cells
		header_formats = workbook.add_format(
			{
				'bold' : True,
				'bg_color' : '#FFFF00',
				'font_size' : 15,
				'align' : 'center',
				'valign' : 'vcenter',
				'font_name' : 'Calibri',
				'border' : 1
			}
		)

		# Add the Record Formats to Record Cells
		record_formats = workbook.add_format(
			{
				'font_size' : 12,
				'align' : 'center',
				'valign' : 'vcenter',
				'font_name' : 'Calibri',
				'border' : 1
			}
		)

		# Formats to Clear Row and Columns 
		clear_row_formats = workbook.add_format(
			{
				'left' : 0,
				'right' : 0
			}
		)

		clear_col_formats = workbook.add_format(
			{
				'top' : 0,
				'bottom' : 0
			}
		)

		# CODE TO SET THE COLUMN WIDTHS FOR THE FOUR TABLES
		# Set the column widths for the headers for MSI and MSIR Tables
		worksheet.set_column(0, 0, 5) # Adjust the NUMBER column width
		worksheet.set_column(1, 1, 20) # Adjust the CONTAINER # column width
		worksheet.set_column(2, 2, 12) # Adjust the LOT # column width
		worksheet.set_column(3, 3, 5) # Adjust the QTY column width
		worksheet.set_column(4, 4, 40) # Adjust the STYLE NAME column width
		worksheet.set_column(5, 5, 8) # Adjust the BIN column width

		# Set the column widths for Transfer & Delivery and Building 3 Tables
		worksheet.set_column(9, 9, 5) # Adjust the NUMBER column width
		worksheet.set_column(10, 10, 20) # Adjust the CONTAINER # column width
		worksheet.set_column(11, 11, 12) # Adjust the LOT # column width
		worksheet.set_column(12, 12, 5) # Adjust the QTY column width
		worksheet.set_column(13, 13, 40) # Adjust the STYLE NAME column width
		worksheet.set_column(14, 14, 8) # Adjust the BIN column width

		# Create the MSI Table
		worksheet.merge_range(0, 0, 0, 5, msi_table_title, title_formats)
		add_headers(1, 0) 
		add_rows(2, 0, 30, 6) 

		# Create the Building #3 Table
		worksheet.merge_range(32, 0, 32, 5, b3_table_title, title_formats)
		add_headers(33, 0) 
		add_rows(34, 0, 30, 6) 

		# Create the MSIR Table
		worksheet.merge_range(0, 9, 0, 14, msir_table_title, title_formats)
		add_headers(1, 9)
		add_rows(2, 9, 30, 6)

		# Create the Transfer & Delivery Table
		worksheet.merge_range(32, 9, 32, 14, td_table_title, title_formats)
		add_headers(33, 9)
		add_rows(34, 9, 30, 6)


# Close the Workbook
workbook.close()