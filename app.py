from flask import Flask, render_template, request, redirect, url_for
from recipes import recipes  # Import the recipes dictionary from recipes.py
import calendar
from datetime import datetime
app = Flask(__name__)

# Selected recipes and their ingredients
selected_recipes = []

meal_plan = {}

# Home Route
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recipe_finder', methods=['GET', 'POST'])
def recipe_finder():
    results = []
    if request.method == 'POST':
        user_ingredients = request.form.get('ingredients', '').lower().split(', ')
        filter_option = request.form.get('filter_option')

        for recipe_name, details in recipes.items():
            ingredients = details["ingredients"]
            vegan = details["vegan"]
            matching_ingredients = set(user_ingredients) & set(ingredients)

            if matching_ingredients:
                missing_ingredients = set(ingredients) - matching_ingredients
                if filter_option == "vegan" and not vegan:
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
    if recipe_name:
        for recipe in recipes:
            if recipe == recipe_name:
                ingredients = recipes[recipe]
                selected_recipes.append({
                    "name": recipe,
                    "ingredients": ingredients
                })
    return redirect(url_for('shopping_list'))


# Shopping List Route
@app.route('/shopping_list', methods=['GET', 'POST'])
def shopping_list():
    if request.method == 'POST':
        checked_items = request.form.getlist('checked_items')
        # Filter out checked items from the shopping list
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

    # Get current month and year
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # Initialize the meal plan for the current month if not already initialized
    if current_month not in meal_plan:
        meal_plan[current_month] = {}

    # Process form submission for assigning meals
    if request.method == 'POST':
        day = int(request.form.get('day'))
        recipe = request.form.get('recipe')

        # Assign the selected recipe to the specified day
        if day in meal_plan[current_month]:
            meal_plan[current_month][day].append(recipe)
        else:
            meal_plan[current_month][day] = [recipe]

    # Generate the calendar for the current month
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(current_year, current_month)

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
