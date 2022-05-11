# Example 1: Turn a tuple of information to a table
import xlsxwriter

# Create a workbook (excel file) and a worksheet (excel sheet)
workbook = xlsxwriter.Workbook("example1.xlsx")
worksheet = workbook.add_worksheet()

# Tuple of Afternoon Meals
afternoon_meal_plan = (['Monday', 'Chicken & Brocolli'],['Tuesday', 'Fried Salmon'],
	['Wednesday', 'Chicken & Brocolli'],['Thursday', 'Shrimp, Peas, & Rice'],
	['Friday', 'Protein Egg and Quinoa'], ['Saturday', 'Chicken & Brocolli'],
	['Sunday', 'Bacon Pizza'])

# Set column widths
worksheet.set_column(0, 0, 10) # Column A set to 10 characters wide
worksheet.set_column(1, 1, 20) # Column b set to 20 characters wide

# Table Column Formats
col_format = workbook.add_format(
	{'bold' : True, 'bg_color' : 'yellow', 'font_size' : 15, 'align' : 'center', 'border' : 1})

# Table Row Formats
row_format = workbook.add_format(
	{'bg_color' : '#d3d3d3', 'font_size' : 12, 'align' : 'center', 'border' : 1})

# Add Headers to table
worksheet.write(0, 0, "Day", col_format) # Column A - 0,0
worksheet.write(0, 1, "Meal", col_format)# Column B - 1,1

# Add the information to the table row by row
row = 1
col = 0
for day, meal in (afternoon_meal_plan):
	worksheet.write(row, col, day, row_format)
	worksheet.write(row, col + 1, meal, row_format)
	row += 1

# Close the workbook
workbook.close()