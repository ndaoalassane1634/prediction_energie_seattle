import pytest
import pandas as pd
from scripts.data_cleaning import clean_data

# 📌 Test 1 : Vérifier que le fichier de données existe et est lisible
def test_load_data():
    df = clean_data("data/data.csv")
    assert isinstance(df, pd.DataFrame), "La sortie doit être un DataFrame Pandas"
    assert not df.empty, "Le DataFrame ne doit pas être vide"

# 📌 Test 2 : Vérifier que certaines colonnes essentielles existent
def test_columns_exist():
    df = clean_data("data/data.csv")
    expected_columns = ["SiteEnergyUse(kBtu)", "Log_SiteEnergyUse", "BuildingType"]
    for col in expected_columns:
        assert col in df.columns, f"La colonne {col} est manquante dans le DataFrame"

# 📌 Test 3 : Vérifier que `Log_SiteEnergyUse` est bien calculée
def test_log_transformation():
    df = clean_data("data/data.csv")
    assert (df["Log_SiteEnergyUse"] > 0).all(), "Toutes les valeurs de Log_SiteEnergyUse doivent être positives"
