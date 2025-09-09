# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Exercises: Level 1
# Find the length of the set it_companies
# print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add("Twitter")
# print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Nvidia', 'Itel', 'Intel', 'HP'])
# print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.pop()
# print(it_companies)
# print(it_companies.pop()) #returns the removed item 

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Exercises: Level 2
# Join A and B
# new_set = A.union(B)
# print(new_set)
# # Find A intersection B
# print(A.intersection(B))
# # Is A subset of B
# print(A.issubset(B)) #all elements of A are in B
# # Are A and B disjoint sets
# print(A.isdisjoint(B))
# # Join A with B and B with A
# print(A.union(B))
# print(B.union(A))
# # What is the symmetric difference between A and B
# print(A.symmetric_difference(B)) #returns set of things that are unique IN EACH SET
# # Delete the sets completely
# del A, B
# print(A) #err

age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age_set)
def len_det():
    print(f"List is {len(age)} values long")
    print(f"Set is {len(age_set)} values long")
    if len(age_set) > len(age):
        print("The set is longer")
    else:
        print("The list is longer")
len_det()
# Explain the difference between the following data types: string, list, tuple and 
    # String: sequence of characters, immutable.
    # List: ordered, mutable collection that allows duplicates. Example: [1, 2, 2, 3].
    # Tuple: ordered, immutable collection that allows duplicates. Example: (1, 2, 2, 3).
    # Set: unordered, mutable collection with no duplicates. Example: {1, 2, 3}.

# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
print(words)
sen_set = set(words)
print(sen_set)
print(len(sen_set))

# extra bits
    # removing punctuation
    # adressing 'I'