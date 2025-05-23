with open('./input.txt', 'r') as f:
  input = f.read()

import ast

data = ast.literal_eval(input)

possibilities = {}

for codes, events in data:
    event_set = set(events)
    for code in codes:
        if code in possibilities:
            possibilities[code] &= event_set
        else:
            possibilities[code] = set(event_set)

assignment = {}

progress = True
while progress:
    progress = False
    for code, opts in list(possibilities.items()):
        if len(opts) == 1:
            letter = next(iter(opts))
            assignment[code] = letter
            del possibilities[code]
            for other in possibilities:
                if letter in possibilities[other]:
                    possibilities[other].remove(letter)
            progress = True

print(assignment)