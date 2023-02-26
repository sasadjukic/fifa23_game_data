

import unittest 
import pandas as pd
import numpy as np
from data import get_clean_data 
from clubs_expiring_contracts import get_top_expiring_contracts
from clubs_most_experienced import get_teams_average_age, create_pandas_series
from clubs_roster_values import find_average_club_values

class CleanData(unittest.TestCase):

    def test_1_get_clean_data(self):

        fifa_23 = get_clean_data()

        # check if we indeed dropped all non-numbers from original data
        self.assertTrue(type(fifa_23['jersey'].mean()), np.float64)

        # assert that our most common jersey number is indeed 7
        self.assertEqual(int(fifa_23['jersey'].mode()), 7)

class ExpiringContracts(unittest.TestCase):

    def test_1_get_top_expiring_contracts(self):

        fake_contracts = {
            'Real Madrid' : 11,
            'Barcelona' : 12,
            'Manchester United' : 7,
            'Liverpool' : 6,
            'Inter' : 13,
            'Borussia Dortmund' : 14,
            'Juventus' : 3,
            'Bayern Munchen' : 5
        }

        top_five = get_top_expiring_contracts(fake_contracts)

        # check if our pandas Series indeed returns top 5 contracts
        self.assertEqual(len(top_five.index.tolist()), 5)

        # check if we get a correct 'Pandas Series Index' return on our fake contracts input 
        self.assertEqual(
                        top_five.index.tolist(), 
                        ['Borussia Dortmund', 'Inter', 'Barcelona', 'Real Madrid', 'Manchester United']
                        )

        # check if we get a correct 'Pandas Series Values' return on our fake contract input
        self.assertEqual(
                        top_five.values.tolist(),
                        [14, 13, 12, 11, 7]
                        )

class MostExperiencedTeams(unittest.TestCase):

    def test_1_create_pd_series_from_avg_age(self):

        fake_age = {
            'Valencia' : 22.34,
            'Tottenham' : 29.56,
            'Arsenal' : 30.07,
            'Napoli' : 30.34,
            'Torino' : 27.45,
            'Lille' : 24.56,
            'Sevilla' : 25.78,
            'Werder' : 24.67,
            'Mainz' : 25.67,
            'Montpellier' : 28.78,
            'Udinese' : 31.45
        }

        avg_age = create_pandas_series(fake_age)

        # check if we get a correct 'Pandas Series Index' return on our fake age input
        self.assertEqual(
                         avg_age.index.tolist(),
                         [
                          'Udinese', 'Napoli', 'Arsenal', 'Tottenham', 'Montpellier',
                          'Torino', 'Sevilla', 'Mainz', 'Werder', 'Lille'
                         ]    
                        )

        # check if we get a correct 'Pandas Series Values' return on our fake age input
        self.assertEqual(
                         avg_age.values.tolist(),
                         [
                          31.45, 30.34, 30.07, 29.56, 28.78, 
                          27.45, 25.78, 25.67, 24.67, 24.56
                         ]
                        )

class RosterValues(unittest.TestCase):

    def test_1_find_avg_roster_values(self):

        fake_team_values = {
            'Inter' : 5_000_000,
            'Mainz' : 10_000_000,
            'FC Porto' : 23_000_000
        }

        # test average roster value (in millions)
        self.assertEqual(find_average_club_values(fake_team_values), 13)

if __name__ == '__main__':
    unittest.main()