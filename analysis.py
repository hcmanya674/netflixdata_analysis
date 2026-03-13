import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show basic information
print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nFirst 5 rows:\n", df.head())

# Movies vs TV Shows
type_counts = df['type'].value_counts()
print("\nContent Types:\n", type_counts)

type_counts.plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("movies_vs_tvshows.png")
plt.show()

# Top 10 release years
year_counts = df['release_year'].value_counts().head(10)
year_counts.plot(kind='bar')
plt.title("Top 10 Release Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.savefig("top_release_years.png")
plt.show()

# Top 10 countries
country_counts = df['country'].value_counts().head(10)
country_counts.plot(kind='bar')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.savefig("top_countries.png")
plt.show()
