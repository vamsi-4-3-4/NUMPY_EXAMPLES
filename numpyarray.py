import numpy as mynum
print("DAILY SALES OF A MONTH\n")
dailysales=mynum.array([[998844,998845,998846,998847,998848,998849,998850],[998852,998853,998854,998855,998856,998857,998858],[998859,998860,998861,998862,998863,998864,998865],[998866,998867,998868,998869,998870,998871,998871],[998872,998873,998874]])
#SIZE OF THE  ARRAY
findingsize=dailysales.size
print("SHOWING SALES OF",findingsize,"WEEKS\n")
#PRINTING ARRAY
print(dailysales,"\n")
#ARRAY ELEMENT
print("WEEK ONE SALES SHOWING FOR",len(dailysales[0]),"DAYS\n",dailysales[0])
print("WEEK TWO SALES SHOWING FOR",len(dailysales[1]),"DAYS\n",dailysales[1])
print("WEEK THREE SALES SHOWING FOR",len(dailysales[2]),"DAYS\n",dailysales[2])
print("WEEK FOUR SALES SHOWING FOR",len(dailysales[3]),"DAYS\n",dailysales[3])
print("WEEK FIVE SALES SHOWING FOR",len(dailysales[4]),"DAYS\n",dailysales[4])

#************************
#||| slicing arrays |||||
#------------------------
weekone=mynum.array(dailysales[0])
weektwo=mynum.array(dailysales[1])
weekthree=mynum.array(dailysales[2])
weekfour=mynum.array(dailysales[3])
weekfive=mynum.array(dailysales[4])
#^^^^^^^^^^^^^^^^^^^^
#||| MAXIMUM      |||
#--------------------
print("\n\nMAXIMUM AMOUNT GAINED IN THE WEEK")
print("MAXIMUM AMOUNT GAINED IN WEEK ONE:",weekone.max())
print("MAXIMUM AMOUNT GAINED IN WEEK TWO:",weektwo.max())
print("MAXIMUM AMOUNT GAINED IN WEEK THREE:",weekthree.max())
print("MAXIMUM AMOUNT GAINED IN WEEK FOUR:",weekfour.max())
print("MAXIMUM AMOUNT GAINED IN WEEK FIVE:",weekfive.max())


#*******************
#||| MINIMUM ||||
#----------------
print("\n\nMINIMUM AMOUNTS GAINED IN THE WEEK")
print("MINIMUM AMOUNT GAINED IN WEEK ONE:",weekone.min())
print("MINIMUM AMOUNT GAINED IN WEEK TWO:",weektwo.min())
print("MINIMUM AMOUNT GAINED IN WEEK THREE:",weekthree.min())
print("MINIMUM AMOUNT GAINED IN WEEK FOUR:",weekfour.min())
print("MINIMUM AMOUNT GAINED IN WEEK FIVE:",weekfive.min())


#------------
#||| SUM |||
#-----------
print("\n\nWEEKELY TURNOVERS")
weekoneturn=weekone.sum()
weektwoturn=weektwo.sum()
weekthreeturn=weekthree.sum()
weekfourturn=weekfour.sum()
weekfiveturn=weekfive.sum()
print("WEEK ONE TURNOVER:",weekoneturn)
print("WEEK TWO TURNOVER:",weektwoturn)
print("WEEK THREE TURNOVER:",weekthreeturn)
print("WEEK FOUR TURNOVER:",weekfourturn)
print("WEEK FIVE TURNOVER:",weekfiveturn)

print("\n\nMONTHLY TURNOVER:",weekoneturn+weektwoturn+weekthreeturn+weekfourturn+weekfiveturn)

print("LOWEST SALES IN WEEK ONE 6991929")
print("HIGHEST SALES IN WEEKFOUR 6992082")

#----------------------
#||| NUMPY FUNCTIONS |||
#-----------------------
print("\n\nFEW OTHER NUMPY ARRAY FUNCTIONS")
print("\nNORMAL ARRAY")
complexdatatypen=mynum.array([3,30,9,90,99],dtype=int)
print(complexdatatypen)
print("\nCOMPLEX ARRAY")
complexdatatype=mynum.array([3,30,9,90,99],dtype=complex)
print(complexdatatype)

#***************
#|| dimensions ||
#---------------
print("\n\nARRAY DIMENSIONS")
print("\nARRAY WITH ONE ROW")
onerow=mynum.array([[99,999,9999,99999,999999],[1,2,3,4,5]])
print(onerow)
print("DIMENSIONS OF THE ARRAY:",onerow.ndim)
print("ABOVE ARRAY WAS WITH",onerow.shape,"2 ROWS AND 5 COLUMNS")

#------------
#|| itemsize||
#------------

print("\n\nITEM SIZE")
print("SIZE OF EACH ELEMENT IN WEEK ONE ARRAY IS:",weekone.itemsize,"BYTES")

#-----------
#|| dtype ||
#-----------

intarray=mynum.array([3,30,9.9999,99],dtype=mynum.int)
floatarray=mynum.array([3,30.00,99.99,999],dtype=mynum.float32)

print(mynum.round([intarray],decimals=10))
print(mynum.round([floatarray],decimals=10))


#*****************
#||| reshapping |||
#-----------------
print("\n\nARRAY RESHAPPING")
print("\nARRAY BEFORE RESHAPPING")
reshapearray=mynum.array([[9,99,999,9999],[3,33,333,33333],[2,22,222,2222],[7,77,777,7777]])
print(reshapearray)
print("\nARRAY AFTER RESHAPPING")
print(reshapearray.reshape(8,2))


