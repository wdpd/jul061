'''Some exercises: dynamic programming'''



def cost(specs_):
    cost_dict = {12: 1.05, 10: 0.95, 9: 0.85, 8: 0.58, 7: 0.52, 6: 0.5, 5: 0.5, 4: 0.4, 3: 0.34, 2: 0.33, 1: 0.32}
    costs = [cost_dict[x] for x in specs_]
    return sum(costs)


specs = [12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
specs_end = [1 for x in range(1, 19 + 1)]
cost_sum = []
# for i in specs:
specs_selected = [12]
while specs_selected != specs_end:
    specs_selected_sum = sum(specs_selected)
    if specs_selected_sum < 19:
        specs_selected.append(specs_selected[-1])
    elif specs_selected_sum > 19:
        specs_selected[-1] = specs[specs.index(specs_selected[-1]) + 1]
    else:
        # print(cost(specs_selected)),
        # print(specs_selected)
        cost_sum.append((cost(specs_selected), specs_selected[:]))
        if specs_selected[-1] == 1:
            temp = specs[specs.index(specs_selected[specs_selected.index(1) - 1]) + 1]
            specs_selected = specs_selected[:specs_selected.index(1) - 1]
            specs_selected.append(temp)
        else:
            specs_selected[-1] = specs[specs.index(specs_selected[-1]) + 1]
print(cost_sum)
print(sorted(cost_sum))
