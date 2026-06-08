import unittest
import sys
# Sense aquesta línia no em funcionava, tinc els imports sense 'src'
sys.path.append("src")
# Així es pot executar el test des de l'arrel, no podia anteriorment
# Importem la funció de la càrrega de dades
from exercises.exercise1 import load_and_eda
# Importem la funció del test de l'exercici 6
from exercises.exercise6 import fun_total_goals

# Definim la classe pel test, tal i com tenim al notebook de la Unit 6
class TestsExercise6(unittest.TestCase):
    """
    Test for exercise 6.
    """
    # Definim la funció del test de fun_total_goals
    def test_fun_total_goals(self):
        """
        Goals calculation test.
        """
        # Càrrega de dades per provar el test
        data = load_and_eda("data/LaLiga_Matches.csv")
        # Cridem a la funció fun_total_goals, com tenim definida a l'exercici 6
        home_goals, away_goals, total_goals = fun_total_goals(data)
        # Fem les comprovacions amb els valors obtinguts i els valors esperats
        self.assertEqual(home_goals, 18040)
        self.assertEqual(away_goals, 13053)
        self.assertEqual(total_goals, 31093)
        # L'inconvenient que veig és que per pantalla, quan executo el test,
        # m'apareixen els 'print' de l'exercici 1, no sé si hauria d'haver fet,
        # un dataframe fictici de provar manualment per no cridar la funció
        # load_and_eda de l'exercici 1.

# Comprovació del test per la terminal, si comencen per test_ realitza el unittest
if __name__ == "__main__":
    unittest.main()