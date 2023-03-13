# let's make a set

my_set01 = {'bsc', 'msc', 'phd', 'dip', 'high', 'ele'}
my_set02 = { 'bsc', 'msc', 'post', 'free'}

# this is the sum of both sets
print(my_set01.union(my_set02))

# difference is what set01 has and set02 doesn't
print(my_set01.difference(my_set02))

# difference is what set02 has and set01 doesn't
print(my_set02.difference(my_set01))

# intersection is what both sets have in common
print(my_set01.intersection(my_set02))


