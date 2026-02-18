import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

    # Convert to DataFrame for Seaborn
    df = pd.DataFrame({'Month': months, 'Sales': sales})

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

    # ---------------- Seaborn Visualizations ---------------- #
    sns.set(style="whitegrid")

    # Line plot
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='Month', y='Sales', marker='o')
    plt.title("Monthly Sales Trend")
    plt.ylabel("Sales")
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=False)  # <- non-blocking

    # Bar plot
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x='Month', y='Sales', palette='viridis')
    plt.title("Monthly Sales Comparison")
    plt.ylabel("Sales")
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=False)  # <- non-blocking

    # Heatmap
    change_df = pd.DataFrame(monthly_changes)
    change_df.set_index('month', inplace=True)

    plt.figure(figsize=(10, 2))
    sns.heatmap(change_df.T, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Percentage Change'})
    plt.title("Monthly Percentage Change Heatmap")
    plt.ylabel("")
    plt.xlabel("Month")
    plt.tight_layout()
    plt.show()  # keep last one blocking to prevent script from closing immediately

run()
