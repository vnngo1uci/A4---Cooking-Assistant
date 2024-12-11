from flask import Flask, render_template, request, redirect, url_for, jsonify
from recipes import recipes
import calendar
from datetime import datetime
import requests
app = Flask(__name__)

RANDOM_MEAL_URL = "https://www.themealdb.com/api/json/v1/1/random.php"

selected_recipes = []
meal_plan = {}

# Home Route
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recipe_finder', methods=['GET', 'POST'])
def recipe_finder():
    results = []
    if request.method == 'POST': #check if a form was submitted
        user_ingredients = request.form.get('ingredients', '').lower().split(', ')
        filter_option = request.form.get('filter_option')

        for recipe_name, details in recipes.items(): #algorithm for finding all recipes that hve the searched ingredient
            ingredients = details["ingredients"]
            vegan = details["vegan"]
            matching_ingredients = set(user_ingredients) & set(ingredients)

            if matching_ingredients:
                missing_ingredients = set(ingredients) - matching_ingredients #hsow missing ingredients
                if filter_option == "vegan" and not vegan: #Aply the vegan filter if selected by the user
                    continue
                if filter_option == "non_vegan" and vegan:
                    continue

                results.append({
                    "name": recipe_name,
                    "matching": list(matching_ingredients),
                    "missing": list(missing_ingredients),
                    "vegan": vegan,
                })

    return render_template('recipe_finder.html', results=results)

# Save Recipe Route
@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    recipe_name = request.form.get('recipe_name')

    if recipe_name and recipe_name in recipes:
        # Extract ingredients correctly
        ingredients = recipes[recipe_name]["ingredients"]

        # Append the recipe with correct structure
        selected_recipes.append({
            "name": recipe_name,
            "ingredients": ingredients
        })
    
    # Redirect to shopping list after saving
    return redirect(url_for('shopping_list'))


# IMPLEMENTATION OF API STARTS
@app.route('/random_meal')
def random_meal():
    response = requests.get(RANDOM_MEAL_URL)
    meal = None

    if response.status_code == 200: #checks if the API request was successful
        meal_data = response.json().get('meals', [])[0]
        if meal_data: #filter meal data
            meal = { #extracts all of the meal data and formats
                'name': meal_data['strMeal'],
                'category': meal_data['strCategory'],
                'area': meal_data['strArea'],
                'instructions': meal_data['strInstructions'],
                'image': meal_data['strMealThumb'],
                'ingredients': [
                    f"{meal_data[f'strIngredient{i}']} - {meal_data[f'strMeasure{i}']}"
                    for i in range(1, 21)
                    if meal_data[f'strIngredient{i}']
                ]
            }
    return render_template('random_meal.html', meal=meal)

@app.route('/random_meal_api')
def random_meal_api():
    response = requests.get(RANDOM_MEAL_URL) 
    meal_data = response.json().get('meals', [])[0]

    meal = { #store data
        'name': meal_data['strMeal'],
        'category': meal_data['strCategory'],
        'area': meal_data['strArea'],
        'instructions': meal_data['strInstructions'],
        'image': meal_data['strMealThumb'],
        'ingredients': [
            f"{meal_data[f'strIngredient{i}']} - {meal_data[f'strMeasure{i}']}"
            for i in range(1, 21)
            if meal_data[f'strIngredient{i}']
        ]
    }
    return jsonify(meal)
# END OF API IMPLEMENTATION

# SHOPPING LIST FEATURE
@app.route('/shopping_list', methods=['GET', 'POST'])
def shopping_list():
    if request.method == 'POST':
        checked_items = request.form.getlist('checked_items') # Filter out checked items from the shopping list
        for recipe in selected_recipes:
            recipe["ingredients"] = [
                ingredient for ingredient in recipe["ingredients"] if ingredient not in checked_items
            ]
    return render_template('shopping_list.html', selected_recipes=selected_recipes)

# Clear Shopping List Route
@app.route('/clear_shopping_list', methods=['POST'])
def clear_shopping_list():
    global selected_recipes
    selected_recipes.clear()  # Clear all selected recipes
    return redirect(url_for('shopping_list'))  # Redirect to the shopping list page

# Meal Planner Route
@app.route('/meal_planner', methods=['GET', 'POST'])
def meal_planner():
    global meal_plan
    now = datetime.now()
    current_year = now.year # Get current month and year
    current_month = now.month

    if current_month not in meal_plan: # Initialize the meal plan for the current month if not already initialized
        meal_plan[current_month] = {}
    if request.method == 'POST':
        day = int(request.form.get('day')) # Process form submission for assigning meals
        recipe = request.form.get('recipe')

        if day in meal_plan[current_month]:
            meal_plan[current_month][day].append(recipe) # Assign the selected recipe to the specified day
        else:
            meal_plan[current_month][day] = [recipe]

    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(current_year, current_month) # Generate the calendar for the current month

    return render_template(
        'meal_planner.html',
        month_days=month_days,
        current_month=current_month,
        current_year=current_year,
        recipes=list(recipes.keys()),
        meal_plan=meal_plan[current_month]
    )

if __name__ == '__main__':
    app.run(debug=True)
