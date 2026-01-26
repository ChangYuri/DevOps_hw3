from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

# Small dataset (kept simple for CI exercises)
recipes = [
    {"id": 1, "name": "Tomato Scrambled Eggs", "ingredients": ["egg", "tomato", "oil", "salt"]},
    {"id": 2, "name": "Egg Fried Rice", "ingredients": ["rice", "egg", "scallion", "oil"]},
    {"id": 3, "name": "Pork with Green Pepper", "ingredients": ["pork", "green pepper", "oil", "salt"]}
]


@app.route('/daily', methods=['GET'])
def daily_recipe():
    """Return a deterministic daily recipe (random but lightweight)."""
    recipe = random.choice(recipes)
    return jsonify({
        "recipe": recipe["name"],
        "id": recipe["id"]
    })

# 2 check ingredients
@app.route('/recommend', methods=['POST'])
def recommend():
    # Be permissive when parsing JSON; avoid exceptions when content-type is missing
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"recipes": []}), 200

    raw = data.get("ingredients", [])

    # Accept either a list or a comma-separated string from clients
    if isinstance(raw, str):
        items = [s.strip() for s in raw.split(',') if s.strip()]
    elif isinstance(raw, list):
        items = [str(s).strip() for s in raw if str(s).strip()]
    else:
        items = []

    provided = set(items)

    # Exact matches: recipe ingredients are subset of provided ingredients
    exact = []
    for recipe in recipes:
        if set(recipe["ingredients"]).issubset(provided) and provided:
            exact.append({"id": recipe["id"], "name": recipe["name"]})

    if exact:
        return jsonify({"recipes": exact}), 200

    # Fallback: return partial matches (share at least one ingredient)
    partial = []
    for recipe in recipes:
        if provided and any(ing in provided for ing in recipe["ingredients"]):
            partial.append({"id": recipe["id"], "name": recipe["name"]})

    return jsonify({"recipes": partial}), 200

# 3 check recipe details
@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if not recipe:
        return jsonify({"error": "Not found"}), 404
    return jsonify(recipe)


@app.route('/', methods=['GET'])
def index():
    """Serve a minimal frontend to interact with the API."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)