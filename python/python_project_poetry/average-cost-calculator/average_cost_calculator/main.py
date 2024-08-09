import pandas as pd
import os

def calculate_average_costs(items_file, sales_file, output_file):
    items_df = pd.read_csv(items_file)
    sales_df = pd.read_csv(sales_file)

    merged_df = pd.merge(sales_df, items_df, on='ItemId')
    merged_df['SalesDate'] = pd.to_datetime(merged_df['SalesDate'])
    merged_df['StartDate'] = pd.to_datetime(merged_df['StartDate'])
    merged_df['EndDate'] = pd.to_datetime(merged_df['EndDate'])

    filtered_df = merged_df[(merged_df['SalesDate'] >= merged_df['StartDate']) & 
                            (merged_df['SalesDate'] <= merged_df['EndDate'])].copy()
    filtered_df.loc[:, 'TotalSalesValue'] = filtered_df['NumSales'] * filtered_df['Price']  
    avg_cost_df = (filtered_df.groupby('ItemId')['TotalSalesValue'].sum() /
                   filtered_df.groupby('ItemId')['NumSales'].sum()).reset_index()
    avg_cost_df.columns = ['ItemId', 'AvgCost']
    avg_cost_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    base_path = 'C:/Users/AryanBhan/OneDrive - AAYS ADVISORY PRIVATE LIMITED/Desktop/Company Work/training/Azure-Data-Engineering-Training/python/python_project_poetry/average-cost-calculator/files'
    items_file = os.path.join(base_path, 'Items.csv')
    sales_file = os.path.join(base_path, 'Sales.csv')
    output_file = os.path.join(base_path, 'avg_costs.csv')
    calculate_average_costs(items_file, sales_file, output_file)
    print("Average cost calculation completed and saved to 'files/avg_costs.csv'.")
