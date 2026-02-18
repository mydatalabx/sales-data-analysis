# Sales Data Analysis

## Description
This project analyzes sales data from a CSV spreadsheet using Python.  
It calculates total sales, monthly averages, identifies the highest and lowest sales months, computes monthly percentage changes, and visualizes the results using Seaborn and Matplotlib.

## Files
- `sales.csv` — the raw sales data
- `main.py` — Python script for analysis and visualization
- `README.md` — this file

## How to Use
1. Install the required Python packages if you don’t already have them:
    ```bash
    pip install pandas seaborn matplotlib
    ```
2. Ensure `sales.csv` and `main.py` are in the same folder.
3. Run the Python script:
    ```bash
    main.py
    ```
4. The script will:
    - Print summary statistics (total sales, average, highest and lowest months)
    - Print monthly percentage changes
    - Display three visualizations:
        1. Line chart showing monthly sales trend
        2. Bar chart comparing monthly sales
        3. Heatmap of monthly percentage changes

## Notes
- The `sales.csv` file should have two columns: `month` and `sales`.
- Visualizations are created using **Seaborn** and **Matplotlib**.
- Designed for **Python 3**.
