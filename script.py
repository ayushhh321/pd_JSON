import pandas as pd

# Load Excel file into DataFrame
df = pd.read_excel('pincodes_Ids_latest_excel.xlsx')

# Convert DataFrame to JSON string
json_data = df.to_json(orient='records')
