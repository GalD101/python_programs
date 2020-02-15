bricks_each_pig = int(input
("Enter three digits (each digit for one pig):"))
total_bricks = int(bricks_each_pig % 10  + 
(bricks_each_pig / 10) % 10 + bricks_each_pig / 100)
print(total_bricks)
print(int(total_bricks / 3))
remainder = total_bricks % 3
print(remainder)
print(remainder == 0)