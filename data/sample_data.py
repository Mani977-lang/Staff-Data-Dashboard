"""
Sample employee data generator for testing and demonstration
"""
import pandas as pd
from datetime import datetime, timedelta
import random


def generate_sample_data(num_employees=100):
    """
    Generate sample employee data for analysis
    
    Parameters:
    -----------
    num_employees : int
        Number of employee records to generate
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with sample employee data
    """
    departments = ['HR', 'IT', 'Finance', 'Operations', 'Sales', 'Marketing']
    job_titles = ['Manager', 'Senior Developer', 'Developer', 'Analyst', 'Coordinator', 'Director']
    
    data = {
        'Employee_ID': [f'EMP{str(i).zfill(4)}' for i in range(1, num_employees + 1)],
        'Name': [f'Employee_{i}' for i in range(1, num_employees + 1)],
        'Department': [random.choice(departments) for _ in range(num_employees)],
        'Job_Title': [random.choice(job_titles) for _ in range(num_employees)],
        'Salary': [random.randint(30000, 150000) for _ in range(num_employees)],
        'Years_Experience': [random.randint(0, 20) for _ in range(num_employees)],
        'Joining_Date': [datetime(2015, 1, 1) + timedelta(days=random.randint(0, 3650)) 
                        for _ in range(num_employees)],
        'Performance_Rating': [round(random.uniform(2.0, 5.0), 1) for _ in range(num_employees)],
    }
    
    df = pd.DataFrame(data)
    return df
