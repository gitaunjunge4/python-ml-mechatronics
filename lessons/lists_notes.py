# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.

#Unpacking list items 
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)


# orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

#slicing
#modifying
#checking
#appending lst.append(item)
#inserting lst.insert(index, item)
#remove lst.remove(item), lst.pop(index)- removes the specified index, del lst, del lst[index], del list[0:4] 
#clearing lst.clear()
#copying, lst2 = lst1 directly copying isn't the best since changes made on lst2 affects lst1. we use lst.copy()
#joining list3 = list1 + list2
#extend old_lst.extend(new_lst)
#counting item sin a list lst.count(item)
#index lst.index(item)
#reverse()
#sorting 
#         sort() method reorders the list items in ascending order and modifies the original list, (reverse=True), 
#           arranges the list in desc order
#         sorted(): returns the ordered list without modifying the original list

            # plants = conifers + cycads
            # print(plants)
            # ordered_plants = sorted(plants)
            # print(ordered_plants)

            # # ans 2
            # plants_copy = plants.copy()
            # plants_copy.sort()
            # print(plants_copy)


# LIST COMPREHENSION 
# newlist = [expression for item in iterable if condition == True]
# return value is a new list, leaving the old list unchanged
# expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list
# condition is like a filter that only accepts the items that evaluate to True.
