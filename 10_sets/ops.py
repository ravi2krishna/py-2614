# Set Operations / Methods

# add(): Add Element To Set
data = {10,20,30,40,50}
data.add(60)
print(data)

# update(): Add Multiple Elements To Set
data = {10,20,30,40,50}
data.update([60,70,80,60,90])
print(data)

# pop(): Removes Random Elements From Set
data = {10,20,30,40,50}
data.pop()
print(data)

# remove(): Removes Elements From Set By value 
data = {10,20,30,40,50}
data.remove(20)
# data.remove(200) # KeyError: 200
print(data)

# discard(): Removes Elements From Set By value 
data = {10,20,30,40,50}
data.discard(20)
data.discard(200) 
print(data)

# clear(): Empties Set
data = {10,20,30,40,50}
data.clear()
print(data)

# copy(): Create Copy 
data = {10,20,30,40,50}
backup = data.copy()
print(backup)

# Set Specific Methods 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): Combine Sets 
print(s1.union(s2))
print(s1 | s2)

# intersection(): Get Common Elements From Set 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update(): Get Common Elements From Set, Updates Calling Set  
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference(): Removes Common Elements and gives unique elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)


# difference_update(): Removes Common Elements and gives unique elements, Updates Calling Set  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference(): Removes Common Elements from sets and takes combined elements from both sets
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1)
print(s2)

# symmetric_difference_update(): Removes Common Elements from sets and takes combined elements from both sets, Updates Calling Set  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset(): Checks if given Set is a subset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset(): Checks if given Set is a Superset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.issuperset(s3))
print(s2.issuperset(s3))

# isdisjoint(): Checks if given Sets have no common elements 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s2.isdisjoint(s3))
print(s1.isdisjoint(s3))