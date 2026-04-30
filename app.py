
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_excel("EUt.xlsx")
df.columns = df.columns.str.strip()

st.title("EUt+ / h_da Dashboard")

# KPIs
k1, k2, k3 = st.columns(3)

with k1:
    st.subheader("Gesamtzahl Beteiligte")
    total = len(df)
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, str(total), fontsize=40, ha="center", va="center")
    ax.axis("off")
    st.pyplot(fig)

with k2:
    st.subheader("Accelerate Teilnehmende")
    accelerate_count = (df["Accelerate  Beteiligung"].astype(str).str.lower() == "ja").sum()
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, str(accelerate_count), fontsize=40, ha="center", va="center")
    ax.axis("off")
    st.pyplot(fig)

with k3:
    st.subheader("Anzahl Cluster")
    cluster_count = df["Cluster"].nunique()
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, str(cluster_count), fontsize=40, ha="center", va="center")
    ax.axis("off")
    st.pyplot(fig)

# PIE-ROW
p1, p2, p3 = st.columns(3)

with p1:
    st.subheader("Accelerate Beteiligung")
    counts_acc = df["Accelerate  Beteiligung"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(counts_acc.values, labels=counts_acc.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

with p2:
    st.subheader("Gender Beteiligung")
    counts_gender = df["Gender"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(counts_gender.values, labels=counts_gender.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

with p3:
    st.subheader("Cluster Donut")
    cluster_counts = df["Cluster"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(cluster_counts.values, labels=cluster_counts.index, startangle=90, wedgeprops={"width": 0.4})
    ax.axis("equal")
    st.pyplot(fig)

# Balken
st.subheader("Beteiligung pro Einrichtung")
counts_einr = df["h_da Einrichtung"].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(counts_einr.index, counts_einr.values)
st.pyplot(fig)
