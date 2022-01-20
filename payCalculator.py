def calculatePay():
    # Implement your solution in between the two comment blocks
    #print("calculating pay")
    
    # This first line is provided for you
    input_hrs = input('Enter Hours: ')
    input_rate = input('Enter Rate: ')

    PAY = float(input_hrs) * float(input_rate)

    print(PAY)
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()