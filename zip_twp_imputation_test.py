import pandas as pd
df = pd.read_csv('911.csv')

addr_unique = {}
print(f"twp null - {df['twp'].isnull().sum()}")
print(f"zip null - {df['zip'].isnull().sum()}")
for index, row in df.iterrows():
    if not (pd.isnull(row['twp']) or pd.isnull(row['zip'])):
        addr = row['addr']
        zip = row['zip']
        twp = row['twp']

        if addr not in addr_unique:
            addr_unique[addr] = {}
        
        addr_unique[addr][zip] = twp
    

# zip_twp = {}
# twp = []
# for index, row in df.iterrows():
#     if (row['twp'] not in twp) and (not pd.isnull(row['zip'])):
#         twp.append(row['twp'])
#         zip_twp[row['twp']] = row['zip']

# for key, value in zip_twp.items():
#     print(f"{key}: {value}")
        
for index, row in df.iterrows():
    if pd.isnull(row['twp']):
        addr = row['addr']
        zip_code = row['zip']
        if (addr in addr_unique) and (zip_code in addr_unique[addr]):
            df.at[index, 'twp'] = addr_unique[addr][zip_code]


zip_by_addr_and_twp = {}
for index, row in df.iterrows():
    if not (pd.isnull(row['twp']) or pd.isnull(row['zip'])):
        addr = row['addr']
        zip_code = row['zip']
        twp = row['twp']

        if addr not in zip_by_addr_and_twp:
            zip_by_addr_and_twp[addr] = {}
        
        zip_by_addr_and_twp[addr][twp] = zip_code

for index, row in df.iterrows():
    if pd.isnull(row['zip']):
        addr = row['addr']
        twp = row['twp']
        if (addr in zip_by_addr_and_twp) and (twp in zip_by_addr_and_twp[addr]):
            df.at[index, 'zip'] = zip_by_addr_and_twp[addr][twp]




print(len(addr_unique))
print(df)

print(f"twp null - {df['twp'].isnull().sum()}")
print(f"zip null - {df['zip'].isnull().sum()}")

print(df[df['twp'].isnull()])
print(df[df['zip'].isnull()])
