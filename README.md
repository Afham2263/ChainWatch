#  ChainWatch: Real-Time Crypto Dashboard

**ChainWatch** is a sleek and responsive crypto market dashboard built with Python and Streamlit. It pulls live data from the CoinGecko API, transforms it into a clean format, visualizes key metrics, and offers a one-click Excel export for offline analysis.

---
## 🔗 Live Demo

You can access the fully deployed version of ChainWatch here:

👉 [https://chain-watch.streamlit.app/](https://chain-watch.streamlit.app/)

No setup needed — just open the link in your browser. The dashboard displays:

- Real-time cryptocurrency prices
- Percentage change over 24 hours
- Market cap and volume data
- Automatically refreshes data on reload

This demo is hosted on Streamlit Cloud and continuously pulls data from the CoinGecko API to ensure up-to-date market insights.

Feel free to explore, analyze, and share feedback.

##  Features

-  **Live Data Extraction** – Get real-time crypto prices using CoinGecko API
-  **Top 10 Cryptocurrencies** – Track price, market cap, 24h volume & change
-  **Interactive Charts** – Bar chart for price, line chart for 24h change
-  **Currency Conversion** – Prices shown in both USD and INR
-  **Excel Export** – Download the data with one click
-  **Dark Themed UI** – Built-in custom styling for that sleek aesthetic
-  **Streamlit App** – Lightweight, fast, and responsive

---

##  Technologies Used

- **Python 3.10**
- **Streamlit** for UI
- **Pandas** for data transformation
- **Requests** for API interaction
- **OpenPyXL** for Excel export

---

##  Installation & Setup

###  Clone the Repository
```bash
git clone https://github.com/Afham2263/ChainWatch.git
cd ChainWatch
```

###  Install Dependencies
```bash
pip install -r requirements.txt
```

###  Run the Dashboard
```bash
streamlit run dashboard.py
```
Then visit `http://localhost:8501` in your browser.

---

##  requirements.txt
```txt
streamlit
pandas
openpyxl
requests
```


---

##  Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

---

##  Author
**Mohd Afham**  
GitHub: [Afham2263](https://github.com/Afham2263)  
LinkedIn: [in/Afham22](https://linkedin.com/in/Afham22)

---

##  License
This project is licensed under the MIT License — feel free to use, fork, and star it!

