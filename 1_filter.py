import pandas as pd

###
#  Process text data
###
df = pd.read_csv('assets/text_analysis.csv')

df = df.rename(columns={'created_at': 'datetime'})
df['datetime'] = pd.to_datetime(df['datetime'])
df['date'] = df['datetime'].dt.date

# Filter rows by date
df = df[df['datetime'] >= '2025-03-28']
df = df[df['datetime'] <= '2025-05-22']

# Save the filtered DataFrame to a new Excel file
df.to_excel('filtered/text.xlsx', index=False)

###
# Process comparison data
###
df = pd.read_csv('assets/comparison_analysis.csv')

df = df.rename(columns={'text1': 'text'})
df = df.rename(columns={'created_at': 'datetime'})
df['datetime'] = pd.to_datetime(df['datetime'])
df['date'] = df['datetime'].dt.date

# Filter rows by date
df = df[df['datetime'] >= '2025-03-28']
df = df[df['datetime'] <= '2025-05-22']

# Save the filtered DataFrame to a new Excel file
df.to_excel('filtered/comparison.xlsx', index=False)


###
# Process simplification data
###
df = pd.read_csv('assets/text_simplification.csv')

df = df.rename(columns={'created_at': 'datetime'})
df['datetime'] = pd.to_datetime(df['datetime'])
df['date'] = df['datetime'].dt.date

# Filter rows by date
df = df[df['datetime'] >= '2025-03-28']
df = df[df['datetime'] <= '2025-05-22']

# Save the filtered DataFrame to a new Excel file
df.to_excel('filtered/simplification.xlsx', index=False)
