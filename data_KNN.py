import pandas as pd
import random

# Increase the number of data points to 25000
num_data_points = 25000
num_data_points_half = 5000
num_data_points_half2 = 2500

# Define synthetic data for ingredient names, quantities, units, and categories
ingredients = ['Chicken', 'Broccoli', 'Rice', 'Tomato', 'Spinach', 'Beef', 'Lettuce', 'Potato', 'Carrot', 'Onion'] * num_data_points_half2
quantities = [random.randint(50, 200) for _ in range(num_data_points)]
units = ['grams', 'ounces', 'cups', 'pieces', 'slices'] * num_data_points_half
categories = ['Proteins', 'Vegetables', 'Grains', 'Fruits', 'Dairy', 'Proteins', 'Vegetables', 'Grains', 'Vegetables', 'Vegetables'] * num_data_points_half2

# Define synthetic data for recipe data
recipes = ['Chicken Stir-Fry', 'Broccoli Salad', 'Tomato Soup', 'Spinach Smoothie', 'Rice Pilaf', 'Beef Stir-Fry', 'Lettuce Wraps', 'Mashed Potatoes', 'Carrot Soup', 'Onion Rings'] * num_data_points_half2
recipe_categories = ['Dinner', 'Lunch', 'Soup', 'Breakfast', 'Snack', 'Dinner', 'Lunch', 'Side Dish', 'Soup', 'Snack'] * num_data_points_half2
recipe_difficulty = ['Easy', 'Medium', 'Medium', 'Easy', 'Hard', 'Medium', 'Easy', 'Medium', 'Medium', 'Medium'] * num_data_points_half2

# Define synthetic data for nutritional data
calories = [random.randint(100, 500) for _ in range(num_data_points)]
carbohydrates = [random.randint(5, 50) for _ in range(num_data_points)]
proteins = [random.randint(5, 50) for _ in range(num_data_points)]
fats = [random.randint(5, 50) for _ in range(num_data_points)]
vitamins = ['Vitamin A', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K'] * num_data_points_half
minerals = ['Iron', 'Calcium', 'Potassium', 'Magnesium', 'Zinc'] * num_data_points_half

# Define synthetic data for user preferences and restrictions
dietary_preferences = ['Italian Cuisine', 'Spicy Food', 'Low-Carb', 'Vegetarian', 'Gluten-Free'] * num_data_points_half
dietary_restrictions = ['Allergy: Nuts', 'Dairy-Free', 'Low-Sodium', 'Vegan', 'Keto'] * num_data_points_half
health_goals = ['Weight Loss', 'Muscle Gain', 'Maintenance', 'Heart Health', 'Energy Boost'] * num_data_points_half

# Define synthetic data for user feedback data
ratings = [random.randint(1, 5) for _ in range(num_data_points)]
comments = ['Delicious!', 'Needs more seasoning', 'Too salty', 'Great recipe!', 'Easy to make'] * num_data_points_half
ingredient_substitutions = ['Almond milk instead of cow milk', 'Tofu instead of chicken', '', 'No substitutions', ''] * num_data_points_half

# Define synthetic data for miscellaneous data
serving_size = [random.randint(1, 4) for _ in range(num_data_points)]
prep_time = [random.randint(5, 60) for _ in range(num_data_points)]
cook_time = [random.randint(10, 120) for _ in range(num_data_points)]

# Check lengths of arrays
array_lengths = {
    'ingredients': len(ingredients),
    'quantities': len(quantities),
    'units': len(units),
    'categories': len(categories),
    'recipes': len(recipes),
    'recipe_categories': len(recipe_categories),
    'recipe_difficulty': len(recipe_difficulty),
    'calories': len(calories),
    'carbohydrates': len(carbohydrates),
    'proteins': len(proteins),
    'fats': len(fats),
    'vitamins': len(vitamins),
    'minerals': len(minerals),
    'dietary_preferences': len(dietary_preferences),
    'dietary_restrictions': len(dietary_restrictions),
    'health_goals': len(health_goals),
    'ratings': len(ratings),
    'comments': len(comments),
    'ingredient_substitutions': len(ingredient_substitutions),
    'serving_size': len(serving_size),
    'prep_time': len(prep_time),
    'cook_time': len(cook_time)
}

print("Array Lengths:", array_lengths)

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
data.to_csv('synthetic_nourishnudge_data_KNN.csv', index=False)
