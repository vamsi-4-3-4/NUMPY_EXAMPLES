import numpy as mynum

#--------------------------------
#||| generating an araay with |||
#|||      a given range       |||
#--------------------------------
myarray=mynum.linspace(0,10,3,dtype=mynum.int)
myarraya=mynum.linspace(0,1,2,dtype=mynum.int)
myarrayb=mynum.linspace(1.0,99.0,10)
myarrayc=mynum.linspace(0.0,1.0,20)
print("GENERATING 3 VALUES BETWEEN 0-10\n:::",myarray)
print("\nGENERATING 2 VALUES BETWEEN 0-1\n:::",myarraya)
print("\nGENERATING 10 VALUES BETWEEN 1.O AND 99.O\nWITH THE EVENLY SPACE BETWEEN ELEMENTS\n:::",myarrayb)
print("\n20 VALUES BETWEEN 0.0-1.O\n:::",myarrayc)
#GENERATING AN EMPTY ARRAY
print("\n\nGENERATING 2*2 MATRIX WITH FLOAT NUMBERS")
myempty=mynum.empty((2,2),dtype=mynum.float)
print(myempty)

myemptya=mynum.empty((3,3),dtype=mynum.int)
print("\n\nGENERATING 3*3 MATRIX WITH INTEGERS ",myemptya)

myzeroarray=mynum.zeros((2,2),dtype=int)
print("\n\nGENERATING 2*2 MATRIX WITH ZER0S\n",myzeroarray)

myzeroarraya=mynum.zeros((3,3),dtype=int)
print("\n\nGENERATING 3*3 MATRIX WITH ZER0S\n",myzeroarraya)


myzeroarrayb=mynum.zeros((4,2),dtype=int)
print("\n\nGENERATING 4*2 MATRIX WITH ZER0S\n",myzeroarrayb)
myzeroarrayc=mynum.zeros((4,4),dtype=int)
print("\n\nGENERATING 4*4 MATRIX WITH ZER0S\n",myzeroarrayc)


myones=mynum.ones((2,2),dtype=int)
print("\n\nGENERATING 2*2 MATRIX WITH ONES\n",myones)

myonesa=mynum.ones((6,6),dtype=float)
myonesaa=mynum.round([myonesa],decimals=10)
print("\n\nGENERATING 6*6 MATRIX WITH FLOAT ONES\n",myonesaa)


