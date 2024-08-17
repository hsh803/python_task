import random

def get_random(m, n):
    lst = []
    for i in range(n):
        lst.append(random.randrange(m)) # get random numbers n times to create a random number list.
    return lst

#print(get_random(1000, 100)) -> Test example


