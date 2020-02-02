# Dictionary for set
names = {1: 'bablu', 2: 'najmul', 4: 'juton'}

# available function for dictionary
# names.copy(self)
# names.clear(self)
# names.fromkeys(seq)
# names.get(self, k)
# names.items(self)
# names.keys(self)
# names.pop(self, k)
# names.popitem(self)
# names.setdefault(self, k, default)
# names.update(self, __m, kwargs)
# names.values(self)

# For get value
print(names[1])
# or
print(names.get(1))

# If key not found get function return 2nd parameter for custom message or default return None
print(names.get(3, 'Not found'))


# Dictionary for List
keys = ['kartic', 'niloy', 'bablu', 'juton']
values = ['python', 'js', 'c++', 'c#']

# keys and values list convert to an object using zip()
data = zip(keys, values)

# data object converted to an dictionary list
data = dict(data)

# Add new key and value to data dictionary
data['samiul'] = 'php'
print(data)

# Delete value by key from data dictionary
del data['samiul']
print(data)

# Get single value by key from Data Dictionary
print(data.get('kartic'))









