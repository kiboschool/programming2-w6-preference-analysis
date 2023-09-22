import unittest

from gradescope_utils.autograder_utils.decorators import weight
from main import *

class TestMealPreference(unittest.TestCase):

    @weight(1)
    def test_create_meal_scores(self):
        preferences = {
            'person1': {'a', 'b', 'c'},
            'person2': {'a', 'b', 'd'},
            'person3': {'a', 'd', 'c'},
            'person4': {'c', 'z', 'x'},
        }

        result = create_meal_frequencies(preferences)
        
        assert result.get('a') == 3 
        assert result.get('b') == 2      
        assert result.get('c') == 3      
        assert result.get('d') == 2      
        assert result.get('z') == 1      
        assert result.get('x') == 1      

        assert len(result) == 6

    @weight(2)
    def test_score_users(self):
        preferences = {
            'person1': {'a', 'b', 'c'},
            'person2': {'a', 'b', 'd'},
            'person3': {'a', 'd', 'c'},
            'person4': {'c', 'z', 'x'},
        }

        frequencies = create_meal_frequencies(preferences)

        scores = create_user_scores(preferences, frequencies)

        assert scores.keys() == preferences.keys()
        assert scores.get('person1') == 8
        assert scores.get('person2') == 7
        assert scores.get('person3') == 8
        assert scores.get('person4') == 5

    @weight(2)
    def test_find_users_with_lowest_score(self):
        user_scores = {
            'person1': 5,
            'person2': 8,
            'person3': 7,
            'person4': 5
        }

        result = find_users_with_lowest_score(user_scores)
        assert len(result) == 2
        assert 'person1' in result
        assert 'person4' in result

if __name__ == '__main__':
    unittest.main()