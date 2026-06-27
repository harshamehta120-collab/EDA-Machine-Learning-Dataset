import pandas as pd

# Load dataset
df = pd.read_csv("train.csv")

# First 5 rows
print(df.head())

import pandas as pd

# Load dataset
df = pd.read_csv("train.csv")

# First 5 rows
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

import matplotlib.pyplot as plt

# Survival Count Plot
# df["Survived"].value_counts().plot(kind="bar")
# plt.title("Survival Count")
# plt.xlabel("Survived (0 = No, 1 = Yes)")
# plt.ylabel("Number of Passengers")
# plt.show()


import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
df["Age"].dropna().hist(bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.show()