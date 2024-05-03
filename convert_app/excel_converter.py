import pandas as pd

def csv_to_excel(csv_file, excel_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Write the DataFrame to an Excel file
    with pd.ExcelWriter(excel_file) as writer:
        df.to_excel(writer, index=False)

# Example usage:
# csv_to_excel('input.csv', 'output.xlsx')
