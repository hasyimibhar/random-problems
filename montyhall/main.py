import random

# [c, e, e, e, e, e, e]
# [0, 0, 0, 0, 0, 0, 0]

# [1, 2, 0, 0, 0, 0, 0]

def simulate(nd, switch):
    door = random.randrange(nd)

    pi = randelem([i for i in range(nd)])
    ri = randelem([i for i in range(nd) if i != pi and i != door])
    if switch:
        pi = randelem([i for i in range(nd) if i != pi and i != ri])
    return pi == door

def randelem(list):
    i = random.randrange(len(list))
    return list[i]

num_doors = 3
experiments = 10000

noswitch = []
switch = []
for i in range(experiments):
    noswitch.append(simulate(num_doors, False))
    switch.append(simulate(num_doors, True))

print(sum(noswitch)/experiments)
print(sum(switch)/experiments)
