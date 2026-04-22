




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('EUt.xlsx')

#df = df.drop(columns=["Name", "Item"])

#df.columns = df.columns.str.replace("\n", " ", regex=False)

# Dashboard Title
# -----------------------------
st.title("📊 Beteiligungs-Dashboard (Matplotlib Version)")


# =========================================================
# 5) KPI: Gesamtzahl Beteiligte
# =========================================================
st.subheader("Gesamtzahl Beteiligte h-da")

total = len(df)

fig5, ax5 = plt.subplots(figsize=(6,4))
ax5.text(0.5, 0.5, f"{total:,}", fontsize=60, ha='center', va='center', color="#0A3D91")
#ax5.text(0.5, 0.2, "h_da Teilnehmende Insgesamt", fontsize=18, ha='center', va='center')
ax5.axis("off")
st.pyplot(fig5)

# =========================================================
# 6) KPI: Accelerate Teilnehmende
# =========================================================
st.subheader("Accelerate Teilnehmende")

accelerate_count = (df["Accelerate  Beteiligung"].astype(str).str.lower() == "ja").sum()

fig6, ax6 = plt.subplots(figsize=(6,4))
ax6.text(0.5, 0.5, f"{accelerate_count:,}", fontsize=60, ha='center', va='center', color="#0A3D91")
#ax6.text(0.5, 0.2, "Accelerate Teilnehmende", fontsize=18, ha='center', va='center')
ax6.axis("off")
st.pyplot(fig6)


# =========================================================
# 1) PIE: Accelerate Beteiligung
# =========================================================
st.subheader("h_da Accelerate Teilnehmende")

counts = df["Accelerate  Beteiligung"].value_counts()

fig1, ax1 = plt.subplots(figsize=(6,6))
ax1.pie(
    counts,
    labels=counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#0A3D91", "#6EC6FF"]
)
#ax1.set_title("Accelerate Beteiligung")
st.pyplot(fig1)

# =========================================================
# 2) PIE: Gender
# =========================================================
st.subheader("Gender Beteiligung")

counts_gender = df["Gender"].value_counts()

fig2, ax2 = plt.subplots(figsize=(6,6))
ax2.pie(
    counts_gender,
    labels=counts_gender.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#0A3D91", "#6EC6FF"]
)
#ax2.set_title("Gender")
st.pyplot(fig2)

# =========================================================
# 3) BAR: Einrichtung (>= 3)
# =========================================================
st.subheader("Beteiligung pro Einrichtung")

counts_Einrichtung = df["h_da Einrichtung"].value_counts()
counts_2 = counts_Einrichtung[counts_Einrichtung >= 3]
counts_2 = counts_2.sort_values(ascending=True)

fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.barh(counts_2.index, counts_2.values, color="#6EC6FF")
ax3.set_xlabel("Anzahl Personen")
#ax3.set_title("Beteiligung pro Einrichtung")
st.pyplot(fig3)

# =========================================================
# 4) BAR: Zielgruppe
# =========================================================
st.subheader("Steakholder")

counts_Ziel = df["Zielgruppe"].value_counts()

fig4, ax4 = plt.subplots(figsize=(10, 6))
ax4.bar(counts_Ziel.index, counts_Ziel.values, color="#0A3D91")
#ax4.set_title("Personen pro Zielgruppe")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig4)


