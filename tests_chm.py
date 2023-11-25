#!Python3
#Tests the Chess capture map

import unittest
from unittest import result
import chm_function

class case_getGamesFromLichess(unittest.TestCase):
    '''Tests for getting chess games from Lichess.org'''
    
    def test_get_games_connection(self):
        '''Gets account tomasquinones and returns an object'''
        status = chm_function.getGamesFromLichess('tomasquinones')
        self.assertEqual(status.status_code, 200)

    def test_bad_user(self):
        '''Tests that an invalid account does not return an object'''
        status = chm_function.getGamesFromLichess('senoniuqsamot')
        self.assertNotEqual(status.status_code, 200)


class case_write_games(unittest.TestCase):

    def test_write_games_as_user(self):
        pass


class case_captureFinderTest(unittest.TestCase):
    '''Tests for the regex and returning a list object'''
  
    def setUp(self):
        self.test_data = "6. Bb5+ c6 7. Qg3 cxb5 8. Kd1 Bg4+ 9. Nge2 Bxe2+ 10. Ke1 Nxc2+ 11. Kxe2 Nxa1"
        
    def test_returning_list_object(self):
        matches = chm_function.captureFinder(self.test_data)
        self.assertIsInstance(matches, list)

    def test_matches(self):
        expected_matches = ['b5', 'e2', 'c2', 'e2', 'a1']
        results = chm_function.captureFinder(self.test_data)
        self.assertListEqual(expected_matches, results)

    def test_no_matches(self):
        results = chm_function.captureFinder('a1 a2 a3 a4 b1 b2 b2 b3 b4 b5 b6')
        self.assertEqual([], results)


class capture_counter_test_case(unittest.TestCase):
    '''Tests the captureCounter function.'''

    def test_returning_dict_object(self):
        test_data = ['b5', 'e2', 'c2', 'e2', 'a1']
        result = chm_function.captureCounter(test_data)
        self.assertIsInstance(result, dict)

    def test_capture_counts(self):
        test_data = ['b5', 'e2', 'c2', 'e2', 'a1']
        result = chm_function.captureCounter(test_data)
        self.assertEqual(result['b5'], 1)
        self.assertEqual(result['e2'], 2)
        self.assertEqual(result['a8'], 0)

if __name__ == '__main__':
    unittest.main()