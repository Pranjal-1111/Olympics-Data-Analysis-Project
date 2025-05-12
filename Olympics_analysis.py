
# olympics_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

import pandas as pd

# Use this for Excel files
df = pd.read_excel("olympics_analysis_report.xlsx")


# Preview
print("Shape of dataset:", df.shape)
print("Columns:", df.columns)

# Clean data
df.dropna(subset=["Medal"], inplace=True)

# ------------------------------
# 🥇 Top 10 Countries by Medals
# ------------------------------
top_countries = df['Country'].value_counts().head(10)
plt.figure()
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title("Top 10 Countries by Total Medals", fontsize=16, fontweight='bold')
plt.xlabel("Total Medals")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("output_charts/top_10_countries.png")
plt.show()

# ----------------------------------
# 👫 Gender Distribution of Medals
# ----------------------------------
gender_dist = df['Gender'].value_counts()
plt.figure()
plt.pie(gender_dist, labels=gender_dist.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#ff9999'])
plt.title("Gender Distribution of Medal Winners", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig("output_charts/gender_distribution.png")
plt.show()

# ----------------------------------
# 📈 Medal Count by Year
# ----------------------------------
medals_per_year = df['Year'].value_counts().sort_index()
plt.figure()
sns.lineplot(x=medals_per_year.index, y=medals_per_year.values, marker='o', color='green')
plt.title("Total Medals Awarded Per Olympic Year", fontsize=16, fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Number of Medals")
plt.tight_layout()
plt.savefig("output_charts/medals_by_year.png")
plt.show()

# -------------------------------------
# 🔥 Most Awarded Athletes (Top 10)
# -------------------------------------
top_athletes = df['Athlete'].value_counts().head(10)
plt.figure()
sns.barplot(x=top_athletes.values, y=top_athletes.index, palette="magma")
plt.title("Top 10 Medal-Winning Athletes", fontsize=16, fontweight='bold')
plt.xlabel("Total Medals")
plt.ylabel("Athlete")
plt.tight_layout()
plt.savefig("output_charts/top_athletes.png")
plt.show()

# -------------------------------------
# 🏅 Medals by Sport (Top 10)
# -------------------------------------
top_sports = df['Sport'].value_counts().head(10)
plt.figure()
sns.barplot(x=top_sports.values, y=top_sports.index, palette='coolwarm')
plt.title("Top 10 Sports by Medal Count", fontsize=16, fontweight='bold')
plt.xlabel("Total Medals")
plt.ylabel("Sport")
plt.tight_layout()
plt.savefig("output_charts/top_sports.png")
plt.show()

# --------------------------------------
# 🧊 Heatmap: Country vs Year (Medals)
# --------------------------------------
heatmap_data = df.pivot_table(index='Country', columns='Year', values='Medal', aggfunc='count').fillna(0)
heatmap_data = heatmap_data.loc[heatmap_data.sum(axis=1).sort_values(ascending=False).head(10).index]  # top 10
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='g', linewidths=0.5)
plt.title("Top 10 Countries – Medal Count Heatmap", fontsize=16, fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("output_charts/heatmap_medals.png")
plt.show()
