import numpy as mynum

mypassword=b"1@1@1sgabc"
print("\nMY BYTE STREAM\n:::",mypassword,"\n\nMY BYTE STREAM TYPE\n:::",type(mypassword))



mypassworda=mynum.frombuffer(mypassword,dtype="S1")
print("\n\n\n")
#
a=(list(str(mypassword)))
newls=[]
for i in range(0,len(a)-1):
    if i>=2:
        newls.append(a[i])
#
counting_password={}
for myitem in newls:
    if myitem in counting_password:
        counting_password[myitem]+=1
    else:
        counting_password[myitem]=1

characters=list(counting_password.keys())
characterss=mynum.asarray(characters)
countins=list(counting_password.values())
countinss=mynum.asarray(countins)
countmatrix=mynum.asarray([characterss,countinss])
print("PASSWORD CHARACTERS COUNT\n\n")
print(countmatrix)


