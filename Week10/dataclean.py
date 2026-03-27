import pandas as pd

# Read CSV file
df = pd.read_csv("new_students.csv")

print("Original DataFrame:")
print(df)

# Data Cleaning 

# Remove spaces
df["name"] = df["name"].str.strip()
df["department"] = df["department"].str.strip()

# Fill missing values
df["department"] = df["department"].fillna("Unknown")
df["marks"] = df["marks"].fillna(0)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nAfter Data Cleaning:")
print(df)

# DataFrame Modification 

# Add Result column
df["Result"] = "Pass"

# Condition based on marks
df.loc[df["marks"] < 40, "Result"] = "Fail"

# Rename column
df.rename(columns={"marks": "Score"}, inplace=True)

print("\nAfter DataFrame Modification:")
print(df)
