import pandas as pd
data_file = "./data/house_tiny.csv"
data = None
try:
    data = pd.read_csv(data_file)
except FileNotFoundError:
    print("File not found")

print(f"data: {data}")