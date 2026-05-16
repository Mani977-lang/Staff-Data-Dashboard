"""
Visualization module for employee data analysis
"""
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def create_salary_by_department_chart(df, save_path=None):
    """
    Create bar chart of average salary by department
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
    save_path : str, optional
        Path to save the figure
    """
    salary_by_dept = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=salary_by_dept.index, y=salary_by_dept.values, palette='viridis')
    plt.title('Average Salary by Department', fontsize=16, fontweight='bold')
    plt.xlabel('Department', fontsize=12)
    plt.ylabel('Average Salary ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    plt.show()


def create_employee_distribution_chart(df, save_path=None):
    """
    Create pie chart of employee distribution by department
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
    save_path : str, optional
        Path to save the figure
    """
    emp_by_dept = df['Department'].value_counts()
    
    plt.figure(figsize=(10, 6))
    plt.pie(emp_by_dept.values, labels=emp_by_dept.index, autopct='%1.1f%%', startangle=90)
    plt.title('Employee Distribution by Department', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    plt.show()


def create_performance_distribution_chart(df, save_path=None):
    """
    Create histogram of performance rating distribution
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
    save_path : str, optional
        Path to save the figure
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['Performance_Rating'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Performance Ratings', fontsize=16, fontweight='bold')
    plt.xlabel('Performance Rating', fontsize=12)
    plt.ylabel('Number of Employees', fontsize=12)
    plt.axvline(df['Performance_Rating'].mean(), color='red', linestyle='--', 
                linewidth=2, label=f'Mean: {df["Performance_Rating"].mean():.2f}')
    plt.legend()
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    plt.show()


def create_salary_vs_experience_chart(df, save_path=None):
    """
    Create scatter plot of salary vs experience
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
    save_path : str, optional
        Path to save the figure
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Years_Experience'], df['Salary'], alpha=0.6, s=100, color='green')
    
    # Add trend line
    z = np.polyfit(df['Years_Experience'], df['Salary'], 1)
    p = np.poly1d(z)
    plt.plot(df['Years_Experience'].sort_values(), p(df['Years_Experience'].sort_values()), 
             "r--", linewidth=2, label='Trend Line')
    
    plt.title('Salary vs Years of Experience', fontsize=16, fontweight='bold')
    plt.xlabel('Years of Experience', fontsize=12)
    plt.ylabel('Salary ($)', fontsize=12)
    plt.legend()
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    plt.show()


def create_job_title_salary_chart(df, save_path=None):
    """
    Create bar chart of average salary by job title
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
    save_path : str, optional
        Path to save the figure
    """
    salary_by_title = df.groupby('Job_Title')['Salary'].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=salary_by_title.values, y=salary_by_title.index, palette='coolwarm')
    plt.title('Average Salary by Job Title', fontsize=16, fontweight='bold')
    plt.xlabel('Average Salary ($)', fontsize=12)
    plt.ylabel('Job Title', fontsize=12)
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    plt.show()


def create_heatmap_salary_performance(df, save_path=None):
    """
    Create heatmap of salary and performance by department
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
    save_path : str, optional
        Path to save the figure
    """
    dept_stats = df.groupby('Department')[['Salary', 'Performance_Rating']].mean()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(dept_stats.T, annot=True, fmt='.0f', cmap='YlGnBu', cbar_kws={'label': 'Value'})
    plt.title('Salary and Performance by Department', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    plt.show()


import numpy as np
