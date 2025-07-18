import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import get_translator

import firebase_admin
from firebase_admin import credentials, db
from utils import set_background, get_translator

# Initialize Firebase (same as before)
if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": st.secrets.FIREBASE.type,
        "project_id": st.secrets.FIREBASE.project_id,
        "private_key_id": st.secrets.FIREBASE.private_key_id,
        "private_key": st.secrets.FIREBASE.private_key.replace("\\n", "\n"),
        "client_email": st.secrets.FIREBASE.client_email,
        "client_id": st.secrets.FIREBASE.client_id,
        "auth_uri": st.secrets.FIREBASE.auth_uri,
        "token_uri": st.secrets.FIREBASE.token_uri,
        "auth_provider_x509_cert_url": st.secrets.FIREBASE.auth_provider_x509_cert_url,
        "client_x509_cert_url": st.secrets.FIREBASE.client_x509_cert_url
    })
    firebase_admin.initialize_app(cred, {
        'databaseURL': st.secrets.FIREBASE.databaseURL
    })

def app(lang_toggle):
    t = get_translator(lang_toggle)
    
    ref = db.reference("/")  # Get all users
    data = ref.get()

# Initialize stock for each shop
    shop_levels = {
       "101": 0,
       "102": 0,
       "103": 0
   }

    for user_id, user_data in data.items():
     shop = str(user_data.get("Shop"))
     level = user_data.get("level")
    
     if shop in shop_levels and level is not None:
        try:
            shop_levels[shop] += int(level)
        except ValueError:
            pass  # Skip if level is not an integer

    st.title("📦Realtime stock monitoring")
    
    
    # === Stock Availability Section ===
    shop = st.selectbox(t("Select Shop"), [
        t("Shop 101 - Chennai"), 
        t("Shop 102 - Madurai"), 
        t("Shop 103 - Coimbatore")
    ])
    try:
     level = int(level)
    except (ValueError, TypeError):
     level = 0

    
    # Dummy stock data
    stock_data = {
    t("Shop 101 - Chennai"): {"Rice": shop_levels["101"], "Sugar": 0, "Wheat": 0},
    t("Shop 102 - Madurai"): {"Rice": shop_levels["102"], "Sugar": 0, "Wheat": 0},
    t("Shop 103 - Coimbatore"): {"Rice": shop_levels["103"], "Sugar": 0, "Wheat": 0},
}


    if shop in stock_data:
        df = pd.DataFrame(stock_data[shop].items(), columns=[t("Item"), t("Quantity")])

# Convert Item to string and Quantity to numeric to avoid matplotlib TypeError
        df[t("Item")] = df[t("Item")].astype(str)
        df[t("Quantity")] = pd.to_numeric(df[t("Quantity")], errors='coerce').fillna(0)

# Bar chart
        fig, ax = plt.subplots()
        ax.bar(df[t("Item")], df[t("Quantity")], color=['orange', 'green', 'blue'])

        # Debugging the translation of axis labels and title
        translated_title = t("Current Stock Levels")
        translated_ylabel = t("Quantity")
        translated_xlabel = t("Item")

        print(f"Translated title: {translated_title}")
        print(f"Translated ylabel: {translated_ylabel}")
        print(f"Translated xlabel: {translated_xlabel}")

        # Apply the translated strings to the plot
        ax.set_title(translated_title)  # Ensure translation is applied here
        ax.set_ylabel(translated_ylabel)  # Ensure translation is applied here
        ax.set_xlabel(translated_xlabel)  # Ensure translation is applied here if needed

        st.pyplot(fig)
    else:
        st.error(f"{t('Selected shop data not available!')}")

    # === Map Display ===
    shop_map_urls = {
        t("Shop 101 - Chennai"): "https://www.google.com/maps?q=13.0827,80.2707&z=15&output=embed",
        t("Shop 102 - Madurai"): "https://www.google.com/maps?q=9.9252,78.1198&z=15&output=embed",
        t("Shop 103 - Coimbatore"): "https://www.google.com/maps?q=11.0168,76.9558&z=15&output=embed",
    }

    st.markdown(f"""
    <iframe width="100%" height="300" frameborder="0" style="border:0"
    src="{shop_map_urls[shop]}" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
