# Picky Eaters and Unique Tastes

For this week's assignment, we will manipulate collections to answer some questions about the food tastes of a group of people. We asked them what their preferred meals were, and stored all that information in a dictionary.

The `preferences` dictionary maps a `string` representing a person's name, to a `set` of strings, representing the three meals they like the most.

```python
preferences = {
  "Mehdi": {"Lasagna", "Tagine", "Steak"},
  "Tolu": {"Pepper Soup", "Noodles", "Lasagna"},
  "Stephen": {"Butter Chicken", "Salad", "Noodles"}
}
```

We are curious to know who amongst all our users has the most "unique" taste. Let's think about how to define that:

- For each meal, we will compute how many times that meal shows up in our dictionary
- For each user, we will then attribute a "score" based on how often each of their meals showed up across 
- We will then look for the user(s) with the **lowest** score, meaning their meals showed up the least often throughout our dataset

In order to achieve this we will build three functions using our knowledge of collections and data structures

## Step 1: Meal Counting

There is already a nice hint in the title of this step! Let's think about using a `Counter` object.

Recall that a `Counter` object is a special kind of dictionary, which works very well for counting objects. Counters can take all kinds of inputs:

- Strings, so the counter will count the characters in the string.
- Lists, so the counter will count the elements in the list.
- Sets, so the counter will count the elements in the set.

For example:

```python
from collections import Counter

letters = Counter('Africa')
print(letters) 
# {'a': 2, 'f': 1, 'r': 1, 'i': 1, 'c': 1}

letters.update({'a', 's', 'i'})
print(letters)
# {'a': 3, 'f': 1, 'r': 1, 'i': 2, 'c': 1, 's': 1}
# Note how the counter changed: 's' became a new entry, while 'a' and 'i' were incremented.
```

Armed with this knowledge, and using the `update` method above, complete the `create_meal_frequencies` method. Looping through all the preferences in the provided dictionary, create and return a counter that counts how often each meal appears.

For example, given

```python
preferences = {
	"Mehdi": {"Lasagna", "Tagine", "Steak"},
	"Tolu": {"Pepper Soup", "Noodles", "Lasagna"},
	"Stephen": {"Butter Chicken", "Salad", "Noodles"}
}
```

We want to see:

```python
print(create_meal_frequencies(preferences))

>> {'Lasagna': 2, 'Noodles': 2, 'Tagine': 1, 'Steal': 1, 'Pepper Soup': 1, 'Butter Chicken': 1, 'Salad': 1}
```

Once completed, run test.py: `test_meal_frequencies` should pass.

## Step 2: Creating User Scores

We want to be able to score each of our participants based on the frequencies. For example, Mehdi's score should be 4, because "Lasagna" has a frequency of 2, "Tagine" has a frequency of 1, and "Steak" has a frequency of 1. Their sum adds up to 4.

We can compute the score for Mehdi easily by looping through all the meals in his set of preferences, looking up each meal in our frequency dictionary

You need to repeat this process for all the users!

```python
preferences = {
	"Mehdi": {"Lasagna", "Tagine", "Steak"},
	"Tolu": {"Pepper Soup", "Noodles", "Lasagna"},
	"Stephen": {"Butter Chicken", "Salad", "Noodles"}
}

frequencies = create_meal_frequencies(preferences)

user_scores = create_user_scores(preferences, frequencies)

print(user_scores)
>> {"Mehdi": 4, "Tolu": 5, "Stephen": 4}
```

Once completed, run test.py: `test_score_users` should now be passing.

## Step 3: Finding the Most Unique Preferences

We are getting close to wrapping this up! We now have a dictionary with scores, so all we want is to extract the users that have the lowest scores. We can do this in two steps.

First, how do we find the lowest score? Well the `min()` method of the `Math` library gives us the smallest element of a collection. The collection we care about here is the _list of all values from the users_score dictionary_ For example,

```python
print(user_scores)
>> {"Mehdi": 4, "Tolu": 5, "Stephen": 4}

print(min(user_scores))
>> 4
```

Now that we know the smallest number, let's find all the users that have that number as their value! You should be able to do this with a loop and a condition, or with list comprehensions.

```python
find_users_with_lowest_score(user_score)
>> ["Mehdi", "Stephen"]
```

Note that order doesn't matter here, but you need to make sure to return all the users that share the lowest score.

Once completed, run `test.py`: all tests should now be passing, translating into full marks!
