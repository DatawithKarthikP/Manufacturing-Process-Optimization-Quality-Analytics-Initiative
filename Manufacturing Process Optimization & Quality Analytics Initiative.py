# manufacturing_analytics.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

df = pd.read_csv('data/manufacturing_data.csv')

# =============================
# 📈 KPI Calculations
# =============================

# KPI 1: Average Production Time by Machine
avg_time_by_machine = df.groupby('Machine_ID')['Production_Time_Min'].mean().sort_values()

# KPI 2: Defect Rate per Machine
defect_rate = (df.groupby('Machine_ID')['Defective_Units'].sum() /
               df.groupby('Machine_ID')['Units_Produced'].sum()).round(4)

# KPI 3: Downtime Analysis
avg_downtime = df.groupby('Machine_ID')['Downtime_Min'].mean().sort_values()

# KPI 4: Yield Rate Over Time
yield_over_time = df.groupby(pd.Grouper(key='Production_Date', freq='D'))['Yield_Rate'].mean()

# KPI 5: Operator Efficiency (Yield Rate)
operator_yield = df.groupby('Operator_ID')['Yield_Rate'].mean().sort_values(ascending=False)

# =============================
# 📊 Visualizations
# =============================

# 1. Avg Production Time by Machine
plt.figure(figsize=(8,5))
sns.barplot(x=avg_time_by_machine.index, y=avg_time_by_machine.values, palette='Blues_d')
plt.title("Average Production Time by Machine")
plt.ylabel("Avg Time (min)")
plt.xlabel("Machine")
plt.tight_layout()
plt.savefig("avg_production_time_by_machine.png")
plt.close()

# 2. Defect Rate per Machine
plt.figure(figsize=(8,5))
sns.barplot(x=defect_rate.index, y=defect_rate.values, palette='Reds_d')
plt.title("Defect Rate per Machine")
plt.ylabel("Defect Rate")
plt.xlabel("Machine")
plt.tight_layout()
plt.savefig("defect_rate_per_machine.png")
plt.close()

# 3. Daily Yield Rate Over Time
plt.figure(figsize=(10,5))
yield_over_time.plot()
plt.title("Daily Average Yield Rate Over Time")
plt.ylabel("Yield Rate")
plt.xlabel("Date")
plt.tight_layout()
plt.savefig("yield_rate_over_time.png")
plt.close()

# 4. Operator Efficiency (Yield Rate)
plt.figure(figsize=(8,5))
sns.barplot(x=operator_yield.index, y=operator_yield.values, palette='Greens_d')
plt.title("Average Yield Rate by Operator")
plt.ylabel("Yield Rate")
plt.xlabel("Operator")
plt.tight_layout()
plt.savefig("yield_by_operator.png")
plt.close()

# =============================
# 🧾 Summary KPIs
# =============================
summary = {
    "Overall Avg Production Time": round(df['Production_Time_Min'].mean(), 2),
    "Overall Defect Rate": round(df['Defective_Units'].sum() / df['Units_Produced'].sum(), 4),
    "Overall Avg Downtime": round(df['Downtime_Min'].mean(), 2),
    "Overall Avg Yield Rate": round(df['Yield_Rate'].mean(), 4)
}

# Print summary to console
print("----- Manufacturing KPIs Summary -----")
for k, v in summary.items():
    print(f"{k}: {v}")
