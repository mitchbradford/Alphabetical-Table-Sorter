# Script by Mitch Bradford
# Dependencies - Pandas, Python 3
# Instructions - enter two columns of data in input.csv to be sorted

# -----------------------------------------------------------------------
import pandas as pd

# Input and output file names
input_file = 'input.csv'
output_file = 'sorted_output.csv'

# If your CSV has a header row, change header=None to header=0 and header=False to header=True in the script.
# Read the CSV file
df = pd.read_csv(input_file, header=None)  # Assumes no header; change as needed

# Sort by the first column (column index 0)
df_sorted = df.sort_values(by=0)

# Write the sorted DataFrame to a new CSV file
df_sorted.to_csv(output_file, index=False, header=False)

print(f"Sorted data saved to {output_file}")
