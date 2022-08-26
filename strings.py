'''
string is a datatype in python.
String is a sequence of characters enclosed in quotes

it can be single ,double or multiple qoutes


'''

a=34
c="hey! good night."
b="Dany  "
print(b)
print(type(b))
print(type(a))
print(c+b)#concatenation of 2 strings
x=b +c#concatenation by using a veriable
print(x)
print(c[0])#string indexing
print(c[0:8])#string sliceing
print(c[5:9])
print(c[:14])#minimum index taken is 0
print(c[1:])#it take max length of the string
print(c[-15:-5])#negative index taken which -15 is taken from last and -5 taken from first
print(c[0:14:2])# start :end : skiptimes it print "h" then skip1 string then print "y" so on...
print(c[0:14:3])#it print "h" then skip 2 then print "!"  then so on..
