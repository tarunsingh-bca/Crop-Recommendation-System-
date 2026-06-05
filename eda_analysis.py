import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("clean_data_core.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Shape of dataset
print("\nShape of dataset:", df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types and info
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Value counts for categorical columns
print("\nSoil Type Counts:")
print(df['soil_type'].value_counts())

print("\nCrop Type Counts:")
print(df['crop_type'].value_counts())

print("\nFertilizer Counts:")
print(df['fertilizer_name'].value_counts())

# Numerical columns
num_cols = ['temperature', 'humidity', 'moisture', 'nitrogen', 'potassium', 'phosphorous']

# Histograms
df[num_cols].hist(figsize=(12, 8), bins=20)
plt.suptitle("Histograms of Numerical Features")
plt.tight_layout()
plt.show()

# Boxplots
for col in num_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Soil type distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='soil_type', data=df)
plt.title("Soil Type Distribution")
plt.show()

# Crop type distribution
plt.figure(figsize=(12, 5))
sns.countplot(x='crop_type', data=df, order=df['crop_type'].value_counts().index)
plt.xticks(rotation=90)
plt.title("Crop Type Distribution")
plt.show()

# Fertilizer distribution
plt.figure(figsize=(12, 5))
sns.countplot(x='fertilizer_name', data=df, order=df['fertilizer_name'].value_counts().index)
plt.xticks(rotation=90)
plt.title("Fertilizer Distribution")
plt.show()

# Fertilizer vs soil type
plt.figure(figsize=(10, 5))
sns.countplot(x='soil_type', hue='fertilizer_name', data=df)
plt.title("Fertilizer Usage by Soil Type")
plt.show()

# Fertilizer vs crop type
plt.figure(figsize=(14, 6))
sns.countplot(x='crop_type', hue='fertilizer_name', data=df)
plt.xticks(rotation=90)
plt.title("Fertilizer Usage Across Crop Types")
plt.show()

# Nitrogen by fertilizer
plt.figure(figsize=(12, 5))
sns.boxplot(x='fertilizer_name', y='nitrogen', data=df)
plt.xticks(rotation=90)
plt.title("Nitrogen Distribution by Fertilizer")
plt.show()