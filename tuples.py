#creating a tupple using()

t=(1,2,5,8)
#printing the tupple
print(t)
print (t[0])

#you can not update the value of the tupple 


''' 
t[0]=55

print(t)

t[0]=55
TypeError: 'tuple' object does not support item assignment'''
########################################################################
'''
t1=() empty tuple
t1=(1,) tuple with single element (right way )
t1=(1) wrong way and it throws an error

'''
t1=()
print(t1)
t1=(2,)
print(t1)

###############################
'''
tuple methods
'''
#count

t2=(1,2,4,1,6,1,1,8)
# it should be print 4  coz count of 1 =4 from this tuple
print(t2.count(1))
#it should be print the index number 
print(t2.index(4))