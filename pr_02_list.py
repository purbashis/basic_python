#write  a program that it accepts marks of 6 students and display it in a sorted manner.
s1=int(input("enter the marks of student of roll 1 : "))
s2=int(input("enter the marks of student of roll 2  : "))
s3=int(input("enter the marks of student of roll 3  :"))
s4=int(input("enter the marks of student of roll 4  :"))
s5=int(input("enter the marks of student of roll 5  :"))
s6=int(input("enter the marks of student of roll 6  :"))
s7=int(input("enter the marks of student of roll 7  :"))

StudentMarks=[s1, s2, s3, s4, s5, s6, s7]
StudentMarks.sort()
print ("StudentMarks is sorted order \n",StudentMarks)