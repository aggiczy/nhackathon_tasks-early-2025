with open('./input.txt', 'r') as f:
    input = f.read()

import ast
import json
import sys
sys.setrecursionlimit(10**7)

days = ast.literal_eval(input)

all_codes = set()
all_events = set()
for day_codes, day_events in days:
    for c in day_codes:
        all_codes.add(c)
    for e in day_events:
        all_events.add(e)

code_list = sorted(all_codes)
event_list = sorted(all_events)

day_code_indices = []
day_event_counts = []
event_index_map = {e: i for i, e in enumerate(event_list)}
code_index_map = {c: i for i, c in enumerate(code_list)}

for (day_codes, day_events) in days:
    cidxs = set()
    for c in day_codes:
        cidxs.add(code_index_map[c])
    day_code_indices.append(cidxs)

    evt_count = [0]*len(event_list)
    for e in day_events:
        evt_count[event_index_map[e]] += 1
    day_event_counts.append(evt_count)

day_assigned_counts = []
for _ in days:
    day_assigned_counts.append([0]*len(event_list))

assignments = [-1]*len(code_list)

def backtrack(idx):
    if idx == len(code_list):
        return True

    for eidx in range(len(event_list)):
        can_assign = True
        needed_days = []
        for day_i, cidxs in enumerate(day_code_indices):
            if idx in cidxs:
                if day_assigned_counts[day_i][eidx] >= day_event_counts[day_i][eidx]:
                    can_assign = False
                    break
                needed_days.append(day_i)
        if not can_assign:
            continue

        assignments[idx] = eidx
        for d_i in needed_days:
            day_assigned_counts[d_i][eidx] += 1

        if backtrack(idx+1):
            return True

        assignments[idx] = -1
        for d_i in needed_days:
            day_assigned_counts[d_i][eidx] -= 1

    return False

ok = backtrack(0)

result = {}
for i, c in enumerate(code_list):
    e_idx = assignments[i]
    result[c] = event_list[e_idx]

print(json.dumps(result, ensure_ascii=False, indent=4))