#Brad Bosak, is_multiple_function

#This is a function that determines if the first parameter is a multiple of the second parameter
def is_multiple(n, m):
   "multiples description"
   if m % n == 0:
       print("True")
   else:
       print ("False")
       
is_multiple(5,15)