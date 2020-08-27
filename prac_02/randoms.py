import random
print(random.randint(5, 20))
# line 1: the smallest number would be 5 and the largest would be 19
print(random.randrange(3, 10, 2))
# line 2: the smallest number would be 3 and the largest 9.
# line 2 could not have produced a four as it increases by 2
# since it starts at 3 it will only include odd numbers from 3-10
print(random.uniform(2.5, 5.5))
# line 3: the smallest number would have been 2.5 and the largest being 5.499999999999999
print(random.randint(1, 101))