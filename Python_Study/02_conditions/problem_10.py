pet_species = "cat"
age = 4

if pet_species == "dog":
    if age < 2:
        food = "puppy food"
    else:
        food = "dog food"
elif pet_species == "cat":
    if age < 3:
        food = "kitten food"
    elif age > 3:
        food = "cat food"
        
print("Animal is ",pet_species," and it need",food)