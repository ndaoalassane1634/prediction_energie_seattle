# app.py
import pandas as pd
import streamlit as st
from pages.data_analysis import show_data_analysis
from pages.predictioncopy import show_prediction_page
from scripts.data_cleaning import clean_data
import warnings

# Désactiver les avertissements
warnings.filterwarnings('ignore')

# ✅ Appeler `st.set_page_config()` en premier
st.set_page_config(layout='wide')

# Affichage du logo et titre
logo_path = './assets/logo_en.PNG'
st.image(logo_path, width=100)
st.subheader("Tableau de bord d'analyse énergétique")

# Sélection du menu latéral
selected_tab = st.sidebar.selectbox(
    "Sélectionner une option :",
    ["Accueil", "Analyse des données", "Prédictions"]
)

# Chargement des données
def load_data():
    data_file = 'data/data.csv'
    df=pd.read_csv(data_file)
    df = clean_data(df)
    return df

df = load_data()

# Gestion des pages
if selected_tab == "Accueil":
    st.subheader("Agilité, Précision et Profits")
    st.write("Sélectionnez une option dans la barre latérale.")
elif selected_tab == "Analyse des données":
    show_data_analysis()
elif selected_tab == "Prédictions":
    show_prediction_page()
