numbers = [1,-2,3,4,-5,6,-7,-8,-9,10]
pos_count = 0

for num in numbers:
    if num > 0:
        pos_count += 1
        
print("Final count", pos_count)