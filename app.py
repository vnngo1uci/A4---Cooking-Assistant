from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store recipes
recipes = {
    "Pasta Primavera": ["pasta", "bell peppers", "tomatoes", "cheese"],
    "Chicken Curry": ["chicken", "curry powder", "onions", "coconut milk"],
    "Vegetable Stir Fry": ["broccoli", "carrots", "soy sauce", "garlic"],
    "Guacamole": ["avocado", "lime", "onions", "tomatoes"],
    "Pasta Carbonara": ["pasta", "chicken", "cheese"],
}

# Selected recipes and their missing ingredients
selected_recipes = []

# Home Route
@app.route('/')
def home():
    return render_template('index.html')


# Recipe Finder Route
@app.route('/recipe_finder', methods=['GET', 'POST'])
def recipe_finder():
    results = []
    if request.method == 'POST':
        user_ingredients = request.form.get('ingredients', '').lower().split(', ')
        for recipe_name, ingredients in recipes.items():
            matching_ingredients = set(user_ingredients) & set(ingredients)
            if matching_ingredients:
                missing_ingredients = set(ingredients) - matching_ingredients
                results.append({
                    "name": recipe_name,
                    "matching": list(matching_ingredients),
                    "missing": list(missing_ingredients),
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
@app.route('/shopping_list')
def shopping_list():
    # Consolidate ingredients from all selected recipes
    shopping_list = []
    for recipe in selected_recipes:
        shopping_list.extend(recipe["ingredients"])
    shopping_list = list(set(shopping_list))  # Remove duplicates
    return render_template('shopping_list.html', shopping_list=shopping_list)


if __name__ == '__main__':
    app.run(debug=True)
