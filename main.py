import csv

def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    data = read_data()

    sales = []
    months = []

    # Collect sales and months
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
        month = row['month']
        months.append(month)

    # Basic calculations
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    max_sales = max(sales)
    min_sales = min(sales)
    max_sales_month = months[sales.index(max_sales)]
    min_sales_month = months[sales.index(min_sales)]

    # Monthly percentage changes
    monthly_changes = []
    for i in range(1, len(sales)):
        change = ((sales[i] - sales[i - 1]) / sales[i - 1]) * 100
        monthly_changes.append({'month': months[i], 'change': change})

    # Print monthly % changes
    print("\nMonthly Percentage Changes:")
    for month_data in monthly_changes:
        print(f"{month_data['month']}: {month_data['change']:.2f}%")

    # Print summary results
    print("\n--- Sales Summary ---")
    print(f"Total sales: {total_sales}")
    print(f"Average sales for the year: {average_sales:.2f}")
    print(f"Highest sales: {max_sales} ({max_sales_month})")
    print(f"Lowest sales: {min_sales} ({min_sales_month})")

run()
