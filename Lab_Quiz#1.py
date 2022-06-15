# Import pandas library
import pandas as pd
import numpy as np

# initialize list elements
id = [12345, 12346, 12347, 12348, 12349, 12350, 12351, 12352, 12353, 12354]
name = [ 'John', 'Mike', 'Jim', 'Peter', 'Jack', 'Andrew', 'Adam', 'Jeff', 'David', 'Kevin']
gpa = [3.5, 3.45, 2.95, 3.12, 2.65, 3.01, 3.70, 2.89, 3.34, 3.82]

# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(data={'Id':id, 'Name':name, 'GPA':gpa})

# Based on above dataframe, change record index to GPA
df.index = gpa

# Generate time series from 7/1/2020 to 8/1/2020
df['Date'] = pd.date_range(start = '7/1/2020', end = '8/1/2020', periods=10)

# Add one more column for student's major BSCS or MSCS
# Randomly choose one of the two major
df['Major'] = np.random.choice(['BSCS', 'MSCS'], size=10)

# Align headers in center
df.columns.align = 'center'
pd.set_option('display.colheader_justify', 'center')

# Print the dataframe
print(df)
