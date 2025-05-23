with open('gear_system/input.txt', 'r') as f:
  input = f.read()

import re
from collections import deque

def parse_input(input_str):
    state_match = re.search(r'\[(.*?)\]', input_str)
    if not state_match:
        raise ValueError("Nem megfelelő formátum a bemenetben! (Nincs lista)")
    state_text = state_match.group(0)
    try:
        target_state = eval(state_text)
        if not (isinstance(target_state, list) and len(target_state) == 3):
            raise ValueError
    except:
        raise ValueError("Nem megfelelő formátum a lista elemei vagy formátuma!")
    
    rest = input_str[state_match.end():].strip()
    if rest:
        try:
            max_moves = int(rest.split()[0])
        except:
            max_moves = 8
    else:
        max_moves = 8
    return target_state, max_moves

def apply_move(state, move):
    new_state = state.copy()
    if move == "left":
        new_state[0] = new_state[0] + 1 if new_state[0] < 3 else 1
        new_state[1] = new_state[1] + 1 if new_state[1] < 3 else 1
    elif move == "right":
        new_state[1] = new_state[1] + 1 if new_state[1] < 3 else 1
        new_state[2] = new_state[2] + 1 if new_state[2] < 3 else 1
    return new_state

def bfs_solution(target_state, max_moves):
    start_state = [3, 3, 3]
    if start_state == target_state:
        return []
    queue = deque()
    queue.append((start_state, []))
    visited = {tuple(start_state)}
    
    while queue:
        state, moves = queue.popleft()
        if len(moves) >= max_moves:
            continue
        for move in ["left", "right"]:
            new_state = apply_move(state, move)
            new_moves = moves + [move]
            if new_state == target_state:
                return new_moves
            t_new_state = tuple(new_state)
            if t_new_state not in visited:
                visited.add(t_new_state)
                queue.append((new_state, new_moves))
    return None

try:
    target_state, max_moves = parse_input(input)
except Exception as e:
    print("Bemeneti hiba:", e)
    exit(1)

solution_moves = bfs_solution(target_state, max_moves)
if solution_moves is None:
    print("Megoldhatatlan")
else:
    print(" ".join(solution_moves))