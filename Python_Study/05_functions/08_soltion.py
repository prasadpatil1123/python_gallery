def marvel(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
marvel(name="IronMan", power="armor")
marvel(name="Hulk", power="punch",color="Green")