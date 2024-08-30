# main.py
import pandas as pd

def calculate_mean(data: pd.DataFrame, column: str) -> float:
    """
    Calculate the mean of a specified column in the DataFrame.
    
    Parameters:
    data (pd.DataFrame): The input data.
    column (str): The column name for which to calculate the mean.
    
    Returns:
    float: The mean of the specified column.
    """
    return data[column].mean()

def main():
    # Example data
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })

    mean_a = calculate_mean(data, 'A')
    mean_b = calculate_mean(data, 'B')

    print(f"Mean of column A: {mean_a}")
    print(f"Mean of column B: {mean_b}")

if __name__ == "__main__":
    main()