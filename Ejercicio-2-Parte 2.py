import random


minus = "abcdefghijk"
mayus = "ABCDEFGHIJK"
numbers = "123456789"
simbols = "!?¿$%&/()"
    
unconcat = minus + mayus + numbers + simbols
longconcat = 10

concat = " ".join(random.sample(unconcat, longconcat))
    
print("tu concat es:  ", concat)