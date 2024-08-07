# Average Cost Calculation

This Python project reads two CSV files containing item and sales data, merges them based on item IDs, and calculates the average cost of items sold within their valid date ranges. The results are then saved to a new CSV file.

## Project Structure

- `items.csv`: CSV file containing item data with columns:
  - `ItemId`: ID of the item
  - `StartDate`: Start date of the item's validity period
  - `EndDate`: End date of the item's validity period
  - `Price`: Price of the item during the validity period

- `sales.csv`: CSV file containing sales data with columns:
  - `SalesId`: ID of the sale
  - `ItemId`: Foreign key reference to the item
  - `NumSales`: Number of units sold
  - `SalesDate`: Date of the sale

- `avg_costs.csv`: Output CSV file containing the average cost of items with columns:
  - `ItemId`: ID of the item
  - `AvgCost`: Average cost for that item

- `main.py`: Python script that reads the input CSV files, performs the necessary calculations, and writes the results to the output CSV file.

- `requirements.txt`: File listing the required Python libraries.

## Requirements

- Python
- pandas

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aryanbhanaays/Azure-Data-Engineering-Training/tree/main
    cd python/python-project_1
    ```

2. Install the required libraries using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your `items.csv` and `sales.csv` files in the project directory.

2. Run the script:
    ```bash
    python main.py
    ```

3. The output file `avg_costs.csv` will be generated in the project directory, containing the average cost calculations.

## Example

### items.csv
| ItemId | StartDate  | EndDate    | Price |
|--------|------------|------------|-------|
| 1      | 2023-01-01 | 2023-01-31 | 100   |
| 2      | 2023-02-01 | 2023-02-28 | 200   |

### sales.csv
| SalesId | ItemId | NumSales | SalesDate  |
|---------|--------|----------|------------|
| 101     | 1      | 10       | 2023-01-15 |
| 102     | 2      | 5        | 2023-02-10 |

### avg_costs.csv
| ItemId | AvgCost |
|--------|---------|
| 1      | 100.0   |
| 2      | 200.0   |

## Function Details

### `calculate_average_costs(items_file, sales_file, output_file)`

Calculates the average cost of items sold within their valid date ranges and saves the results to a CSV file.

#### Arguments
- `items_file` (str): Path to the CSV file containing item data.
- `sales_file` (str): Path to the CSV file containing sales data.
- `output_file` (str): Path to the CSV file where the results will be saved.

#### Example
```python
calculate_average_costs('items.csv', 'sales.csv', 'avg_costs.csv')
