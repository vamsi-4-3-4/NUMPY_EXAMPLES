import numpy as mynum
import matplotlib.pyplot as mypyplot
import matplotlib

mymatrix=mynum.array([[99,999,9],[3,33,333],[2,22,222]])
print("\nMY COMPLETE MATRIX\n",mymatrix)
runs=mynum.linspace(0,10)
balls=mynum.linspace(0,120)
over1=[1,2,3,4,5,6]
over2=[4,4,4,4,4,4]

mypyplot.plot(runs,over1)
#mypyplot.plot(balls,over1)
mypyplot.show()
