myDict={

"purbashis" : "gamer",
"marks" : "100",
"list" : [1,5,6,7,8,9,10,11,12],
"anotherdict" : {'dantz' : 'daddy ',
'nepal':'momo',
'daddy':'mummy',
'plugin':'json'
}
}
#dictionary methods
print(list(myDict.keys())) #prints the keys of the dictionary - list type casting
print(myDict.keys()) #prints the keys of the dictionary.
print(myDict.items()) #prints the all  (keys ,values) for all contents of dictionary
print(myDict.values()) #prints the values of the dictionary.


#update the dictionary
newDict_update={
    "lovish": "Friend",
    "subham": "friends",
    "yt":"sub"
}


myDict.update(newDict_update) # update the dictionary by adding key - value pairs from newDict_update 
print("################################")
print("after update of dictionary of myDict")
print(myDict)
print(myDict.get("lovish")) # it use to
print(myDict.get("subham2"))#it returns subham2 is not present in the dictionary and it shows none  in the output pannel.


