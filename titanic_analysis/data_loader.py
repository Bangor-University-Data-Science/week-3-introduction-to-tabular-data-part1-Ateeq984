# import pandas as pd
# def load_titanic_data(filepath: str) -> pd.DataFrame:
#     df = pd.read_csv(filepath)
#     return df

# last
# import pandas as pd
# def load_titanic_data(filepath: str) -> pd.DataFrame:
#     df = pd.read_csv(filepath)
#     return df
#     if __name__ == "__main__":
#         filepath = "data/titanic.csv"
#         titanic_data = load_titanic_data(filepath)

import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    Args:
        filepath (str): Path to the Titanic CSV file.
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv("../../data/titanic.csv")
    
    # Return the loaded DataFrame
    return df  