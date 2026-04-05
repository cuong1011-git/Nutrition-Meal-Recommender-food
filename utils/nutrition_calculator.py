def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    if height_m == 0:
        return 0
    return weight_kg / (height_m ** 2)

def calculate_daily_calories(age, gender, weight_kg, height_cm):
    # Mifflin-St Jeor Equation
    if gender == "Male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    
    # Assuming moderate activity level
    return bmr * 1.55

def get_nutritional_constraints(calories, diabetes, hypertension, obesity, heart_disease):
    constraints = {
        'min_calories': calories * 0.85,
        'max_calories': calories * 1.15,
        'min_protein': (calories * 0.2) / 4, # 20% of calories from protein
        'max_sugar': 50, # default max sugar
        'max_sodium': 2300, # default max sodium
        'max_fat': (calories * 0.35) / 9 # 35% of calories from fat
    }
    
    if diabetes:
        constraints['max_sugar'] = 30
    if hypertension:
        constraints['max_sodium'] = 1500
    if obesity:
        constraints['max_calories'] = calories * 0.8 # Caloric deficit
    if heart_disease:
        constraints['max_fat'] = (calories * 0.25) / 9
        constraints['max_sodium'] = 1500
        
    return constraints
