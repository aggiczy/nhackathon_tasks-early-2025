with open('./input.txt', 'r') as f:
    input = f.read()

import ast
from collections import defaultdict

data = ast.literal_eval(input)

code_candidates = {}
code_days = defaultdict(list)

for day in data:
    codes, events = day
    event_set = set(events)
    for code in codes:
        code_days[code].append(event_set)

for code in code_days:
    candidate = set.intersection(*code_days[code])
    code_candidates[code] = candidate

codes_list = list(code_candidates.keys())

solution = {}

def valid_assignment(assignment):
    for codes, events in data:
        if all(c in assignment for c in codes):
            day_assigned = [assignment[c] for c in codes]
            if sorted(day_assigned) != sorted(events):
                return False
    return True

found = None

def backtrack(i, assignment):
    global found
    if i == len(codes_list):
        if valid_assignment(assignment):
            found = assignment.copy()
            return True
        return False
    code = codes_list[i]
    for candidate in code_candidates[code]:
        assignment[code] = candidate
        if valid_assignment(assignment):
            if backtrack(i + 1, assignment):
                return True
    del assignment[code]
    return False

backtrack(0, {})

print(found)
