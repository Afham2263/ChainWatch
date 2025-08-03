import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO
from extract import extract_coin_data
from transform import transform_data

# ---------------------- Streamlit Config ---------------------- #
st.set_page_config(
    page_title="Crypto Market Tracker 💰",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------- Styling ---------------------- #
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #cfcfcf;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00c0f2;
    }
    .block-container {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Title ---------------------- #
st.markdown("""
    <h1 style='text-align: center;'> Crypto Market Dashboard </h1>
    <hr style='border: 1px solid #333;'>
""", unsafe_allow_html=True)

# ---------------------- Data Pull ---------------------- #
st.markdown("### 🔁 Refresh Dashboard")
refresh = st.button("Refresh Data")

if refresh:
    raw_data = extract_coin_data()
else:
    raw_data = extract_coin_data()

df = transform_data(raw_data)

# Timestamp
st.caption(f"Last updated: {datetime.now().strftime('%d %b %Y | %I:%M %p')}")

# ---------------------- Metrics ---------------------- #
col1, col2, col3 = st.columns(3)
col1.metric(" Bitcoin", f"${df.iloc[0]['Price (USD)']:,}", f"{df.iloc[0]['24h Change (%)']}%")
col2.metric(" Ethereum", f"${df.iloc[1]['Price (USD)']:,}", f"{df.iloc[1]['24h Change (%)']}%")
col3.metric(" Dogecoin", f"${df[df['Symbol'] == 'doge'].iloc[0]['Price (USD)']}", f"{df[df['Symbol'] == 'doge'].iloc[0]['24h Change (%)']}%")

# ---------------------- Table View ---------------------- #
st.subheader(" Top 10 Cryptocurrencies")
styled_df = df.style.format({
    "Price (USD)": "{:.2f}",
    "Market Cap": "{:,.0f}",
    "24h Volume": "{:,.0f}",
    "24h Change (%)": "{:.2f}",
    "Price (INR)": "{:,.2f}"
}).highlight_max(axis=0)

st.dataframe(styled_df, use_container_width=True)

# ---------------------- Download Excel ---------------------- #
def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='CryptoData')
    output.seek(0)
    return output

excel_data = convert_df_to_excel(df)
st.download_button(
    label="🗃️ Download Excel File",
    data=excel_data,
    file_name="crypto_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ---------------------- Charts ---------------------- #
st.subheader(" Price in USD")
st.bar_chart(df.set_index("Coin")["Price (USD)"])

st.subheader(" 24h Price Change (%)")
st.line_chart(df.set_index("Coin")["24h Change (%)"])

# ---------------------- Footer ---------------------- #
st.markdown("""
    <hr style='border: 1px solid #333;'>
    <p style='text-align: center; color: gray;'>Built by Afham  | Powered by Streamlit & CoinGecko API</p>
""", unsafe_allow_html=True)
