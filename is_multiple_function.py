#Brad Bosak, is_multiple_function

#This is a function that determines if the first parameter is a multiple of the second parameter
def is_multiple(n, m):
   "multiples description"
   if m % n == 0:
       print("True")   #The function will display "True" if n is a multiple of m
       return True     #The function will return True as well.  I did this to demonstrate the return feature of a function
   else:
       print("False")  #Likewise, the other part of the control flow will print and return False
       return False
       
is_multiple(5,15)