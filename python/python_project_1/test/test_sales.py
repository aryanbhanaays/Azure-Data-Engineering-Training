"""
Test suite for calculate_average_costs function
"""

import pandas as pd
import pytest
from src.main import calculate_average_costs

@pytest.fixture
def setup_test_data(tmp_path):
    """
    Fixture to set up temporary CSV files for testing.

    Args:
        tmp_path (pathlib.Path): Temporary directory provided by pytest.

    Returns:
        tuple: Paths to items, sales, and output CSV files.
    """
    # Create CSV content for items and sales
    items_csv = """ItemId,StartDate,EndDate,Price
1,2022-01-01,2022-12-31,10
2,2022-01-01,2022-12-31,20
3,2022-06-01,2022-12-31,30
"""
    sales_csv = """SalesId,ItemId,NumSales,SalesDate
1,1,10,2022-01-15
2,2,5,2022-07-15
3,3,2,2022-06-15
4,3,3,2023-01-01
"""
    # Write the content to temporary CSV files
    items_file = tmp_path / "Items.csv"
    sales_file = tmp_path / "Sales.csv"
    output_file = tmp_path / "avg_costs.csv"

    items_file.write_text(items_csv)
    sales_file.write_text(sales_csv)

    return str(items_file), str(sales_file), str(output_file)

def test_calculate_average_costs(setup_test_data):
    """
    Test the calculate_average_costs function with sample data.

    Args:
        setup_test_data (tuple): Tuple containing paths to items, sales, and output CSV files.
    """
    # Get file paths from fixture
    items_file, sales_file, output_file = setup_test_data

    # Call the function to calculate average costs
    calculate_average_costs(items_file, sales_file, output_file)

    # Read the output CSV file
    avg_cost_df = pd.read_csv(output_file)

    # Expected output data
    expected_data = {
        'ItemId': [1, 2, 3],
        'AvgCost': [10.0, 20.0, 30.0]
    }
    expected_df = pd.DataFrame(expected_data)

    # Assert that the dataframes are equal
    assert avg_cost_df.equals(expected_df)