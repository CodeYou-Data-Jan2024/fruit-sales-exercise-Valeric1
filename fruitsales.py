import pandas as pd

# Create a dictionary with the data
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

# Create the DataFrame
df = pd.DataFrame(data, index=['2017 Sales', '2018 Sales'])

# Display the DataFrame
print(df)
