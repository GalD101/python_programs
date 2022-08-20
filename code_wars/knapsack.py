#!/usr/bin/python3

def knapsack(capacity, items):
    # Be greedy!
    ratio = [v/w for w, v in items]
    solution = [0 for _ in items] # hashmap
    item_counter = 0
    
    while capacity > 0 and len(ratio) != 0:
        biggest_index = ratio.index(max(ratio))
        best_item_weight, best_item_value = items[biggest_index] # (w, v) tuple
        while capacity - best_item_weight >= 0:
            capacity -= best_item_weight
            item_counter += 1
        ratio.pop(biggest_index)
        solution[biggest_index] = item_counter
        item_counter = 0
        
    return solution
