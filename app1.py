import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import get_translator

def app(lang_toggle):
    t = get_translator(lang_toggle)
    
    st.header(t("Real-Time Stock"))

    # === Stock Availability Section ===
    shop = st.selectbox(t("Select Shop"), [
        t("Shop 101 - Chennai"), 
        t("Shop 102 - Madurai"), 
        t("Shop 103 - Coimbatore")
    ])

    # Dummy stock data
    stock_data = {
        "Shop 101 - Chennai": {"Rice": 100, "Sugar": 40, "Wheat": 0},
        "Shop 102 - Madurai": {"Rice": 80, "Sugar": 75, "Wheat": 60},
        "Shop 103 - Coimbatore": {"Rice": 30, "Sugar": 60, "Wheat": 90},
    }

    df = pd.DataFrame(stock_data[shop].items(), columns=[t("Item"), t("Quantity")])

    # === Bar Chart ===
    fig, ax = plt.subplots()
    ax.bar(df[t("Item")], df[t("Quantity")], color=['orange', 'green', 'blue'])
    ax.set_title(t("Current Stock Levels"))
    ax.set_ylabel(t("Quantity"))
    ax.set_xlabel(t("Item"))
    st.pyplot(fig)

    # === Map Display ===
    shop_map_urls = {
        "Shop 101 - Chennai": "https://www.google.com/maps?q=13.0827,80.2707&z=15&output=embed",
        "Shop 102 - Madurai": "https://www.google.com/maps?q=9.9252,78.1198&z=15&output=embed",
        "Shop 103 - Coimbatore": "https://www.google.com/maps?q=11.0168,76.9558&z=15&output=embed",
    }

    st.markdown(f"""
    <iframe width="100%" height="300" frameborder="0" style="border:0"
    src="{shop_map_urls[shop]}" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
