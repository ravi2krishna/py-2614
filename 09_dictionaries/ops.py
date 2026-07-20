# Dictionaries Operations / Methods

data = {"a":"apple","b":"banana"}
print(data)

# update(): Adds / Updates 
data.update({"c":"cherry"}) # Adds if the key is not present 
print(data)

# update(): Adds / Updates 
data.update({"a":"apricot"}) # Updates if the key is already present 
print(data)

# pop(): Remove by key 

data = {"a":"apple","b":"banana"}
print(data)
data.pop("a")
print(data)
# data.pop("d") # KeyError: 'd'
# print(data)

# popitem(): Remove last item 
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)

# clear(): Empties Dictionary
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# get(): Used to get value for key
data = {"a":"apple","b":"banana"}
print(data)
print(data.get("a"))
print(data.get("c"))

# keys(): Used to get keys 
data = {"a":"apple","b":"banana"}
print(data)
data.keys()
print(data.keys())

for key in data.keys():
    print(key)


# values(): Used to get values 
data = {"a":"apple","b":"banana"}
print(data)
data.values()
print(data.values())

for value in data.values():
    print(value)
    
# items(): Used to get keys & values 
data = {"a":"apple","b":"banana"}
print(data)
data.items()
print(data.items())

for item in data.items():
    print(item)
    
# setdefault(): returns a value of key, if the key is already present
# if key doesn't exist, then adds the item and returns the value 
data = {"a":"apple","b":"banana"}
print(data)
data.setdefault("b","blueberry")
print(data.setdefault("b","blueberry"))
print(data)

data = {"a":"apple","b":"banana"}
print(data)
print(data.setdefault("c","cherry"))
print(data)

# copy(): Creates a copy of dict
data = {"a":"apple","b":"banana"}
print(data)
backup = data.copy()
print(backup)
