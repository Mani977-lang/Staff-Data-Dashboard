"""
Data analysis module for employee data
"""
import pandas as pd
import numpy as np


def get_summary_statistics(df):
    """
    Get summary statistics of the dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
        
    Returns:
    --------
    dict
        Summary statistics
    """
    summary = {
        'Total Employees': len(df),
        'Total Departments': df['Department'].nunique() if 'Department' in df.columns else 0,
        'Average Salary': df['Salary'].mean() if 'Salary' in df.columns else 0,
        'Salary Range': f"${df['Salary'].min():,.0f} - ${df['Salary'].max():,.0f}" if 'Salary' in df.columns else 'N/A',
        'Average Experience': round(df['Years_Experience'].mean(), 1) if 'Years_Experience' in df.columns else 0,
        'Average Performance Rating': round(df['Performance_Rating'].mean(), 2) if 'Performance_Rating' in df.columns else 0,
    }
    return summary


def salary_by_department(df):
    """
    Calculate average salary by department
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
        
    Returns:
    --------
    pd.Series
        Average salary by department
    """
    return df.groupby('Department')['Salary'].mean().sort_values(ascending=False)


def employees_by_department(df):
    """
    Count employees by department
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
        
    Returns:
    --------
    pd.Series
        Employee count by department
    """
    return df.groupby('Department').size().sort_values(ascending=False)


def salary_by_job_title(df):
    """
    Calculate average salary by job title
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
        
    Returns:
    --------
    pd.Series
        Average salary by job title
    """
    return df.groupby('Job_Title')['Salary'].mean().sort_values(ascending=False)


def performance_statistics(df):
    """
    Get performance rating statistics
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
        
    Returns:
    --------
    dict
        Performance statistics
    """
    return {
        'Average Rating': round(df['Performance_Rating'].mean(), 2),
        'Median Rating': round(df['Performance_Rating'].median(), 2),
        'Min Rating': df['Performance_Rating'].min(),
        'Max Rating': df['Performance_Rating'].max(),
        'Std Dev': round(df['Performance_Rating'].std(), 2),
    }


def high_performers(df, threshold=4.0):
    """
    Get high performers (rating >= threshold)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
    threshold : float
        Minimum performance rating
        
    Returns:
    --------
    pd.DataFrame
        High performing employees
    """
    return df[df['Performance_Rating'] >= threshold].sort_values('Performance_Rating', ascending=False)


def salary_experience_correlation(df):
    """
    Calculate correlation between salary and years of experience
    
    Parameters:
    -----------
    df : pd.DataFrame
        Employee data
        
    Returns:
    --------
    float
        Correlation coefficient
    """
    return df['Salary'].corr(df['Years_Experience'])
