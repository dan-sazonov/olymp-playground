import unittest

def season(month):

    if month in (12, 1, 2):
        return "зима"
    elif month in (3, 4, 5):
        return "весна"
    elif month in (6, 7, 8):
        return "лето"
    elif month in (9, 10, 11):
        return "осень"

class SeasonTestCase(unittest.TestCase):

    def test_season(self):
        seasons = [None, 'зима', 'зима', 'весна', 'весна', 'весна',
                   'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

        for month in range(1, 13):
            with self.subTest(month=month):
                self.assertEqual(season(month).lower(), seasons[month])



if __name__ == "__main__":
    unittest.main()