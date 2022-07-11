import numpy as mynum

mylog=mynum.logspace(0,12,3)
print("LOGSPACE GENERATES THE LOG VALUES \nBETWEEN THE SPECIFIED VALUES FOR THE \nSPECIFIED NUMBER OF ELEMENTS\nGENERATING 3 LOG VALUES BETWEEN 0-12\n",mylog)
#MESH GRID 
print("\nGENERATING MESH GRID")
grida=mynum.array([-9,-3,0,3,9])
gridb=mynum.array([-3,-9,0,3,9])
grida,gridb=mynum.meshgrid(grida,gridb)
print("\nGRID A\n",grida)
print("\nGRID B\n",gridb)
print("\nGRID_A + GRID_B\n",grida+gridb)
print("\nGRID A\n",grida)
print("\nGRID B\n",gridb)
print("\nGRID_A - GRID_B\n",grida-gridb)
print("\nGRID A\n",grida)
print("\nGRID B\n",gridb)
print("\nGRID_A * GRID_B\n",grida*gridb)
#RANDOM
myrandom=mynum.random.rand(10)
print("\nRANDOM.RAND GENERATES THE SPECIFIED NUMBER OF \n RANDOM NUMBERS BETWEEN 0-1")
print("\nGENERATING 10 RANDOM NUMBERS BETWEEN 0-1\n",myrandom)
myrandoma=mynum.random.randint(0,10,14)
print("\nGNERATING 14 RANDOM NUMBERS BETWEEN 0-10\n",myrandoma)

print("\nFILLING ALL ARRAY ELEMENTS WITHT THE SPECIFIED NUMBER\n")
#myfullarray=numpy.full(number of times,number required)
#required number:9 for 5 times
myfullarray=mynum.full(5,9)
print("FILIING A ARRAY WITH 5 9`S\n",myfullarray)
myfullarraya=mynum.full(9,99)
print("FILLING A ARRAY WITH 9 99`S \n",myfullarraya)
myfullarrayb=mynum.full(10,3)
print("FILLING A ARRAY WITH 10 3`S\n",myfullarrayb)
myidentity=mynum.identity(6)
myidentitya=mynum.identity(5)
myidentityb=mynum.identity(4)
myidentityc=mynum.identity(3)
print("\nGENERATING IDENTITY MATRIX\n")
print("\n6*6 IDENTITY MATRIX\n",myidentity)
print("\n5*5 IDENTITY MATRIX\n",myidentitya)
print("\n4*4 IDENTITY MATRIX\n",myidentityb)
print("\n3*3 IDENTITY MATRIX\n",myidentityc)
myeye=mynum.eye(6)
myeyea=mynum.eye(5)
myeyeb=mynum.eye(7)
print("\nGENERATING EYE MATRIX\n")
print("\n6*6 GENERATED EYE\n",myeye)
print("\n5*5 GENERATED EYE\n",myeyea)
print("\nGENERATING 7*7 EYE\n",myeyeb)
print("\nOTHER VARIANTS OF EYE MATRIX\n")
myeyec=mynum.eye(9,k=-1)
myeyed=mynum.eye(9,k=-3)
myeyee=mynum.eye(9,k=3)
myeyef=mynum.eye(9,k=5)
print("\n9*9EYE MATRIX VARIANT1\n",myeyec)
print("\n9*9EYE MATRIX VARIANT1\n",myeyed)
print("\n9*9EYE MATRIX VARIANT1\n",myeyee)
print("\n9*9EYE MATRIX VARIANT1\n",myeyef)

print("\nDIAG AND ARANGE\n")
mydiagarange=mynum.diag(mynum.arange(0,100,10))
print("\nDIAG AND ARANGE\n",mydiagarange)