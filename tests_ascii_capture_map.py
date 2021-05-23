#!Python3
#Tests the Chess capture map

import unittest
from unittest import result
import acm_function

class GetGamesTestCase(unittest.TestCase):
    '''Tests for getting chess games from Lichess.org'''

    def test_get_games_connection(self):
        status = acm_function.getGamesFromLichess('tomasquinones')
        self.assertEqual(status.status_code, 200)

    def test_bad_user(self):
        status = acm_function.getGamesFromLichess('senoniuqsamot')
        self.assertNotEqual(status.status_code, 200)


class writeGamesTestCase(unittest.TestCase):
    '''Tests for writing games to file'''

    def test_user_file_exists(self):
        pass


class captureFinderTestCase(unittest.TestCase):
    '''Tests for the regex and returning a list object'''
  
    def test_returning_list_object(self):
        test_data = "6. Bb5+ c6 7. Qg3 cxb5 8. Kd1 Bg4+ 9. Nge2 Bxe2+ 10. Ke1 Nxc2+ 11. Kxe2 Nxa1"
        matches = acm_function.captureFinder(test_data)
        self.assertIsInstance(matches, list)

    def test_matches(self):
        test_data = "6. Bb5+ c6 7. Qg3 cxb5 8. Kd1 Bg4+ 9. Nge2 Bxe2+ 10. Ke1 Nxc2+ 11. Kxe2 Nxa1"
        expected_matches = ['b5', 'e2', 'c2', 'e2', 'a1']
        results = acm_function.captureFinder(test_data)
        self.assertListEqual(expected_matches, results)


class capture_counter_test_case(unittest.TestCase):
    '''Tests the captureCounter function.'''

    def test_returning_dict_object(self):
        test_data = ['b5', 'e2', 'c2', 'e2', 'a1']
        result = acm_function.captureCounter(test_data)
        self.assertIsInstance(result, dict)

    def test_capture_counts(self):
        test_data = ['b5', 'e2', 'c2', 'e2', 'a1']
        result = acm_function.captureCounter(test_data)
        self.assertEqual(result['b5'], 1)
        self.assertEqual(result['e2'], 2)
        self.assertEqual(result['a8'], 0)

if __name__ == '__main__':
    unittest.main()