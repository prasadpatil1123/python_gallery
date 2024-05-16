# num = 5

# for i in range(1,num+1):
#     if num % 2 == 0:
#         print("Yes it is prime")
#         break
#     else:
#         print("No It is not Prime")
#         break

num  = 29
is_prime = True

if num > 1:
    for i in range(2, num):
        if( num % i )==0:
            is_prime = False
            
print(is_prime)