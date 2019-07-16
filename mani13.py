mr = int(input())  
  
if mr > 1:  
   for i in range(2,mr):  
       if (mr % i) == 0:  
           print("no")  
           break  
   else:  
       print("yes")  
         
else:  
   print("no")
