from openpyxl import Workbook
from extensions import df
import calendar

def get_sales_by_drink():
    sales_by_drink = df.groupby('Drink Name')['Sales Amount'].sum().sort_values(ascending=False)
    print('\nSales by Drink:')
    print(sales_by_drink)

    # Create a new workbook
    workbook = Workbook()

    # Select the active sheet
    sheet = workbook.active

    # Append the data
    sheet.append(['Drink Name', 'Drink Sales'])
    for drink_name, drink_sales in sales_by_drink.items():
        sheet.append([drink_name, drink_sales])

    # Save the workbook
    workbook.save(f'workbooks/aggregated/sales_by_drink_{calendar.month_name.lower()}.xlsx')

    # Close the workbook
    workbook.close()