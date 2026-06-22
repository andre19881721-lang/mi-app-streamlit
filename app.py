import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Workplace Insights Dashboard", layout="wide")

# -------------------------
# DATA (translated to English)
# -------------------------
total_capacity = 2600

avg_occupancy = 2100
peak_occupancy = 2450
p95_occupancy = 2350
vacant_desks = 500

unused_space_m2 = 4940
total_space_m2 = 26000
rent_per_m2 = 25

# Time series (synthetic but consistent)
np.random.seed(7)
dates = pd.date_range("2024-12-01", "2025-05-31", freq="D")
occupancy = np.clip(
    np.random.normal(2100, 250, len(dates)),
    1200,
    2600
)

df = pd.DataFrame({"date": dates, "occupancy": occupancy})

# Weekday distribution
weekday_data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Occupancy": [1850, 2250, 2350, 2200, 1750]
})

# Buildings
building_data = pd.DataFrame({
    "Building": ["Building A", "Building B"],
    "Avg Occupancy": [1050, 1050]
})

# Floor analysis
floor_data = pd.DataFrame({
    "Floor": ["Floor 4", "Floor 3", "Floor 2", "Floor 1"],
    "Building A": [62, 75, 88, 95],
    "Building B": [58, 73, 85, 92],
})

# Financial impact
monthly_savings = unused_space_m2 * rent_per_m2
annual_savings = monthly_savings * 12

# -------------------------
# SIDEBAR FILTERS
# -------------------------
st.sidebar.title("Filters")
date_range = st.sidebar.date_input(
    "Date range",
    [df["date"].min(), df["date"].max()]
)

building_filter = st.sidebar.selectbox(
    "Building",
    ["All", "Building A", "Building B"]
)

st.sidebar.button("Clear filters")

# -------------------------
# HEADER
# -------------------------
st.title("Executive Summary")
st.caption("Occupancy analysis | Last 6 months (Dec 2024 – May 2025)")

# -------------------------
# KPIs
# -------------------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Avg Daily Occupancy", f"{avg_occupancy:,}", f"{avg_occupancy/total_capacity:.0%} utilization")
col2.metric("Peak Occupancy", f"{peak_occupancy:,}", "Max observed")
col3.metric("P95 Occupancy", f"{p95_occupancy:,}", "95th percentile")
col4.metric("Vacant Desks", f"{vacant_desks:,}")
col5.metric("Unused Space (est.)", f"{unused_space_m2:,} m²")

# -------------------------
# CHARTS ROW 1
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Daily Occupancy Trend")
    fig = px.line(df, x="date", y="occupancy", title="")
    fig.add_hline(y=avg_occupancy, line_dash="dash")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Occupancy by Weekday")
    fig = px.bar(weekday_data, x="Day", y="Occupancy")
    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# CHARTS ROW 2
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Occupancy by Building")
    fig = px.pie(building_data, names="Building", values="Avg Occupancy")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Floor Occupancy Analysis")
    st.dataframe(floor_data, use_container_width=True)

with col3:
    st.subheader("Financial Impact (Estimated)")
    st.write(f"Unused space: **{unused_space_m2:,} m²**")
    st.write(f"Average rent: **${rent_per_m2}/m²**")

    st.success(f"Monthly savings: ${monthly_savings:,.0f}")
    st.success(f"Annual savings: ${annual_savings:,.0f}")

# -------------------------
# RECOMMENDATION
# -------------------------
st.markdown("---")
st.subheader("Recommendation")

st.info(
    "Based on the last 6 months of analysis, it is recommended to consolidate occupancy "
    "into higher-demand floors and negotiate returning approximately "
    f"{unused_space_m2:,} m² (19% of leased space), enabling estimated savings of "
    f"${annual_savings:,.0f} annually in rental costs."
)
