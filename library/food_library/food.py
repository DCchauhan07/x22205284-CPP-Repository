def calculate_total_calories(foods, servings):
    calorie_values = {
        "Chole Bhature": 252,
        "Kadai Paneer": 105,
        "Uttapam": 170,
        "Choole Kulche": 220,
        "erra papu": 100,
        "Rajma Chawal": 150,
        "Noodles": 200,
    }

    total_calories = 0
    for food, serving in zip(foods, servings):
        if food.lower() in calorie_values:
            total_calories += calorie_values[food.lower()] * serving
        else:
            print(f"Warning: No calorie information found for {food}")

    return total_calories

# Example usage:
foods = ["Chole Bhature", "Kadai Paneer", "Uttapam", "Choole Kulche", "erra papu", "Rajma Chawal", "Noodles"]
servings = [2, 1, 3, 2, 1, 2, 1]
total_calories = calculate_total_calories(foods, servings)
print("Total Calories:", total_calories)
