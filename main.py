def main():
   ##################################################
   # Comlete your code here
   ##################################################
   original_price = 200
   rate = 0.20
   original_price = int(input("Enter Original Price: "))
   
   rate = float(input("Enter Discount Rate: "))
   # In this Lab, we assume the "rate" is percentage like 20. 
   # You should convert this rate as a fractional value like 0.2
 
   
   discount_ammount = original_price * rate  # this statement should be "original_price * rate / 100 "
   
   print (original_price)
   print(discount_ammount)
   print(original_price - discount_ammount)





pass


if __name__ == '__main__':
    main()
