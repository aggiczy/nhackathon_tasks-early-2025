with open('./input.txt', 'r') as f:
    input = f.read()

dice_options = [2, 3, 4, 6, 8, 10, 20]

memo_combinations = {}

def find_first_combination_recursive(k, current_target_sum, start_idx, current_combo_list):
    state = (k, current_target_sum, start_idx, tuple(sorted(current_combo_list)))
    if state in memo_combinations:
        return list(memo_combinations[state]) if memo_combinations[state] is not None else None

    if k == 0:
        return list(current_combo_list) if current_target_sum == 0 else None
    
    if current_target_sum < 0:
        return None

    if start_idx >= len(dice_options) or \
        k * dice_options[start_idx] > current_target_sum or \
        k * dice_options[-1] < current_target_sum:
        return None

    for i in range(start_idx, len(dice_options)):
        die_val = dice_options[i]
        current_combo_list.append(die_val)
        
        result = find_first_combination_recursive(k - 1, current_target_sum - die_val, i, current_combo_list)
        
        current_combo_list.pop()
        if result:
            memo_combinations[state] = list(result)
            return result
    
    memo_combinations[state] = None
    return None

lines = input.strip().split('\n')
results_to_print = []

for line in lines:
    if not line.strip():
        continue
    parts = line.split()
    min_val = int(parts[0])
    max_val = int(parts[1])

    L_target = max_val - min_val + 1

    found_solution_for_line = False
    max_n_dice_to_check = 6
    for n_dice in range(1, max_n_dice_to_check + 1):
        target_sum_for_combination = L_target + n_dice - 1
        
        if L_target == 1 and n_dice > 0:
            pass

        if target_sum_for_combination < n_dice * dice_options[0] or \
            target_sum_for_combination > n_dice * dice_options[-1]:
            continue

        chosen_combo_sides = find_first_combination_recursive(n_dice, target_sum_for_combination, 0, [])

        if chosen_combo_sides:
            min_value_from_dice_combo = n_dice 
            
            offset = min_val - n_dice
            
            dice_str_parts = [f"1d{s}" for s in chosen_combo_sides]
            result_str = "+".join(dice_str_parts)
            
            if offset > 0:
                result_str += f"+{offset}"
            elif offset < 0:
                result_str += f"{offset}"
            
            results_to_print.append(result_str)
            found_solution_for_line = True
            break

for res in results_to_print:
    print(res)