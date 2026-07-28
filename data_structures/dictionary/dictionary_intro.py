#Dictionary - Is comma separated key-value pair enclosed under {}
#{key1:value1, key2:value2, key3:value3, ......}
#Dictionary are mutable. We can update by accessing using the key.


groceries = { "milk": 60, "biscuits": 20, "rice": 90, "bread": 30}
print(groceries, type(groceries))
print(len(groceries))

#To fetch the value we need to use the key. We can't use index in dict
print(groceries["milk"])
print(groceries["rice"])

#Update values in dict
groceries["milk"] = 65
print(groceries)

#When we fetch value for the key which is not available it fails.
# print(groceries["eggs"]) # THis will fail

#Adding new key value pair in dict
groceries["eggs"] = 10
print(groceries)

