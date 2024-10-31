
import pandas as pd

def create_summary_table(df):
    
    summary_df = pd.DataFrame({
        'Feature Name': df.columns,   
        'Data Type': [df[col].dtype for col in df.columns],   
        'Number of Unique Values': [df[col].nunique() for col in df.columns],  
        'Has Missing Values?': [df[col].isnull().any() for col in df.columns]  
    })
    
    
    summary_df = summary_df[['Feature Name', 'Data Type', 'Number of Unique Values', 'Has Missing Values?']]
    
    
    print("Columns in summary_df:", summary_df.columns.tolist())
    
    return summary_df