# ===========================================
# population_growth_graphs.py
# Author: Michael (Data Analyst Portfolio)
# Purpose: Analyze TX city population growth
# ===========================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Make sure this CSV is in the same folder as this script
df = pd.read_csv("2023_txpopest_place.csv")

# Step 2: Select the columns we need
# Place = city name, pct_chg_20_24 = percent change 2020–2024
df_growth = df[["Place", "pct_chg_20_24"]]

# Step 3: Clean data (remove missing values just in case)
df_growth = df_growth.dropna()

# Step 4: Sort cities by growth rate
df_growth_sorted = df_growth.sort_values(by="pct_chg_20_24", ascending=False)

# Step 5: Take top 10 fastest growing cities
top10 = df_growth_sorted.head(10)

# Step 6: Plot bar chart
plt.figure(figsize=(10,6))
plt.bar(top10["Place"], top10["pct_chg_20_24"], color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Fastest Growing Cities in Texas (2020–2024)", fontsize=14)
plt.xlabel("City")
plt.ylabel("Growth Rate (%)")

# Step 7: Save the graph as PNG
plt.tight_layout()
plt.savefig("population_growth_top10.png", dpi=300)

# Step 8: Show the graph (optional)
plt.show()

print("✅ Graph created and saved as population_growth_top10.png")
