import requests
import json

SPOONACULAR_API_KEY = 'f340994d08154111b87096d533084729'

def assign_meal_tags(title, dishTypes):
    tags = []
    title_lower = title.lower()
    dish_lower = [d.lower() for d in dishTypes]
    # Breakfast
    if 'breakfast' in dish_lower or any(k in title_lower for k in ['egg', 'pancake', 'smoothie', 'oatmeal']):
        tags.append('Breakfast')
    # Lunch
    if 'lunch' in dish_lower or any(k in title_lower for k in ['salad', 'sandwich', 'wrap']):
        tags.append('Lunch')
    # Dinner (default)
    if not tags:
        tags.append('Dinner')
    return tags

def fetch_spoonacular_recipes_by_tag(tag, n=5):
    url = f'https://api.spoonacular.com/recipes/random?number={n}&tags={tag}&apiKey={SPOONACULAR_API_KEY}'
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    recipes = data.get('recipes', [])
    foods = []
    for r in recipes:
        foods.append({
            'id': r.get('id'),
            'title': r.get('title'),
            'image': r.get('image'),
            'link': r.get('sourceUrl'),
            'cuisine': r.get('cuisines', []),
            'diet': r.get('diets', []),
            'tags': assign_meal_tags(r.get('title',''), r.get('dishTypes', [])),
            'description': (r.get('summary', '') or '').replace('<[^>]+>', '')[:120],
            'readyInMinutes': r.get('readyInMinutes'),
            'servings': r.get('servings'),
            'vegetarian': r.get('vegetarian'),
            'vegan': r.get('vegan'),
            'glutenFree': r.get('glutenFree'),
            'dairyFree': r.get('dairyFree'),
            'veryHealthy': r.get('veryHealthy'),
            'cheap': r.get('cheap'),
            'aggregateLikes': r.get('aggregateLikes'),
            'healthScore': r.get('healthScore')
        })
    return foods

def save_to_js(foods, filename='foodswipe/assets/foods.js'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('const foods = ')
        json.dump(foods, f, ensure_ascii=False, indent=2)
        f.write(';')

if __name__ == '__main__':
    breakfast = fetch_spoonacular_recipes_by_tag('breakfast', 5)
    lunch = fetch_spoonacular_recipes_by_tag('lunch', 5)
    dinner = fetch_spoonacular_recipes_by_tag('dinner', 5)

    all_foods = breakfast + lunch + dinner

    # Remove duplicates by recipe ID
    unique_foods = {f['id']: f for f in all_foods}.values()

    save_to_js(list(unique_foods))
    print(f"Saved {len(unique_foods)} recipes to assets/foods.js")
