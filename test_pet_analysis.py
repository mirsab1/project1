import unittest
import pandas as pd
import pet_analysis as pa

class TestPetAnalysisFunctions(unittest.TestCase):

    # Load test data once for all tests
    @classmethod
    def setUpClass(cls):
        cls.test_df = pd.read_csv('pets.csv')
        cls.test_df = pa.clean_data(cls.test_df)

    def test_calculate_average_price(self):
        avg_price_dog = pa.calculate_average_price(self.test_df, 'Dog')
        self.assertAlmostEqual(avg_price_dog, 82.20, places=2)  # Adjust based on your expected values

    def test_find_pets_with_feature(self):
        pets_with_feature = pa.find_pets_with_feature(self.test_df, 'Foxhound')
        self.assertIn('Ginger', pets_with_feature)

    def test_get_species_statistics(self):
        species_stats = pa.get_species_statistics(self.test_df)
        self.assertEqual(len(species_stats), 7)  # Assuming there are 4 species in the dataset

if __name__ == '__main__':
    unittest.main()

