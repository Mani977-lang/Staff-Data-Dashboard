## Staff Data Dashboard

A Python-based employee data analysis dashboard that uses **Pandas** for data manipulation and **Matplotlib/Seaborn** for visualization.

### Features

- 📊 Employee data analysis
- 📈 Salary statistics by department and job title
- 👥 Employee distribution visualization
- ⭐ Performance rating analysis
- 🔗 Correlation analysis between salary and experience
- 📉 Multiple chart types (bar, pie, histogram, scatter, heatmap)
- 💾 Export data to CSV and Excel formats

### Project Structure

```
Staff-Data-Dashboard/
├── data/
│   ├── __init__.py
│   ├── sample_data.py          # Sample data generator
│   └── output/                 # Generated data files (CSV, Excel)
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Data loading functions
│   ├── analysis.py             # Analysis functions
│   └── visualization.py        # Visualization functions
├── output/
│   └── charts/                 # Generated charts
├── main.py                     # Main execution script
├── requirements.txt            # Project dependencies
├── .gitignore
└── README.md
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mani977-lang/Staff-Data-Dashboard.git
   cd Staff-Data-Dashboard
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the main analysis script:

```bash
python main.py
```

This will:
- Generate sample employee data (100 records)
- Perform statistical analysis
- Display summary statistics
- Generate 6 different visualization charts
- Save data to CSV and Excel files

### Key Modules

#### `data/sample_data.py`
- `generate_sample_data()` - Creates sample employee dataset

#### `src/analysis.py`
- `get_summary_statistics()` - Overall statistics
- `salary_by_department()` - Average salary analysis
- `employees_by_department()` - Count by department
- `salary_by_job_title()` - Title-based salary analysis
- `performance_statistics()` - Performance metrics
- `high_performers()` - Filter top performers
- `salary_experience_correlation()` - Correlation analysis

#### `src/visualization.py`
- `create_salary_by_department_chart()` - Bar chart
- `create_employee_distribution_chart()` - Pie chart
- `create_performance_distribution_chart()` - Histogram
- `create_salary_vs_experience_chart()` - Scatter plot
- `create_job_title_salary_chart()` - Horizontal bar chart
- `create_heatmap_salary_performance()` - Heatmap

#### `src/data_loader.py`
- `load_csv()` - Load CSV files
- `load_excel()` - Load Excel files
- `save_to_csv()` - Export to CSV
- `save_to_excel()` - Export to Excel

### Using Your Own Data

To analyze your own employee data:

1. **Create a CSV or Excel file** with columns like:
   - Employee_ID
   - Name
   - Department
   - Job_Title
   - Salary
   - Years_Experience
   - Performance_Rating

2. **Modify `main.py`** to load your data:
   ```python
   from src.data_loader import load_csv
   
   df = load_csv('path/to/your/employee_data.csv')
   ```

3. **Run the analysis** with your data

### Dependencies

- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Plotting and visualization
- **seaborn** - Statistical data visualization
- **openpyxl** - Excel file handling

### Output

After running the script, you'll get:

- **Data Files:**
  - `data/output/employee_data.csv`
  - `data/output/employee_data.xlsx`

- **Charts:**
  - Salary by Department
  - Employee Distribution
  - Performance Distribution
  - Salary vs Experience
  - Salary by Job Title
  - Salary & Performance Heatmap

### Example Output

```
============================================================
EMPLOYEE DATA ANALYSIS DASHBOARD
============================================================

1. Generating sample employee data...
   ✓ Generated 100 employee records

2. Summary Statistics:
   Total Employees: 100
   Total Departments: 6
   Average Salary: $87,450
   Average Performance Rating: 3.52
```

### Future Enhancements

- [ ] Interactive dashboard with Plotly
- [ ] Advanced filtering and querying
- [ ] Export reports to PDF
- [ ] Predictive analytics
- [ ] Department-wise detailed reports
- [ ] Bonus/incentive analysis
- [ ] Turnover rate analysis

### Author

Created by: [Mani977-lang](https://github.com/Mani977-lang)

### License

This project is open source and available under the MIT License.
