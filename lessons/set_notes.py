# Set is a collection of unordered and un-indexed distinct elements
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# print(type(fruits))
# SET{} vs TUPLE()

# checking a item we use in mebership operator 

# adding items
# adding items ot a set we use add() example.add(item)
# adding multiple items: update(), takes a list args. example.update([item1, item2, item3])

# removing items
# remove(), but this raises errors if it isn't found, use discard() instead
# pop() methods remove a random item from a list and it returns the removed item
# clearing items
# st.clear()
# st.del

# joining sets, union()/ update()
# st3 = st1.union(st2), returns a new set
# st1.update(st2), inserts a set into a given set

# intersection items
# Intersection returns a set of items which are in both the sets
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item3', 'item2'}
# print(st1.intersection(st2)) # {'item3', 'item2'}

# joining sets
# If two sets do not have a common item or items we call them disjoint sets
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# print(st1.isdisjoint(st2)) # False returns True if there is no common item 

# checking diff btwn 2 sets returns the difference between 2 sets (but not in)
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# print(st2.difference(st1)) # set() empty set 
# # This means elements in st2 but not in st1.
# # All of these are already inside st1
# # So result = set() (empty set).
# print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2

# symmetric difference 
# returns a set that contains all items from both sets, except items that are present in both sets
# items that are unique in each set
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# print(st2.symmetric_difference(st1)) # {'item1', 'item4'}

# subset and superset
# A set A is a subset of set B if every element of A is in B. read as (x issubset of (y)) returns True or False

# A set A is a superset of set B if A contains every element of B.

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True