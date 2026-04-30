import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# -----------------------------
# Daten laden
# -----------------------------
df = pd.read_excel("EUt.xlsx")
df.columns = df.columns.str.strip()

# -----------------------------
# Titel
# -----------------------------
st.markdown("<h1 style='text-align:center;'>EUt+ / h_da Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------
# KPI-ROW (3 Spalten)
# -----------------------------
k1, k2, k3 = st.columns(3)

def kpi_box(value, label):
    st.markdown(
        f"""
        <div style="
            background-color:#f0f2f6;
            padding:20px;
            border-radius:10px;
            text-align:center;
            box-shadow:0 0 4px rgba(0,0,0,0.1);
        ">
            <div style="font-size:42px; font-weight:700;">{value}</div>
            <div style="font-size:18px; color:#555;">{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k1:
    kpi_box(len(df), "Gesamtzahl Beteiligte")

with k2:
    accelerate_count = (df["Accelerate  Beteiligung"].astype(str).str.lower() == "ja").sum()
    kpi_box(accelerate_count, "Accelerate Teilnehmende")

with k3:
    zielgruppen_count = df["Zielgruppe"].nunique()
    kpi_box(zielgruppen_count, "Zielgruppen")

st.markdown("---")

# -----------------------------
# PIE-ROW (3 Spalten)
# -----------------------------
p1, p2, p3 = st.columns(3)

with p1:
    st.subheader("Accelerate Beteiligung")
    counts_acc = df["Accelerate  Beteiligung"].value_counts()
    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie(counts_acc.values, labels=counts_acc.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

with p2:
    st.subheader("Gender Beteiligung")
    counts_gender = df["Gender"].value_counts()
    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie(counts_gender.values, labels=counts_gender.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

with p3:
    st.subheader("h_da Einrichtungen")
    einr_counts = df["h_da Einrichtung"].value_counts()
    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie(einr_counts.values, labels=einr_counts.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

st.markdown("---")

# -----------------------------
# BALKEN (volle Breite)
# -----------------------------
st.subheader("Beteiligung pro Einrichtung")
counts_einr = df["h_da Einrichtung"].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(counts_einr.index, counts_einr.values, color="#4a90e2")
ax.set_xlabel("Anzahl")
st.pyplot(fig)
