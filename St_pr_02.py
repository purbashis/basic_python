#write a program to fill a letter templete given replace the name and date according to your input
letter=''' dear <|name|>,
You are  selected!

Thank You.
Date <|date|> ''' 
name =input("enter the  name of the candidate ")
date=input(" date")
letter =letter.replace("<|name|>",name)
letter =letter.replace("<|date|>",date)
print(letter)