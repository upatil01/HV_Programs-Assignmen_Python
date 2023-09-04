# ### three variables 
# book1 = int("Introduction to Python Programming : 499")
# book2 = int("Python Libraries Cookbook : 855 ")
# book3 = int("Data Science in Python : 645 ")
# ### add 
# add = ( int(book1 + book2 + book3))
# ### 12% of add
# gst = (int(add) * 12) / 100
# deliverycharges = 250
# calculate = ( int(gst) + int(deliverycharges))
# print ( " The total invoice amount is : " (calculate))


# book1 =  499
# book2 =  855
# book3 =  645 
# ### add 
# add = (book1 + book2 + book3)
# ### 12% of add
# gst = (add * 12) / 100
# deliverycharges = 250
# calculate = ( add + gst+ deliverycharges)
# print ( " The total invoice amount is : " , (calculate))


###take expenses for Python course
book1 = 499
print( " Introduction to python programming : Rs." , book1) 

book2 = 855
print(" Python Libraries Cookbook : Rs." , book2)

book3 = 645
print(" Data Science in Python : Rs." , book3)

###Addition of all three expenses
add = ( book1 +book2 +book3 )

###calculate gst 12% on the total expenses
gstc = 12 
print(" GST :" , gstc , "%")
gst = (add * 12) / 100

deliverycharges = 250
print( " The delivery charges : Rs." , deliverycharges)

##add total expenses, GST on total expenses & delivery charges
calculate =( add + gst + deliverycharges) 
print( " The total invoice amount is Rs." , (calculate))