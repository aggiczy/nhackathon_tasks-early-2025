with open('dice_range_expression/input.txt', 'r') as f:
  input = f.read()

def get_dice_expression(min_val, max_val):
    diff = max_val - min_val
    if diff == 0:
        return str(min_val)

    coins = [19, 9, 7, 5, 3, 2, 1]

    result_coins = []
    remaining = diff
    for coin in coins:
        while remaining >= coin:
            result_coins.append(coin)
            remaining -= coin

    result_coins.sort()
    
    k = len(result_coins)
    
    offset = min_val - k
    
    dice_terms = []
    for coin in result_coins:
        die_val = coin + 1
        dice_terms.append(f"1d{die_val}")
    
    expr = "+".join(dice_terms)
    if offset > 0:
        expr += f"+{offset}"
    elif offset < 0:
        expr += f"{offset}"
    
    return expr


results = []
for line in input.splitlines():
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) != 2:
        continue
    try:
        low = int(parts[0])
        high = int(parts[1])
        expr = get_dice_expression(low, high)
        results.append(expr)
    except Exception as e:
        results.append("Error")

for res in results:
    print(res)