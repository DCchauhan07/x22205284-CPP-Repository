class FoodCalorieCalculator:
    def __init__(self):
        self.calories_per_gram = {
            'Chole Bhature': 500,
            'Kadai Paneer': 325,
            'Uttapam': 92,
            'Choole Kulche': 223,
            'erra papu': 100,
            'Rajma Chawal': 261,
            'Half boil': 78
        }

    def calculate_calories(self, food, quantity):
        if food.lower() in self.calories_per_gram:
            calories_per_gram = self.calories_per_gram[food.lower()]
            total_calories = calories_per_gram * quantity
            return total_calories
        else:
            return 'Food item not found in database'

if __name__ == '__main__':
    fcc = FoodCalorieCalculator()
    foods = ['Chole Bhature', 'Kadai Paneer', 'Uttapam', 'Choole Kulche', 'erra papu', 'Rajma Chawal', 'Half boil',]
    quantities = [100, 150, 200]

    for food in foods:
        for quantity in quantities:
            calories = fcc.calculate_calories(food, quantity)
            print(f'{quantity} grams of {food.capitalize()} contains {calories} calories.')