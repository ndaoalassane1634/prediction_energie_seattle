import pytest

# Exemple d'une fonction simple à tester
def addition(a, b):
    return a + b

# Test unitaire très basique
def test_addition():
    assert addition(2, 3) == 5, "L'addition de 2 et 3 doit être égale à 5"
    assert addition(-1, 1) == 0, "L'addition de -1 et 1 doit être égale à 0"
    assert addition(0, 0) == 0, "L'addition de 0 et 0 doit être égale à 0"

# Exécution du test
if __name__ == "__main__":
    pytest.main()
