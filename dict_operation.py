#dictionary_operation

#copying one dictionary in to another 
num = {1:'one', 2:'two',3 : 'three'}
number = dict(num)
print(number)

# checking length of the dictionary
n = len(num)
print("len of dict num is: ",n)

#deleting element from a dictionary
del num[2]
print("deleting item with key = 2", num)

#inserting values in dictionary
num[4] = 'four'
print("after inserting 4th element", num)

#updating value in a dictionary
num[2] = 'second'
print("after updating 2nd values", num)

