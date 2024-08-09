# Average Cost Calculator

## Overview

The **Average Cost Calculator** is a Python project designed to calculate the average cost of items sold based on data from two CSV files: one containing item details and another containing sales data. This project uses Python and Poetry for dependency management and optimization.

## Features

- **Calculate Average Cost**: Computes the average cost of items sold within their valid date ranges.
- **Directory Management**: Creates necessary directory structures using Python.
- **Poetry Integration**: Manages dependencies using Poetry for consistency and reproducibility.

## Installation

### Using Poetry

1. **Install Poetry** (if not already installed):
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the Repository**:
   ```sh
   git clone https://github.com/aryanbhanaays/Azure-Data-Engineering-Training.git
   cd .\python\python_project_poetry
   ```

3. **Install Dependencies**:
   ```sh
   poetry install
   ```

## Usage

1. **Prepare Your Data**:
   - Ensure you have two CSV files:
     - `Items.csv`: Contains columns `ItemId`, `StartDate`, `EndDate`, `Price`.
     - `Sales.csv`: Contains columns `SalesId`, `ItemId`, `NumSales`, `SalesDate`.

2. **Update the Script**:
   - Modify the paths in `main.py` to point to your CSV files.

3. **Run the Script**:
   ```sh
   poetry run python average_cost_calculator/main.py
   ```

   This will read the data from the CSV files, calculate the average cost of items sold, and save the results to `avg_costs.csv`.

## Directory Structure

The following directory structure will be created:

Specifiy your path in the base path

```
C:/
└── Users/
    └── AryanBhan/
        └── OneDrive - AAYS ADVISORY PRIVATE LIMITED/
            └── Desktop/
                └── Company Work/
                    └── training/
                        └── Azure-Data-Engineering-Training/
                            └── python/
                                └── python_project_poetry/
                                    └── files/
```

## Git Ignore

The following directories are ignored in the Git repository to avoid committing unnecessary files:

- `__pycache__/`
- `env/`
- `.pytest_cache/`

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [aryanbhan@aaysinsight.com](mailto:your-email@example.com).
```

### To Use:
1. **Save** the content as `README.md` in your project directory.
2. **Update placeholders** such as `https://github.com/aryanbhanaays/Azure-Data-Engineering-Training.git`, `python\python_project_poetry`, and contact email.

This single `README.md` file provides a comprehensive overview of the project, installation instructions, usage details, and other relevant information.