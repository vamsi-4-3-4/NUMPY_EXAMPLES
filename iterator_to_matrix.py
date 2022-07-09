import numpy as mynum
items=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
iterator=iter(items)
myelements=mynum.fromiter(iterator,dtype=int)
iteratora=iter(myelements)
product=mynum.fromiter(iteratora,dtype=int)*100
sumofall=product.sum()
sumofalla=myelements.sum()

print("TAKEN ELEMENTS\n:::",myelements)
print("PRODUCT WITH 100\n:::",product)
print("NORMAL SUM OF ALL\n:::",sumofalla)
print("SUM OF PRODUCT ELEMENTS\n:::",sumofall)
