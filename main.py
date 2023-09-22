from collections import Counter

def create_meal_frequencies(preferences):
    meal_frequencies = Counter()
    for preference_set in preferences.values():
        meal_frequencies.update(preference_set)

    return meal_frequencies

def score_meals(meals, meal_score):
    result = 0
    for meal in meals:
        result += meal_score.get(meal)
    return result

def create_user_scores(preferences, meal_score):
    return {user: score_meals(user_meals, meal_score) for user, user_meals in preferences.items()}

def find_users_with_lowest_score(user_score):
    val = min(user_score.values())
    return [user for user, value in user_score.items() if value == val]


if __name__ == '__main__':
    preferences = {
        'a': {'pizza', 'goat meat', 'shortbread', 'tea'},
        'b': {'pizza', 'shrimp', 'tea'},
        'c': {'pizza', 'tea'},
    }


    meal_score = create_meal_frequencies(preferences)
    print(f'{meal_score}')
    user_score = create_user_scores(preferences, meal_score)
    print(f'{user_score}')

    print(find_users_with_lowest_score(user_score))