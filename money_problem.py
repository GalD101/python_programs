import itertools

# Amount of money we have:
bills = [20, 20, 20, 10, 10, 10, 10,
         10, 5, 5, 1, 1, 1, 1, 1]

# How many ways to get 100$?
makes_100 = []
for n in range(1, len(bills) + 1):
    for combination in itertools.combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)

print(set(makes_100))
print(len(set(makes_100)))