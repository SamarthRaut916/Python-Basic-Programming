

#READ FILE....

fileName="atext.txt"

fileRead=open(fileName,"r").read()

print(fileRead)




#Create New File & WRITING FILE....
newFileName="atext.txt"

data="""
            jhjfed jhsdfk kjhsdjfi aaskfh 
"""
open(newFileName,"w+").write(data)

#Priint RAndom Text:-
import random
num=random.randint(0,10)
print(num)

#Append Method..
fileNAme="atext.txt"

open(fileNAme,"w+").write(data)

