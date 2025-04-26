import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import set_background, show_title_image, get_translator

def app():
    # === Setup ===
    st.set_page_config(page_title="Stock Availability", layout="wide")
    set_background()
    lang_toggle = st.sidebar.checkbox("Switch to Tamil")
    t = get_translator(lang_toggle)

    show_title_image()
    st.header(t("Real-Time Stock"))

    # === Stock Availability Section ===
    shop = st.selectbox(t("Select Shop"), [
        "Shop 101 - Chennai", 
        "Shop 102 - Madurai", 
        "Shop 103 - Coimbatore"
    ])

    # Dummy stock data
    stock_data = {
        "Shop 101 - Chennai": {"Rice": 100, "Sugar": 40, "Wheat": 0},
        "Shop 102 - Madurai": {"Rice": 80, "Sugar": 75, "Wheat": 60},
        "Shop 103 - Coimbatore": {"Rice": 30, "Sugar": 60, "Wheat": 90},
    }

    df = pd.DataFrame(stock_data[shop].items(), columns=["Item", "Quantity"])

    # === Bar Chart for Stock ===
    fig, ax = plt.subplots()
    ax.bar(df["Item"], df["Quantity"], color=['orange', 'green', 'blue'])
    ax.set_title(t("Current Stock Levels"))
    ax.set_ylabel(t("Quantity"))
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
