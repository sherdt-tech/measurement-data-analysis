import pandas as pd

data = pd.read_csv("data/sample_measurement.csv")

print("Mean temperature:", data["temperature"].mean())
print("Min temperature:", data["temperature"].min())
print("Max temperature:", data["temperature"].max())
