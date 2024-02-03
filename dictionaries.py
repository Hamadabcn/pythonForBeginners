# dictionaries

band = {
    "vocals": "plant",
    "guitar": "page"
}

band2 = dict(vocals="plant", guitar="page")

print(band)
print(band2)
print(type(band))
print(len(band))

# access items in a dictionary
print(band["vocals"])
print(band.get("guitar"))

# list all keys in a dictionary
print(band.keys())

# list all values in a dictionary
print(band.values())

# list of keys/value pairs as tuples
print(band.items())

# verify if a key exists in the dictionary
print("guitar" in band)
print("triangle" in band)

# change values in the dictionary
band ["vocals"] = "coverdale"
band.update({"bass": "jpj"})

print(band)

# remove items from the dictionary
print(band.pop("bass"))
print(band)

band["drums"] = "bonham"
print(band)

print(band.popitem()) # it going to return a tuple
print(band)

# delete and clear items from dictionaries
band["drums"] = "bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries (how not to create a copy)
# band2 = band # create a reference it is not the right way to copy dictionaries
# print("bad copy🥴")
# print(band2)
# print(band)

# band2["drums"] = "Hamada"
# print(band)

band2 = band.copy()
band2["drums"] = "Hamada"
print("good copy😎")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("good copy😎")
print(band3)

# nested dictionaries
member1 = {
    "name": "plant",
    "instrument": "vocals",
}
member2 = {
    "name": "page",
    "instrument": "guitar",
}

band = {
    "member1": member1,
    "member2": member2,
}
print(band)
print(band["member1"]["name"])

# sets 
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# true is a dupe of 1, false is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you can not refer to an element in the set with an index position or a key as dictionaries

# add a new element to the set
nums.add(8)
nums.add(9)
nums.add(5)
print(nums)

# add elements from one set to another
morenums = {6, 7, 10, 11, 12}
nums.update(morenums)
print(nums)

# you can use update() with lists, tuples and dictionaries

# merge two sets to create a new set
one ={1, 2, 3}
two ={4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one ={1, 2, 3}
two ={2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one ={1, 2, 3}
two ={2, 3, 4}

one.symmetric_difference_update(two)
print(one)
