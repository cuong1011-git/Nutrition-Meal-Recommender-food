import random

def solve_csp(filtered_df, constraints):
    breakfasts = filtered_df[filtered_df['category'] == 'Sáng'].to_dict('records')
    lunches = filtered_df[filtered_df['category'] == 'Trưa'].to_dict('records')
    dinners = filtered_df[filtered_df['category'] == 'Tối'].to_dict('records')
    snacks = filtered_df[filtered_df['category'] == 'Ăn vặt'].to_dict('records')
    
    # If any category is empty after filtering, return None
    if not breakfasts or not lunches or not dinners:
        return None
        
    # Simple backtracking / random sampling approach for CSP
    # We will try up to 2000 random combinations to find one that satisfies constraints
    best_meal_plan = None
    best_score = float('inf')
    
    for _ in range(2000):
        b = random.choice(breakfasts)
        l = random.choice(lunches)
        d = random.choice(dinners)
        s = random.choice(snacks) if snacks else None
        
        total_cal = b['calories'] + l['calories'] + d['calories'] + (s['calories'] if s else 0)
        total_prot = b['protein'] + l['protein'] + d['protein'] + (s['protein'] if s else 0)
        total_sugar = b['sugar'] + l['sugar'] + d['sugar'] + (s['sugar'] if s else 0)
        total_sodium = b['sodium'] + l['sodium'] + d['sodium'] + (s['sodium'] if s else 0)
        total_fat = b['fat'] + l['fat'] + d['fat'] + (s['fat'] if s else 0)
        
        # Check constraints
        if total_cal > constraints['max_calories'] or total_cal < constraints['min_calories']:
            continue
        if total_prot < constraints['min_protein']:
            continue
        if total_sugar > constraints['max_sugar']:
            continue
        if total_sodium > constraints['max_sodium']:
            continue
        if total_fat > constraints['max_fat']:
            continue
            
        # Heuristic: minimize the difference from target calories
        target_cal = (constraints['min_calories'] + constraints['max_calories']) / 2
        score = abs(total_cal - target_cal)
        
        if score < best_score:
            best_score = score
            best_meal_plan = {
                'breakfast': b,
                'lunch': l,
                'dinner': d,
                'snack': s,
                'totals': {
                    'calories': total_cal,
                    'protein': total_prot,
                    'sugar': total_sugar,
                    'sodium': total_sodium,
                    'fat': total_fat
                }
            }
            
    # If strict constraints fail, relax them and try again to at least return something
    if best_meal_plan is None:
        b = random.choice(breakfasts)
        l = random.choice(lunches)
        d = random.choice(dinners)
        best_meal_plan = {
            'breakfast': b,
            'lunch': l,
            'dinner': d,
            'snack': None,
            'totals': {
                'calories': b['calories'] + l['calories'] + d['calories'],
                'protein': b['protein'] + l['protein'] + d['protein'],
                'sugar': b['sugar'] + l['sugar'] + d['sugar'],
                'sodium': b['sodium'] + l['sodium'] + d['sodium'],
                'fat': b['fat'] + l['fat'] + d['fat']
            },
            'relaxed': True
        }
        
    return best_meal_plan
