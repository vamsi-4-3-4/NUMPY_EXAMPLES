import numpy as mynum
#GENERATING MATRIX FOR THE 0 TO 99 ELEMENTS
zerotoninenine=mynum.arange(100)
#RESHAPPING AS 10*10 MATRIX
generated=zerotoninenine.reshape(10,10)
print("GENERATED MATRIX\n",generated)
#PRINTING ONLY THE DIAGONAL ELEMENTS

diagonalelements=mynum.diag(generated)
print("\n\nDIAGONAL ELEMENTS ARE:\n",diagonalelements)

makingotherzero=mynum.diag(mynum.diag(generated))
print("\n\nMAKING OTHER ELEMENTS AS ZERO OTHERTHAN DIAGONAL\n",makingotherzero)
diagonalb=mynum.diag(mynum.diag(generated,k=-1))
print("\nGNERATED MATRIX\n",diagonalb)

diagonalb=mynum.diag(mynum.diag(generated,k=-2))
print("\nGNERATED MATRIX\n",diagonalb)

diagonalb=mynum.diag(mynum.diag(generated,k=-3))
print("\nGNERATED MATRIX\n",diagonalb)

diagonalc=mynum.diag(mynum.diag(generated,k=-4))
print("\nGENERATED MATRIX\n",diagonalc)

diagonald=mynum.diag(mynum.diag(generated,k=-5))
print("\nGENERATED MATRIX\n",diagonald)

diagonald=mynum.diag(mynum.diag(generated,k=-6))
print("\nGENERATED MATRIX\n",diagonald)

diagonale=mynum.diag(mynum.diag(generated,k=-7))
print("\nGENERATED MATRIX\n",diagonale)
diagonalf=mynum.diag(mynum.diag(generated,k=-8))
print("\nGENERATED MATRIX\n",diagonalf)
diagonalg=mynum.diag(mynum.diag(generated,k=-9))
print("\nGENERATED MATRIX\n",diagonalg)
diagonalh=mynum.diag(mynum.diag(generated,k=-10))
print("\nGENERATED MATRIX\n",diagonalh)
diagonali=mynum.diag(mynum.diag(generated,k=-11))
print("\nGENERATED MATRIX\n",diagonali)
diagonalj=mynum.diag(mynum.diag(generated,k=9))
print("\nGENERATED MATRIX\n",diagonalj)
diagonalK=mynum.diag(mynum.diag(generated,k=8))
print("\nGENERATED MATRIX\n",diagonalK)
diagonall=mynum.diag(mynum.diag(generated,k=7))
print("\nGENERATED MATRIX\n",diagonall)

diagonalm=mynum.diag(mynum.diag(generated,k=6))
print("\nGENERATED MATRIX\n",diagonalm)

diagonaln=mynum.diag(mynum.diag(generated,k=5))
print("\nGENERATED MATRIX\n",diagonaln)

diagonalo=mynum.diag(mynum.diag(generated,k=4))
print("\nGENERATED MATRIX\n",diagonalo)

diagonalp=mynum.diag(mynum.diag(generated,k=3))
print("\nGENERATED MATRIX\n",diagonalp)

diagonalq=mynum.diag(mynum.diag(generated,k=2))
print("\nGENERATED MATRIX\n",diagonalq)

diagonalr=mynum.fliplr(generated).diagonal()
print("\nGENERATED MATRIX\n",diagonalr)

diagonals=mynum.flipud(generated).diagonal()
print("\nGENRATED MATRIX\n",diagonals)















