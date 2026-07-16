# List Operations / Methods

# append(): Adds Element To End Of List 
data = [10,20,30,40,50]
print(data)
data.append(60)
# data.append("ravi")
# data.append([70,80])
print(data)

# extend(): Adds Iterable To List 
data = [10,20,30,40,50]
print(data)
data.extend([60,70,80])
print(data)

# insert(): Add Element To List Based On Index Position
data = [10,20,40,50]
print(data)
data.insert(2,30)
print(data)

# pop(): Remove an element, by default last element 
data = [10,20,30,40,50]
print(data)
data.pop() # Remove last element by default
print(data)

data = [10,20,30,40,50]
print(data)
data.pop(2)
print(data)

data = [10,20,30,40,50]
print(data)
# data.pop(10) # IndexError: pop index out of range
print(data)

# remove(): Remove an element based on value 
data = [10,20,30,40,50]
print(data)
data.remove(40)
print(data)

data = [10,20,10,30,10,40,50]
print(data)
data.remove(10)
print(data)

# Requirement is remove all 10's
data = [10,20,10,30,10,40,50]
print(data)

for i in data:
    if i == 10:
        data.remove(i)

print(data)

# Requirement is remove all 10's
data = [10,20,10,30,10,40,50]
print(data)

while 10 in data:
    data.remove(10)
print(data)   

# clear(): Removes all elements and empties 
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index(): Used to get the index position of value 
data = [10,20,30,40,50]
print(data)
position = data.index(30)
print(position)
print(data.index(20))
print(data.index(50))

# count(): Count the number of occurrences 
data = [10,20,10,30,10,40,50]
print(data)
print(data.count(10))

# reverse(): Reverses the list 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): Sorts the list, default is Ascending Order 
data = [10,30,20,40,50]
print(data)
data.sort() # default is Ascending Order 
print(data)

data = [10,30,20,40,50]
print(data)
data.sort(reverse=True) # Descending Order 
print(data)

# copy(): Creates a copy of list 
data = [10,30,20,40,50]
print(data)
backup = data.copy()
print(backup)

