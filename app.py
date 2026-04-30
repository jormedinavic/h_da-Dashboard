
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_excel('EUt.xlsx')

# =========================================================
# ROW 1 — KPIs (kompakt)
# =========================================================
col1, col2 = st.columns([1,1])

with col1:
    st.subheader("Gesamtzahl Beteiligte h-da")
    total = len(df)
    fig5, ax5 = plt.subplots(figsize=(2.0, 1.4), dpi=60)
    ax5.text(0.5, 0.5, f"{total:,}", fontsize=22, ha='center', va='center', color="#0A3D91")
    ax5.axis("off")
    st.pyplot(fig5, use_container_width=False)

with col2:
    st.subheader("Accelerate Teilnehmende")
    accelerate_count = (df["Accelerate  Beteiligung"].astype(str).str.lower() == "ja").sum()
    fig6, ax6 = plt.subplots(figsize=(2.0, 1.4), dpi=60)
    ax6.text(0.5, 0.5, f"{accelerate_count:,}", fontsize=22, ha='center', va='center', color="#0A3D91")
    ax6.axis("off")
    st.pyplot(fig6, use_container_width=False)

# =========================================================
# ROW 2 — PIE CHARTS (kompakt)
# =========================================================
p1, p2 = st.columns([1,1])

with p1:
    st.subheader("h_da Accelerate Teilnehmende")
    counts = df["Accelerate  Beteiligung"].value_counts()
    fig1, ax1 = plt.subplots(figsize=(2.6, 2.6), dpi=60)
    ax1.pie(counts, labels=counts.index, autopct="%1.0f%%", startangle=90,
            colors=["#0A3D91", "#6EC6FF"])
    ax1.axis("equal")
    st.pyplot(fig1, use_container_width=False)

with p2:
    st.subheader("Gender Beteiligung")
    counts_gender = df["Gender"].value_counts()
    fig2, ax2 = plt.subplots(figsize=(2.6, 2.6), dpi=60)
    ax2.pie(counts_gender, labels=counts_gender.index, autopct="%1.0f%%", startangle=90,
            colors=["#0A3D91", "#6EC6FF"])
    ax2.axis("equal")
    st.pyplot(fig2, use_container_width=False)

# =========================================================
# ROW 3 — BALKEN (kompakt)
# =========================================================
b1, b2 = st.columns([1,1])

with b1:
    st.subheader("Einrichtungen h_da")
    counts_Einrichtung = df["h_da Einrichtung"].value_counts()
    counts_2 = counts_Einrichtung[counts_Einrichtung >= 3].sort_values(ascending=True)
    fig4, ax4 = plt.subplots(figsize=(3.0, 2.4), dpi=60)
    ax4.barh(counts_2.index, counts_2.values, color="#6EC6FF")
    ax4.set_xlabel("Anzahl Personen")
    ax4.tick_params(axis='y', labelsize=7)
    ax4.tick_params(axis='x', labelsize=7)
    
    st.pyplot(fig4, use_container_width=False)







with b2:
    st.subheader("Stakeholder")
    counts_Ziel = df["Zielgruppe"].value_counts()
    fig5b, ax5b = plt.subplots(figsize=(3.0, 2.4), dpi=60)
    ax5b.bar(counts_Ziel.index, counts_Ziel.values, color="#0A3D91")
    #plt.xticks(rotation=45, ha="right")

    ax5b.tick_params(axis='x', labelsize=7, rotation=45)
    ax5b.tick_params(axis='y', labelsize=7)
    st.pyplot(fig5b, use_container_width=False)

# =========================================================
# ROW 4 — CLUSTER DONUT (kompakt)
# =========================================================
i1, i2 = st.columns([1,1])

with i1:
    st.subheader("EUt+/h_da Clusters")
    cluster_counts = df["Cluster"].value_counts()
    fig_cluster, axc = plt.subplots(figsize=(2.8, 2.8), dpi=60)
    wedges, texts = axc.pie(cluster_counts, startangle=90, wedgeprops={"width": 0.35})
    axc.axis("equal")
    axc.legend(
        wedges,
        [f"{cluster}: {count}" for cluster, count in cluster_counts.items()],
        title="Cluster & Teilnehmende",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )
    st.pyplot(fig_cluster, use_container_width=False)
