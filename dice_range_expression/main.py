with open('./input.txt', 'r') as f:
    input = f.read()

dice_options = [20, 10, 8, 6, 4, 3, 2]

def dice_expression(min_val: int, max_val: int):
    dice_range = (max_val - min_val + 1)
    if min_val >= 0:
        shift_val = max_val - dice_range
    else:
        shift_val = min_val - 1
    
    used_dice = []
    
    for sides in dice_options:
        while dice_range - sides >= 0 and (dice_range % 2 != 0):
            while (dice_range % 2 != 0) and (dice_range - sides >= 0):
                used_dice.append(3)
                dice_range -= 3
        while dice_range - sides >= 0 and (dice_range % 2 == 0):
            used_dice.append(sides)
            dice_range -= sides

    used_dice.sort(reverse=True)
    counts = {}
    for d in used_dice:
        counts[d] = counts.get(d, 0) + 1

    merged_parts = []
    for side, count in counts.items():
        merged_parts.append(f"{count}d{side}")
    dice_expr = "+".join(merged_parts)
    
    if shift_val > 0:
        dice_expr += f"+{shift_val}"
    elif shift_val < 0:
        dice_expr += f"{shift_val}"

    print(dice_expr)

lines = input.strip().split("\n")
for l in lines:
    if not l.strip():
        continue
    parts = l.split()
    if len(parts) < 2:
        continue
    minimum = int(parts[0])
    maximum = int(parts[1])
    dice_expression(minimum, maximum)