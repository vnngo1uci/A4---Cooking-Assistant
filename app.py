from flask import Flask, render_template, request

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Recipe Finder Route
@app.route('/recipe_finder', methods=['GET', 'POST'])
def recipe_finder():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        # Mock data for demonstration
        recipes = [
            {"name": "Pasta", "missing": "Cheese"},
            {"name": "Salad", "missing": "Olives"},
        ]
        return render_template('recipe_finder.html', ingredients=ingredients, recipes=recipes)
    return render_template('recipe_finder.html', recipes=[])

# Shopping List Route
@app.route('/shopping_list')
def shopping_list():
    # Mock shopping list for demonstration
    shopping_list = ["Tomatoes", "Cheese", "Pasta"]
    return render_template('shopping_list.html', shopping_list=shopping_list)

# Meal Planner Route
@app.route('/meal_planner')
def meal_planner():
    # Mock meal plan
    meal_plan = {
        "Monday": ["Pasta", "Salad"],
        "Tuesday": ["Soup", "Grilled Cheese"],
    }
    return render_template('meal_planner.html', meal_plan=meal_plan)

if __name__ == '__main__':
    app.run(debug=True)
