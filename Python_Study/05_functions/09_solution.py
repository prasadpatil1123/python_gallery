def even_generator(limit):
    for i in range(2, limit+1,3):
        yield i
        
for num in even_generator(15):
    print(num)