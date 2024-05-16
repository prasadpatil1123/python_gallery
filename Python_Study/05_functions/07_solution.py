def sum_all(*args):
    print(args)
    for i in args:
        print(i)
    return sum(args)
    
    
print(sum_all(1,3,4))