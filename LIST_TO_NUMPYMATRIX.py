import numpy as mynum
print("\n\n------CUTE LITTLE SHOP-------")
personlist=["chotabeam","motu","kaliya","chutke","shinchan"]
itemsbought=["redbull","samosa","laddu","cherrys","noodles"]
numberofitems=[1,2,3,4,5]
priceofitems=[200,20,10,20,50]
#CONVERTING LIST DATA INTO THE NUMPYARRAY
personlista=mynum.asarray(personlist)
itemsboughta=mynum.asarray(itemsbought)
numberofitemsa=mynum.asarray(numberofitems)
priceofitemsa=mynum.asarray(priceofitems)
#MULTIPLICATION OF THE ARRAYS
amountarray=mynum.array(numberofitemsa*priceofitemsa)

allarray=mynum.asarray([personlist,itemsbought,numberofitems,priceofitems,amountarray])
print("ALL THE DATA\n",allarray)

for i in range(0,len(personlista)):
    print(personlist[i],"TAKEN",numberofitemsa[i],itemsboughta[i],"WORTH",priceofitemsa[i])
    print(personlista[i],"HAVE TO PAY:",amountarray[i],"\n")
print("FROM THE MAIN MATRIX WHERE WE CAPTURED\nALL THE DATA ITEMS TO IT\nFROM THE INDIVIDUAL ARRAYS\n")
print("*************************************************************")
print("PERSONLIST  ITEMS  NUMBER_OF_ITEMS  PRICE_OF_EACH  TOTAL_AMOUNT\n")
print("*************************************************************")
print(allarray[0][0],"",allarray[1][0],"\t",allarray[2][0],"\t\t",allarray[3][0],"\t\t",allarray[4][0])
print(allarray[0][1],"\t  ",allarray[1][1],"\t",allarray[2][1],"\t\t",allarray[3][1],"\t\t",allarray[4][1])
print(allarray[0][2],"\t  ",allarray[1][2],"\t",allarray[2][2],"\t\t",allarray[3][2],"\t\t",allarray[4][2])
print(allarray[0][3],"   ",allarray[1][3],"\t",allarray[2][3],"\t\t",allarray[3][3],"\t\t",allarray[4][3])
print(allarray[0][4]," ",allarray[1][4],"\t",allarray[2][4],"\t\t",allarray[3][4],"\t\t",allarray[4][4])
print("_____________________________________________________________")
