import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

# ============================
# Load Data
# ============================
df = pd.read_excel("EUt.xlsx")

# ============================
# Dashboard Title
# ============================
st.title("EUt+ / h_da Dashboard")

# ============================
# KPIs (3 columns)
# ============================
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Gesamtzahl Beteiligte")
    total = len(df)
    fig, ax = plt.subplots(figsize=(4,3))
    ax.text(0.5, 0.5, f"{total:,}", fontsize=50, ha='center', va='center', color="#0A3D91")
    ax.axis("off")
    st.pyplot(fig)

with col2:
    st.subheader("Accelerate Teilnehmende")
    accelerate_count = (df["Accelerate  Beteiligung"].astype(str).str.lower() == "ja").sum()
    fig, ax = plt.subplots(figsize=(4,3))
    ax.text(0.5, 0.5, f"{accelerate_count:,}", fontsize=50, ha='center', va='center', color="#0A3D91")
    ax.axis("off")
    st.pyplot(fig)

with col3:
    st.subheader("Anzahl Cluster")
    cluster_count = df["Cluster"].nunique()
    fig, ax = plt.subplots(figsize=(4,3))
    ax.text(0.5, 0.5, f"{cluster_count}", fontsize=50, ha='center', va='center', color="#0A3D91")
    ax.axis("off")
    st.pyplot(fig)

# ============================
# Accelerate & Gender (2 columns)
# ============================
col4, col5 = st.columns(2)

with col4:
    st.subheader("Accelerate Beteiligung")
    counts = df["Accelerate  Beteiligung"].value_counts()
    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90, colors=["#0A3D91", "#6EC6FF"])
    st.pyplot(fig)

with col5:
    st.subheader("Gender Beteiligung")
    counts_gender = df["Gender"].value_counts()
    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(counts_gender, labels=counts_gender.index, autopct="%1.1f%%", startangle=90, colors=["#0A3D91", "#6EC6FF"])
    st.pyplot(fig)

# ============================
# Einrichtung & Zielgruppe (2 columns)
# ============================
col6, col7 = st.columns(2)

with col6:
    st.subheader("Beteiligung pro Einrichtung (≥3)")
    counts_Einrichtung = df["h_da Einrichtung"].value_counts()
    counts_2 = counts_Einrichtung[counts_Einrichtung >= 3].sort_values(ascending=True)
    fig, ax = plt.subplots(figsize=(8,6))
    ax.barh(counts_2.index, counts_2.values, color="#6EC6FF")
    ax.set_xlabel("Anzahl Personen")
    st.pyplot(fig)

with col7:
    st.subheader("Stakeholder")
    counts_Ziel = df["Zielgruppe"].value_counts()
    fig, ax = plt.subplots(figsize=(8,6))
    ax.bar(counts_Ziel.index, counts_Ziel.values, color="#0A3D91")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

# ============================
# Cluster Donut (full width)
# ============================
st.subheader("EUt+/h_da Cluster Beteiligung")

cluster_counts = df["Cluster"].value_counts()
total = cluster_counts.sum()

fig_cluster, ax = plt.subplots(figsize=(8,8))

# Donut
wedges, _ = ax.pie(
    cluster_counts,
    startangle=90,
    wedgeprops={"width": 0.4},
    labels=None
)

# Zahlen im Ring
angles = np.cumsum(cluster_counts) - cluster_counts / 2
r = 0.7

for angle, value in zip(angles, cluster_counts):
    x = r * np.cos(np.deg2rad(angle))
    y = r * np.sin(np.deg2rad(angle))
    ax.text(x, y, str(value), ha='center', va='center', fontsize=14, fontweight='bold')

# Legende mit Prozent
legend_labels = [
    f"{cluster} ({count/total*100:.1f}%)"
    for cluster, count in cluster_counts.items()
]

ax.legend(
    wedges,
    legend_labels,
    title="Cluster",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

ax.axis("equal")
st.pyplot(fig_cluster)
