import pandas as pd
import random

# Define synthetic data for ingredient names, quantities, units, and categories
ingredients = ['Chicken', 'Broccoli', 'Rice', 'Tomato', 'Spinach']
quantities = [random.randint(50, 200) for _ in range(len(ingredients))]
units = ['grams', 'ounces', 'cups', 'pieces', 'slices']
categories = ['Proteins', 'Vegetables', 'Grains', 'Fruits', 'Dairy']

# Define synthetic data for recipe data
recipes = ['Chicken Stir-Fry', 'Broccoli Salad', 'Tomato Soup', 'Spinach Smoothie', 'Rice Pilaf']
recipe_categories = ['Dinner', 'Lunch', 'Soup', 'Breakfast', 'Snack']
recipe_difficulty = ['Easy', 'Medium', 'Medium', 'Easy', 'Hard']

# Define synthetic data for nutritional data
calories = [random.randint(100, 500) for _ in range(len(recipes))]
carbohydrates = [random.randint(5, 50) for _ in range(len(recipes))]
proteins = [random.randint(5, 50) for _ in range(len(recipes))]
fats = [random.randint(5, 50) for _ in range(len(recipes))]
vitamins = ['Vitamin A', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K']
minerals = ['Iron', 'Calcium', 'Potassium', 'Magnesium', 'Zinc']

# Define synthetic data for user preferences and restrictions
dietary_preferences = ['Italian Cuisine', 'Spicy Food', 'Low-Carb', 'Vegetarian', 'Gluten-Free']
dietary_restrictions = ['Allergy: Nuts', 'Dairy-Free', 'Low-Sodium', 'Vegan', 'Keto']
health_goals = ['Weight Loss', 'Muscle Gain', 'Maintenance', 'Heart Health', 'Energy Boost']

# Define synthetic data for user feedback data
ratings = [random.randint(1, 5) for _ in range(len(recipes))]
comments = ['Delicious!', 'Needs more seasoning', 'Too salty', 'Great recipe!', 'Easy to make']
ingredient_substitutions = ['Almond milk instead of cow milk', 'Tofu instead of chicken', '', 'No substitutions', '']

# Define synthetic data for miscellaneous data
serving_size = [random.randint(1, 4) for _ in range(len(recipes))]
prep_time = [random.randint(5, 60) for _ in range(len(recipes))]
cook_time = [random.randint(10, 120) for _ in range(len(recipes))]

# Create DataFrame with synthetic data
data = pd.DataFrame({
    'Ingredient': ingredients,
    'Quantity': quantities,
    'Unit': units,
    'Category': categories,
    'Recipe': recipes,
    'Recipe Category': recipe_categories,
    'Recipe Difficulty': recipe_difficulty,
    'Calories': calories,
    'Carbohydrates': carbohydrates,
    'Proteins': proteins,
    'Fats': fats,
    'Vitamins': vitamins,
    'Minerals': minerals,
    'Dietary Preferences': dietary_preferences,
    'Dietary Restrictions': dietary_restrictions,
    'Health Goals': health_goals,
    'Rating': ratings,
    'Comments': comments,
    'Ingredient Substitutions': ingredient_substitutions,
    'Serving Size': serving_size,
    'Prep Time (mins)': prep_time,
    'Cook Time (mins)': cook_time
})

# Save DataFrame to CSV file
data.to_csv('synthetic_nourishnudge_data.csv', index=False)
