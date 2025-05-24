with open('./input.txt', 'r') as f:
    input = f.read()

def get_dice_expression(min_val, max_val):
    diff = max_val - min_val
    dice_sides = [20, 10, 8, 6, 4, 3, 2]

    def backtrack(target, n, start=0):
        if n == 0:
            return [] if target == 0 else None
        max_possible = dice_sides[0] * n
        min_possible = dice_sides[-1] * n
        if target < min_possible or target > max_possible:
            return None

        for i in range(start, len(dice_sides)):
            side = dice_sides[i]
            if side <= target:
                result = backtrack(target - side, n - 1, i)
                if result is not None:
                    return [side] + result
        return None

    for N in range(1, 7):
        target_sum = diff + N
        if target_sum < N * 2:
            continue
        combo = backtrack(target_sum, N)
        if combo is not None:
            offset = min_val - N
            expression_parts = []
            for side in combo:
                expression_parts.append(f"1d{side}")
            expression = "+".join(expression_parts)
            if offset > 0:
                expression += f"+{offset}"
            elif offset < 0:
                expression += f"{offset}"
            return expression

    return "Impossible"


lines = input.strip().split("\n")
for line in lines:
    parts = line.strip().split()
    if len(parts) != 2:
        continue
    min_v = int(parts[0])
    max_v = int(parts[1])
    result = get_dice_expression(min_v, max_v)
    print(result)
