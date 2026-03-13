import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show first 5 rows
print(df.head())

# Count Movies vs TV Shows
print(df['type'].value_counts())

# Plot graph
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.show()
print(df['country'].value_counts().head())
print(df['release_year'].value_counts().head())
print(df['listed_in'].value_counts().head())
df['release_year'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Release Years")
plt.show()