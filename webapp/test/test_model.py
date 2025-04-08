import pytest
import numpy as np
import pandas as pd
import joblib
from pages.predictioncopy import load_model, predict, calculate_metrics

# Test 1 : Vérifier que le modèle se charge correctement
def test_load_model():
    model = load_model()
    assert model is not None, "Le modèle ne s'est pas chargé correctement"
    assert hasattr(model, "predict"), "Le modèle n'a pas de méthode 'predict'"

# Test 2 : Vérifier le fonctionnement de la prédiction

def test_predict():
    model = load_model()
    expected_columns = [
        'YearBuilt', 'NumberofBuildings', 'NumberofFloors', 'PropertyGFATotal',
        'GFAPerBuilding', 'GFAPerFloor', 'GFABuildingRate', 'LargestPropertyUseTypeGFA',
        'GFAParkingRate', 'Distance_from_SeattleKM',
        'BuildingType', 'Neighborhood', 'LargestPropertyUseType'
    ]

    X_sample = pd.DataFrame([[
        2005, 1, 3, 5000, 2500, 1250, 0.5, 3000, 0.2, 4,
        'NonResidential', 'Downtown', 'Office'
    ]], columns=expected_columns)

    prediction = predict(model, X_sample)
    assert prediction.shape == (1,)
    assert isinstance(prediction[0], (float, np.float32, np.float64))

# Test 3 : Vérifier la cohérence des métriques


def test_calculate_metrics():
    y_true = np.array([3.2, 4.5, 5.1])
    y_pred = np.array([3.1, 4.4, 5.0])
    rmse, mae, r2 = calculate_metrics(y_true, y_pred)

    assert rmse > 0, "RMSE doit être positif"
    assert mae > 0, "MAE doit être positif"
    assert -1 <= r2 <= 1, "R² doit être entre -1 et 1"
