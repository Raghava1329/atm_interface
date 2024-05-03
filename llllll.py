from datetime import datetime
import time

print("DATE AND TIME:",datetime.now())

print("PLEASE INSERT YOUR CARD")

time.sleep(1.5)

passcode=1800

time.sleep(1)

secret_pin=int(input("PLEASE ENTER YOUR SECRET PIN :"))
c_balance = 1239

if secret_pin == passcode:
    while True:

     print(""" PLEASE SELECT NUMBER
           1 >> BALANCE ENQUIRY
           2 >> WITHDRAWL AMOUNT
           3 >> DEPOSIT AMOUNT
           4 >> EXIT 
          """
          )

     try:
         option=int(input("PLEASE ENTER YOUR TRANSACTION NUMBER :"))
     except:
         print(" ")


     if option==1:
         print(f"CURRENT BALANCE : {c_balance}")

     if option==2:

         w_amount=int(input("ENTER THE AMOUNT :"))
         if  w_amount <= c_balance:
                
                c_balance=c_balance-w_amount
                
                print(f"REMAINING AMOUNT :{c_balance}")
         elif  w_amount > c_balance:
                print("*****TRANSACTION CANCELLED*****")     

     if option==3:

         deposit_amount=int(input("PLEASE ENTER DEPOSIT NUMBER :"))

         c_balance=c_balance+deposit_amount

         print(f"CURRENT BALANCE : {c_balance}")

     if option == 4:
         print("""
               *****TRANSACTION CANCELLED*****
               THANK YOU AND HAVE A NICE DAY
               """
               )
         break
     if option > 4 or option==0:
         print("******INVALID TRANSACTION NUMBER******")
else:print("""
      WRONG PIN!!!!!!! 
      TRY AGAIN.....""")