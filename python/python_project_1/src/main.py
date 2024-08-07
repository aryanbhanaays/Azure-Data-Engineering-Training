"""
Program to Calculate the average cost of items sold
"""
import pandas as pd
def calculate_average_costs(items_file, sales_file, output_file):
    """
    Calculate the average cost of items sold within their valid date ranges
    
    Args:
    items_file (str): Path to the CSV file containing item data.
    sales_file (str): Path to the CSV file containing sales data.
    output_file (str): Path to the CSV file where the results will be saved.
    
    The items_file should have columns: ItemId, StartDate, EndDate, Price.
    The sales_file should have columns: SalesId, ItemId, NumSales, SalesDate.
    """
    items_df = pd.read_csv(items_file)
    sales_df = pd.read_csv(sales_file)

    merged_df = pd.merge(sales_df, items_df, on='ItemId')
    merged_df['SalesDate'] = pd.to_datetime(merged_df['SalesDate'])
    merged_df['StartDate'] = pd.to_datetime(merged_df['StartDate'])
    merged_df['EndDate'] = pd.to_datetime(merged_df['EndDate'])

    filtered_df = merged_df[(merged_df['SalesDate'] >= merged_df['StartDate']) & 
                            (merged_df['SalesDate'] <= merged_df['EndDate'])].copy()
    filtered_df.loc[:,'TotalSalesValue'] = filtered_df['NumSales'] * filtered_df['Price']  
     
    avg_cost_df = (filtered_df.groupby('ItemId')['TotalSalesValue'].sum() /
                   filtered_df.groupby('ItemId')['NumSales'].sum()).reset_index()
    avg_cost_df.columns = ['ItemId', 'AvgCost']
    avg_cost_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    calculate_average_costs('../files/Items.csv', '../files/Sales.csv', '../files/avg_costs.csv')
    print("Average cost calculation completed and saved to 'avg_costs.csv'.")
