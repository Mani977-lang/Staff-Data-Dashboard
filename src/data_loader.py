"""
Data loading module for employee data
"""
import pandas as pd
import os


def load_csv(file_path):
    """
    Load employee data from CSV file
    
    Parameters:
    -----------
    file_path : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Loaded employee data
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None


def load_excel(file_path, sheet_name=0):
    """
    Load employee data from Excel file
    
    Parameters:
    -----------
    file_path : str
        Path to the Excel file
    sheet_name : str or int
        Sheet name or index to load
        
    Returns:
    --------
    pd.DataFrame
        Loaded employee data
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Successfully loaded data from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None


def save_to_csv(df, file_path):
    """
    Save DataFrame to CSV file
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to save
    file_path : str
        Path where to save the CSV file
    """
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")


def save_to_excel(df, file_path, sheet_name='Sheet1'):
    """
    Save DataFrame to Excel file
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to save
    file_path : str
        Path where to save the Excel file
    sheet_name : str
        Sheet name in Excel file
    """
    df.to_excel(file_path, sheet_name=sheet_name, index=False)
    print(f"Data saved to {file_path}")
