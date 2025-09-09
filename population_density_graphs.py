# ===========================================
# population_density_graphs.py
# Author: Michael (Data Analyst Portfolio)
# Purpose: Show largest population centers in Texas
# ===========================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("2023_txpopest_place.csv")

# Step 2: Select city + population estimate (2024)
df_pop = df[["Place", "jan1_2024_pop_est"]]

# Step 3: Clean data (remove missing values)
df_pop = df_pop.dropna()

# Step 4: Sort by 2024 population
df_pop_sorted = df_pop.sort_values(by="jan1_2024_pop_est", ascending=False)

# Step 5: Take top 10 largest cities
top10_pop = df_pop_sorted.head(10)

# Step 6: Plot bar chart
plt.figure(figsize=(10,6))
plt.bar(top10_pop["Place"], top10_pop["jan1_2024_pop_est"], color="orange")
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Most Populated Cities in Texas (2024 Estimate)", fontsize=14)
plt.xlabel("City")
plt.ylabel("Population")

# Step 7: Save chart as PNG
plt.tight_layout()
plt.savefig("top10_population_2024.png", dpi=300)

# Step 8: Show chart (optional)
plt.show()

print("✅ Graph created and saved as top10_population_2024.png")
