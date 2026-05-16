"""
Main script to run employee data analysis and generate visualizations
"""
import sys
sys.path.insert(0, '.')

from data.sample_data import generate_sample_data
from src.data_loader import save_to_csv, save_to_excel
from src.analysis import (
    get_summary_statistics,
    salary_by_department,
    employees_by_department,
    salary_by_job_title,
    performance_statistics,
    high_performers,
    salary_experience_correlation
)
from src.visualization import (
    create_salary_by_department_chart,
    create_employee_distribution_chart,
    create_performance_distribution_chart,
    create_salary_vs_experience_chart,
    create_job_title_salary_chart,
    create_heatmap_salary_performance
)
import os


def main():
    """Main execution function"""
    
    print("=" * 60)
    print("EMPLOYEE DATA ANALYSIS DASHBOARD")
    print("=" * 60)
    
    # Generate sample data
    print("\n1. Generating sample employee data...")
    df = generate_sample_data(num_employees=100)
    print(f"   ✓ Generated {len(df)} employee records\n")
    
    # Display first few records
    print("Sample Data Preview:")
    print(df.head())
    print()
    
    # Save data
    print("2. Saving data...")
    os.makedirs('data/output', exist_ok=True)
    save_to_csv(df, 'data/output/employee_data.csv')
    save_to_excel(df, 'data/output/employee_data.xlsx')
    print()
    
    # Summary Statistics
    print("3. Summary Statistics:")
    summary = get_summary_statistics(df)
    for key, value in summary.items():
        print(f"   {key}: {value}")
    print()
    
    # Salary Analysis
    print("4. Salary by Department:")
    salary_dept = salary_by_department(df)
    print(salary_dept)
    print()
    
    # Employee Count by Department
    print("5. Employee Count by Department:")
    emp_dept = employees_by_department(df)
    print(emp_dept)
    print()
    
    # Salary by Job Title
    print("6. Average Salary by Job Title:")
    salary_title = salary_by_job_title(df)
    print(salary_title)
    print()
    
    # Performance Statistics
    print("7. Performance Rating Statistics:")
    perf_stats = performance_statistics(df)
    for key, value in perf_stats.items():
        print(f"   {key}: {value}")
    print()
    
    # High Performers
    print("8. High Performers (Rating >= 4.0):")
    high_perf = high_performers(df)
    print(f"   Total: {len(high_perf)} employees")
    print(high_perf[['Employee_ID', 'Name', 'Department', 'Performance_Rating']].head(10))
    print()
    
    # Correlation
    print("9. Salary-Experience Correlation:")
    correlation = salary_experience_correlation(df)
    print(f"   Correlation coefficient: {correlation:.3f}")
    print()
    
    # Generate Visualizations
    print("10. Generating visualizations...")
    os.makedirs('output/charts', exist_ok=True)
    
    create_salary_by_department_chart(df, 'output/charts/salary_by_department.png')
    create_employee_distribution_chart(df, 'output/charts/employee_distribution.png')
    create_performance_distribution_chart(df, 'output/charts/performance_distribution.png')
    create_salary_vs_experience_chart(df, 'output/charts/salary_vs_experience.png')
    create_job_title_salary_chart(df, 'output/charts/salary_by_job_title.png')
    create_heatmap_salary_performance(df, 'output/charts/salary_performance_heatmap.png')
    
    print("\n" + "=" * 60)
    print("✓ Analysis Complete!")
    print("=" * 60)
    print("\nOutputs saved to:")
    print("   - CSV: data/output/employee_data.csv")
    print("   - Excel: data/output/employee_data.xlsx")
    print("   - Charts: output/charts/")
    print()


if __name__ == "__main__":
    main()
