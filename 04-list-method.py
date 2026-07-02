test = ['abc','test','mumbai','abc']
veg = ["tttt","svvvv"]

# test.append("Mango")   #==============> append
# test.insert(1,"Mango")   #==============> insert add specfic key
# test.remove("mumbai")   #==============> remove value
# test.pop(1)  #===============>last value remove if add any key put so remove specific
# test.clear()   #==============> all value remove
# test.sort(reverse=True);  #==================> sort after reverse and captial first char mai in first key show
# test.reverse()  #====================> reverse all data
# x = test.copy()  #===========>>copy
# x = test[:]  #===============> copy you can pass index number
# test.extend(veg)  #================> add in second another list


test = ['abc','test','mumbai','abc']
x = test.index("test")   #==============> find the key  number
x = test.index("test",1,3)   #==============> find the key  number according key range
x = test.count("test")   #==============> find the value  count number
x = len(test)   #==============> total count of number list
x = max(test)   #==============> max value of list last char find
x = min(test)   #==============> min value of list first char find
x = list(test)   #==============> convert in the list

print(x)