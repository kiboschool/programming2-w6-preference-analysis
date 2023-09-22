def create_meal_frequencies(preferences):
    pass

def create_user_scores(preferences, meal_score):
    pass

def find_users_with_lowest_score(user_score):
    pass

if __name__ == '__main__':
    preferences = {
        'a': {'pizza', 'goat meat', 'shortbread'},
        'b': {'pizza', 'shrimp', 'tea'},
        'c': {'pizza', 'nutella', 'dumplings'},
    }


    meal_score = create_meal_frequencies(preferences)
    print(f'{meal_score}')
    user_score = create_user_scores(preferences, meal_score)
    print(f'{user_score}')

    print(find_users_with_lowest_score(user_score))