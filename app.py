
# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Asset Management", layout="wide")

st.title("Overview - Asset & Kegiatan Safety")

# --- CONFIG: ganti dengan ID sheet dan sheet name ---
SHEET_ID = "1R1UYHVGMFNNWaalVO5RQwVJbMPYigr23Pl6R9A4-VrE"
SHEET_NAME = "2025"  # ganti sesuai nama tab di sheetmu

csv_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={TES PRAKTIK ALL BU 2025}"

@st.cache_data(ttl=60)
def load_data(url):
    return pd.read_csv(url)

try:
    df = load_data(csv_url)
    st.write("Data preview")
    st.dataframe(df.head(50))
    # contoh ringkasan
    if 'BU' in df.columns:
        st.subheader("Count per BU")
        st.bar_chart(df['BU'].value_counts())
except Exception as e:
    st.error("Gagal load data. Pastikan Google Sheet bisa diakses publik atau gunakan service account.")
    st.exception(e)
