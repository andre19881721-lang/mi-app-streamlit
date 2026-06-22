
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Workplace Insights Dashboard", layout="wide")

st.title("Executive Summary - Workplace Insights")

# Metrics
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Avg Daily Occupancy", "2,100 / 2,600", "81% utilization")
col2.metric("Peak Occupancy", "2,450", "94% utilization")
col3.metric("P95 Occupancy", "2,350", "90% utilization")
col4.metric("Available Desks (avg)", "500")
col5.metric("Unused Space", "4,940 m²")

st.divider()

# Weekly distribution
st.subheader("Occupancy by Day of Week")
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
values = [1850, 2250, 2350, 2200, 1750]

fig, ax = plt.subplots()
ax.bar(days, values)
ax.set_ylabel("Average Occupancy")
st.pyplot(fig)

# Trend (synthetic)
st.subheader("Daily Occupancy Trend (Last 6 Months)")
np.random.seed(42)
trend = 1700 + np.random.randn(120) * 200

fig2, ax2 = plt.subplots()
ax2.plot(trend)
ax2.set_ylabel("Occupancy")
ax2.set_xlabel("Days")
st.pyplot(fig2)

# Building split
st.subheader("Occupancy by Building")
labels = ["Building A", "Building B"]
vals = [1050, 1050]

fig3, ax3 = plt.subplots()
ax3.pie(vals, labels=labels, autopct="%1.1f%%")
st.pyplot(fig3)

# Floor analysis
st.subheader("Floor Utilization")
floors = ["F1", "F2", "F3", "F4"]
a = [95, 88, 75, 62]
b = [92, 85, 73, 58]

df = pd.DataFrame({"Floor": floors, "Building A (%)": a, "Building B (%)": b})
st.dataframe(df)

# Financial impact
st.subheader("Financial Impact")
unused = 4940
rate = 25
monthly = unused * rate
annual = monthly * 12

st.write(f"Estimated unused space: {unused} m²")
st.write(f"Monthly savings potential: ${monthly:,.0f}")
st.write(f"Annual savings potential: ${annual:,.0f}")

st.success("Recommendation: Consolidate occupancy in high-demand floors and reduce leased space to optimize costs.")
